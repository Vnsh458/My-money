from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from rest_framework.viewsets import ModelViewSet
from django.views.generic import ListView, UpdateView, DeleteView
from .serializers import OrderSerializer
from datetime import datetime

from .models import Transaction, Category
from .forms import CategoriesForm
from .utils import DataMixin, AddTransaction, AddCategories


class TransactionHome(DataMixin, ListView, AddTransaction):
	model = Transaction
	template_name = 'index.html'
	context_object_name = 'transactions'

	def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
		context = super().get_context_data(**kwargs)
		c_def = self.get_user_context()
		return dict(list(context.items()) + list(c_def.items()))
	
	def get_queryset(self, category_id=None):
		return Transaction.objects.filter(date__year=datetime.now().year, date__month=datetime.now().month)
	
	def get_result_expenses(self) -> int:
		result_expenses = 0

		for transaction in self.get_queryset():
			result_expenses += transaction.expenses

		return result_expenses


class TransactionCategory(TransactionHome):
	def get_queryset(self) -> QuerySet[Any]:
		return Transaction.objects.filter(category__id=self.kwargs['category_id'], date__year=datetime.now().year, date__month=datetime.now().month)


def show_sopping_list(request):
	return render(request, 'shopping_list.html')


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


class DeleteTransaction(DeleteView):
	model = Transaction
	success_url = reverse_lazy('transaction:start_page')


class DeleteCategories(DeleteView):
	model = Category
	success_url = reverse_lazy('transaction:categories')
	

class UpdateTransaction(UpdateView):
	model = Transaction	
	template_name = 'update_transaction.html'

	fields = ['date', 'name', 'category', 'expenses']


# class UpdateCategories(UpdateView):
# 	model = Category	
# 	template_name = 'update_category.html'

# 	fields = ['name']


def show_autorisation_page(request):
	return render(request, 'autorisation.html')