# Generated by Django 4.1.13 on 2024-02-18 07:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0007_alter_transaction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Дата'),
        ),
    ]
