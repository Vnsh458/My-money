from datetime import datetime
from django.db import models


class Category(models.Model):
	class Meta:
		db_table = 'category'
		verbose_name = 'Категорию'
		verbose_name_plural = 'Категории'

	name = models.CharField(max_length=30, blank=False, verbose_name='Название')

	def __str__(self):
			return f'{self.name}'
	
	def get_absolute_url(self):
		return '/'


class IncomeCategory(models.Model):
	class Meta:
		db_table = 'income category'
		verbose_name = 'Категорию дохода'
		verbose_name_plural = 'Категории дохода'
	
	name = models.CharField(max_length=30, blank=False, verbose_name='Название')

	def __str__(self):
		return f'{self.name}'
	
	def get_absolute_url(self):
		return '/'


class Income(models.Model):
	class Meta:
		db_table = 'income'
		verbose_name = 'Доход'
		verbose_name_plural = 'Доходы'
	
	date = models.DateField(verbose_name='Дата', default=datetime.now)
	name = models.CharField(max_length=30, blank=False, verbose_name='Название')
	expenses = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Доход')
	category = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE, verbose_name='Категория')

	def __str__(self):
		return f'{self.name} {self.date}'
	
	def get_absolute_url(self):
		return '/'

class Transaction(models.Model):
	class Meta:
		db_table = 'transaction'
		verbose_name = 'Транзакцию'
		verbose_name_plural = 'Транзакции'

	date = models.DateField(verbose_name='Дата', default=datetime.now)
	name = models.CharField(max_length=30, blank=False, verbose_name='Название')
	expenses = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Сумма')
	category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

	def __str__(self):
		return f'{self.name} {self.date}'
	
	def get_absolute_url(self):
		return '/'
	
