from django.contrib.contenttypes.models import ContentType
from django.test import TestCase

from contribution_plan.models import PaymentPlan
from core.datetimes.ad_datetime import datetime
from individual.models import Individual
from invoice.models import Bill
from payment_cycle.models import PaymentCycle
from payment_cycle.tests.data import benefit_plan_payload, individual_payload, beneficiary_payload, payment_plan_payload
from payment_cycle.services import PaymentCycleService
from payment_cycle.tests.helpers import LogInHelper
from social_protection.models import BenefitPlan, Beneficiary


class BenefitPlanPaymentCycleServiceTests(TestCase):
    user = None
    service = None

    test_benefit_plan = None
    test_individual_1 = None
    test_individual_2 = None
    test_beneficiary_1 = None
    test_beneficiary_2 = None
    test_payment_plan = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = LogInHelper().get_or_create_user_api()
        cls.service = PaymentCycleService(cls.user)
