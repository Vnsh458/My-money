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
	
