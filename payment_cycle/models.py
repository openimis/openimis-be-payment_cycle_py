from django.contrib.contenttypes.models import ContentType
from django.db import models

from core.models import HistoryModel, UUIDModel, ObjectMutation, MutationLog


class PaymentCycle(HistoryModel):
    run_year = models.IntegerField()
    run_month = models.SmallIntegerField()
    type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING, null=True, unique=False)



class PaymentCycleMutation(UUIDModel, ObjectMutation):
    payment_cycle = models.ForeignKey(PaymentCycle, models.DO_NOTHING, related_name='mutations')
    mutation = models.ForeignKey(
        MutationLog, models.DO_NOTHING, related_name='payment_cycle')

    class Meta:
        managed = True
        db_table = "payment_cycle_PaymentCycleMutation"
