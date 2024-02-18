# Generated by Django 4.1.13 on 2024-02-18 02:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0005_alter_transaction_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='IncomeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категорию дохода',
                'verbose_name_plural': 'Категории дохода',
                'db_table': 'income category',
            },
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Дата'),
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now, verbose_name='Дата')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('expenses', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Доход')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.incomecategory', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Доход',
                'verbose_name_plural': 'Доходы',
                'db_table': 'income',
            },
        ),
    ]
