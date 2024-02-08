from .models import Transaction
from django.forms import ModelForm, TextInput, DateTimeInput


class TransactionForm(ModelForm):
	class Meta:
		model = Transaction
		fields = ['date', 'name', 'category', 'expenses']

		widgets = {
			'name': TextInput (attrs={
				'placeholder': 'Название'
			}),
			'date': DateTimeInput (attrs={
				'placeholder': 'Дата'
			})
		}