from .models import Transaction, Category
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
			}, format=("%Y-%m-%d")),
		}

	
class CategoriesForm(ModelForm):
	class Meta:
		model = Category
		fields = ['name']

		widgets = {
			'name': TextInput(attrs={
				'placeholder': 'Название',
			})
		}