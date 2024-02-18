from django.shortcuts import redirect, render, get_object_or_404
from rest_framework.viewsets import ModelViewSet
from django.views.generic import UpdateView
from .serializers import OrderSerializer
from datetime import datetime

from .models import Transaction, Category
from .forms import TransactionForm, CategoriesForm


def start_page(request):
	error = ''
	if request.method == 'POST':
		form = TransactionForm(request.POST)
		if form.is_valid():
			form.save()
		else:
			error = "Неверно заполненная форма"

	form = TransactionForm()

	transactions = Transaction.objects.filter(date__year=datetime.now().year, date__month=datetime.now().month)
	result_expenses = 0

	for transaction in transactions:
		result_expenses += transaction.expenses

	data = {
		'categories': Category.objects.all(),
		'transactions': transactions,
		'form': form,
		'error': error,
		'result': result_expenses,
	}
	return render(request, 'index.html', data)

def format(request, category_id):
	if not category_id:
		transactions = Transaction.objects.filter(date__year=datetime.now().year, date__month=datetime.now().month)
	else:
		transactions = Transaction.objects.filter(category__id=category_id, date__year=datetime.now().year, date__month=datetime.now().month)
	
	result_expenses = 0

	for transaction in transactions:
		result_expenses += transaction.expenses

	data = {
		'categories': Category.objects.all(),
		'transactions': transactions,
		'result': result_expenses,
	}
	return render(request, 'index.html', data)

def show_transaction_info(request, category_id):
	pass


def show_sopping_list(request):
	return render(request, 'shopping_list.html')

def show_categories(request):
	error = ''
	if request.method == 'POST':
		form = CategoriesForm(request.POST)
		if form.is_valid():
			form.save()
		else:
			error = "Неверно заполненная форма"

	form = CategoriesForm()

	categories = Category.objects.all()

	data = {
		'categories': categories,
		'form': form,
		'error': error,
	}

	return render(request, 'categories.html', data)


class TransactionView(ModelViewSet):
	queryset = Transaction.objects.all()
	serializer_class = OrderSerializer


class Update(UpdateView):
	model = Transaction	
	template_name = 'update_transaction.html'

	fields = ['date', 'name', 'category', 'expenses']


# def delete(request, transaction_id):
# 	transaction = get_object_or_404(Transaction, id=transaction_id)
# 	transaction.delete()
# 	return redirect('/')

'''Нужно привести все в порядок'''