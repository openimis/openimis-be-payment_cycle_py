from django.apps import AppConfig

from core.rights_declaration import RightsDeclaration

MODULE_NAME = 'payment_cycle'


# Rights, by entity then by action.
DJANGO_PERMS = {
    "paymentCycle": {
        "query": ("payment_cycle.view_paymentcycle", 200001),
        "create": ("payment_cycle.add_paymentcycle", 200002),
        "update": ("payment_cycle.change_paymentcycle", 200003),
        "delete": ("payment_cycle.delete_paymentcycle", 200004),
    },
}

_PERM_CFG = {
    "gql_query_payment_cycle_perms": ("paymentCycle", "query"),
    "gql_create_payment_cycle_perms": ("paymentCycle", "create"),
    "gql_update_payment_cycle_perms": ("paymentCycle", "update"),
    "gql_delete_payment_cycle_perms": ("paymentCycle", "delete"),
}

RIGHTS = RightsDeclaration(MODULE_NAME, DJANGO_PERMS, _PERM_CFG)

perms = RIGHTS.perms
django_perms = RIGHTS.django_perm_names
configured_perms = RIGHTS.configured
require = RIGHTS.require


DEFAULT_CONFIG = {
    'gql_check_payment_cycle': True,
    "payment_cycle_benefits_field_mapping": {
        'payrollbenefitconsumption__payroll__payment_cycle__code': 'Payment Cycle Code',
        'payrollbenefitconsumption__payroll__name': 'Payroll Name',
        'payrollbenefitconsumption__payroll__status': 'Payroll Status',
        'individual__first_name': 'First Name',
        'individual__last_name': 'Last Name',
        'individual__dob': 'Date of Birth',
        'code': 'Code',
        'status': 'Status',
        'amount': 'Amount',
        'type': 'Type',
        'receipt': 'Receipt',
    },
    "payment_cycle_benefits_paid_yes": "Yes",
    "payment_cycle_benefits_paid_no": "No",
    "payment_cycle_benefits_status_column": "Status",
}


class PaymentCycleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = MODULE_NAME

    # Rights: constants, no longer overridable. They go neither through DEFAULT_CFG
    # nor through ready(): `ModuleConfiguration.get_or_default` now ignores any
    # `_perms` key stored in the database.
    gql_query_payment_cycle_perms = RIGHTS.perms("paymentCycle", "query")
    gql_create_payment_cycle_perms = RIGHTS.perms("paymentCycle", "create")
    gql_update_payment_cycle_perms = RIGHTS.perms("paymentCycle", "update")
    gql_delete_payment_cycle_perms = RIGHTS.perms("paymentCycle", "delete")
    gql_check_payment_cycle = None
    payment_cycle_benefits_field_mapping = None
    payment_cycle_benefits_paid_yes = None
    payment_cycle_benefits_paid_no = None
    payment_cycle_benefits_status_column = None

    def ready(self):
        from core.models import ModuleConfiguration

        cfg = ModuleConfiguration.get_or_default(self.name, DEFAULT_CONFIG)
        self.__load_config(cfg)

    @classmethod
    def __load_config(cls, cfg):
        """
        Load all config fields that match current AppConfig class fields, all custom fields have to be loaded separately
        """
        for field in cfg:
            if hasattr(PaymentCycleConfig, field):
                setattr(PaymentCycleConfig, field, cfg[field])
