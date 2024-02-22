from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from rest_framework.viewsets import ModelViewSet
from django.views.generic import ListView, UpdateView, DeleteView
from .serializers import OrderSerializer
from datetime import datetime

from .models import Transaction, Category
from .forms import TransactionForm, CategoriesForm


class Update(UpdateView):
	model = Transaction	
	template_name = 'update_transaction.html'

	fields = ['date', 'name', 'category', 'expenses']


class AddTransaction(View):
	def get(self, request):
		form = TransactionForm()
		return render(request, 'index.html', {'form': form})

	def post(self, request):
		form = TransactionForm(request.POST, request.FILES)
		if form.is_valid():
			form.save() 
			return redirect('/')


class TransactionCategory(ListView):
	model = Transaction
	template_name = 'index.html'
	context_object_name = 'transactions'

	def get_result_expenses(self) -> int:
		result_expenses = 0

		for transaction in self.get_queryset():
			result_expenses += transaction.expenses

		return result_expenses
	
	def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
		context = super().get_context_data(**kwargs)
		context['categories'] = Category.objects.all()
		context['result'] = self.get_result_expenses()
		context['form'] = TransactionForm()

		return context
	
	def get_queryset(self) -> QuerySet[Any]:
		return Transaction.objects.filter(category__id=self.kwargs['category_id'], date__year=datetime.now().year, date__month=datetime.now().month)


class TransactionHome(ListView, AddTransaction):
	model = Transaction
	template_name = 'index.html'
	context_object_name = 'transactions'

	def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
		context = super().get_context_data(**kwargs)
		context['categories'] = Category.objects.all()
		context['result'] = self.get_result_expenses()
		context['form'] = TransactionForm()
		return context
	
	def get_queryset(self, category_id=None):
		return Transaction.objects.filter(date__year=datetime.now().year, date__month=datetime.now().month)
	
	def get_result_expenses(self) -> int:
		result_expenses = 0

		for transaction in self.get_queryset():
			result_expenses += transaction.expenses

		return result_expenses


def show_sopping_list(request):
	return render(request, 'shopping_list.html')


class AddCategories(View):
	def get(self, request):
		form = CategoriesForm()
		return render(request, 'categories.html', {'form': form})

	def post(self, request):
		form = CategoriesForm(request.POST, request.FILES)
		if form.is_valid():
			form.save() 
			return redirect('/categories')



class ShowCategories(ListView, AddCategories):
	model = Category
	template_name = 'categories.html'
	context_object_name = 'categories'

	def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
		context = super().get_context_data(**kwargs)
		context['form'] = CategoriesForm
		return context


class TransactionView(ModelViewSet):
	queryset = Transaction.objects.all()
	serializer_class = OrderSerializer


class Delete(DeleteView):
	model = Transaction
	success_url = reverse_lazy('transaction:start_page')

'''Нужно привести все в порядок'''

def show_autorisation_page(request):
	return render(request, 'autorisation.html')