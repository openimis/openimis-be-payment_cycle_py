# Generated by Django 3.2.24 on 2024-03-11 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment_cycle', '0004_add_start_and_end_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalpaymentcycle',
            name='run_year',
        ),
        migrations.RemoveField(
            model_name='historicalpaymentcycle',
            name='run_month',
        ),
        migrations.RemoveField(
            model_name='paymentcycle',
            name='run_year',
        ),
        migrations.RemoveField(
            model_name='paymentcycle',
            name='run_month',
        ),
    ]
