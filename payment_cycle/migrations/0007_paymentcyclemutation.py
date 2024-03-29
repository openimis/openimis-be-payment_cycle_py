# Generated by Django 3.2.24 on 2024-03-20 12:33

import core.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_alter_interactiveuser_last_login_and_more'),
        ('payment_cycle', '0006_auto_20240315_0943'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentCycleMutation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('mutation', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='payment_cycle', to='core.mutationlog')),
                ('payment_cycle', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='mutations', to='payment_cycle.paymentcycle')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, core.models.ObjectMutation),
        ),
    ]
