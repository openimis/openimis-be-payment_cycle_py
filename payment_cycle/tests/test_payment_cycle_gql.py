from graphene import Schema
from graphene.test import Client

from core.models.openimis_graphql_test_case import openIMISGraphQLTestCase, BaseTestContext
from core.test_helpers import LogInHelper
from payment_cycle.models import PaymentCycle
from payment_cycle.schema import Query
from payment_cycle.services import PaymentCycleService


class PaymentCycleSearchGQLTestCase(openIMISGraphQLTestCase):
    """The `search` argument of the paymentCycle query, used by the PaymentCyclePicker."""

    query = """
        query ($search: String) {
          paymentCycle(search: $search, isDeleted: false, first: 50) {
            edges { node { code } }
          }
        }
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = LogInHelper().get_or_create_user_api()
        cls.gql_client = Client(Schema(query=Query))
        cls.gql_context = BaseTestContext(cls.user)
        service = PaymentCycleService(cls.user)
        for code in ('SRCHAA01', 'SRCHBB02', 'OTHERC03'):
            result = service.create({
                'code': code,
                'start_date': '2026-01-01',
                'end_date': '2026-01-31',
                'status': PaymentCycle.PaymentCycleStatus.ACTIVE,
            })
            assert result.get('success'), result

    def _codes(self, search):
        result = self.gql_client.execute(
            self.query, context=self.gql_context.get_request(), variables={'search': search})
        self.assertIsNone(result.get('errors'), result.get('errors'))
        return {edge['node']['code'] for edge in result['data']['paymentCycle']['edges']}

    def test_search_restricts_to_matching_codes(self):
        self.assertEqual(self._codes('srchbb'), {'SRCHBB02'})

    def test_search_matches_part_of_the_code(self):
        self.assertEqual(self._codes('SRCH'), {'SRCHAA01', 'SRCHBB02'})

    def test_empty_search_does_not_filter(self):
        self.assertTrue({'SRCHAA01', 'SRCHBB02', 'OTHERC03'} <= self._codes(''))
