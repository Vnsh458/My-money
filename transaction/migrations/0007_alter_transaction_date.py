# Generated by Django 4.1.13 on 2024-02-18 07:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0006_incomecategory_alter_transaction_date_income'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата'),
        ),
    ]
