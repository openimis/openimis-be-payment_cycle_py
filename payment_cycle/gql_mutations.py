import graphene
from django.core.exceptions import PermissionDenied
from django.utils.translation import gettext as _

from core.schema import OpenIMISMutation
from payment_cycle.apps import PaymentCycleConfig
from payment_cycle.models import PaymentCycleMutation, PaymentCycle
from payment_cycle.services import BenefitPlanPaymentCycleService


class ProcessBenefitPlanPaymentCycleMutation(OpenIMISMutation):
    _mutation_module = "payment_cycle"
    _mutation_class = "ProcessBenefitPlanPaymentCycleMutation"

    class Input(OpenIMISMutation.Input):
        year = graphene.Int()
        month = graphene.Int()

    @classmethod
    def async_mutate(cls, user, **data):
        client_mutation_id = data.pop('client_mutation_id', None)
        if not user.has_perms(PaymentCycleConfig.gql_mutation_process_payment_cycle_perms):
            raise PermissionDenied(_("unauthorized"))
        res = BenefitPlanPaymentCycleService(user).process(**data)
        if client_mutation_id and res['success']:
            payment_cycle_id = res['data']['id']
            payment_cycle = PaymentCycle.objects.filter(id=payment_cycle_id)
            PaymentCycleMutation.object_mutated(
                user, client_mutation_id=client_mutation_id, payment_cycle=payment_cycle
            )
        return res if not res['success'] else None
