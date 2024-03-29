# Generated by Django 4.2.9 on 2024-02-07 16:47

import core.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('payment_cycle', '0002_add_pc_rights_to_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalpaymentcycle',
            name='date_created',
            field=core.fields.DateTimeField(db_column='DateCreated', default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='historicalpaymentcycle',
            name='date_updated',
            field=core.fields.DateTimeField(db_column='DateUpdated', default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='paymentcycle',
            name='date_created',
            field=core.fields.DateTimeField(db_column='DateCreated', default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='paymentcycle',
            name='date_updated',
            field=core.fields.DateTimeField(db_column='DateUpdated', default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='paymentcycle',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='contenttypes.contenttype'),
        ),
        migrations.AlterField(
            model_name='paymentcycle',
            name='user_created',
            field=models.ForeignKey(db_column='UserCreatedUUID', on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_user_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='paymentcycle',
            name='user_updated',
            field=models.ForeignKey(db_column='UserUpdatedUUID', on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_user_updated', to=settings.AUTH_USER_MODEL),
        ),
    ]
