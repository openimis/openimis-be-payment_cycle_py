import graphene
from django.core.exceptions import PermissionDenied
from django.utils.translation import gettext as _

from core.schema import OpenIMISMutation
from payment_cycle.apps import PaymentCycleConfig
from payment_cycle.services import PaymentCycleService


class ProcessBenefitPlanPaymentCycleMutation:
    _mutation_module = "payment_cycle"
    _mutation_class = "ProcessPaymentCycleMutation"

    class Input(OpenIMISMutation.Input):
        year = graphene.Int()
        month = graphene.Int()

    @classmethod
    def async_mutate(cls, user, **data):
        if not user.has_perms(PaymentCycleConfig.gql_mutation_process_payment_cycle_perms):
            raise PermissionDenied(_("unauthorized"))
        res = PaymentCycleService(user).process(**data)
        return res if not res['success'] else None
