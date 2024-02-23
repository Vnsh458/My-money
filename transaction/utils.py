from django.shortcuts import redirect, render
from django.views import View

from .models import *
from .forms import *

class DataMixin:
	def get_user_context(self, **kwargs):
		context = kwargs
		context['categories'] = Category.objects.all()
		context['result'] = self.get_result_expenses()
		context['form'] = TransactionForm()

		return context
	

class AddTransaction(View):
	def get(self, request):
		form = TransactionForm()
		return render(request, 'index.html', {'form': form})

	def post(self, request):
		form = TransactionForm(request.POST, request.FILES)
		if form.is_valid():
			form.save() 
			return redirect('/')
		

class AddCategories(View):
	def get(self, request):
		form = CategoriesForm()
		return render(request, 'categories.html', {'form': form})

	def post(self, request):
		form = CategoriesForm(request.POST, request.FILES)
		if form.is_valid():
			form.save() 
			return redirect('/categories')