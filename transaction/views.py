from django.shortcuts import redirect, render
from rest_framework.viewsets import ModelViewSet
from django.views.generic import DeleteView

from .serializers import OrderSerializer
from .models import Transaction
from .forms import TransactionForm


def start_page(request):
	error = ''
	if request.method == 'POST':
		form = TransactionForm(request.POST)
		if form.is_valid():
			form.save()
		else:
			error = "Неверно заполненная форма"

	form = TransactionForm()

	data = {
		'transactions': Transaction.objects.all(),
		'form': form,
		'error': error,
	}
	return render(request, 'index.html', data)


def show_sopping_list(request):
	return(request, 'shopping_list.html')


class TransactionView(ModelViewSet):
	queryset = Transaction.objects.all()
	serializer_class = OrderSerializer


'''class NewDeleteView(DeleteView):
	model = Transaction
	success_url = 'index.html'
	template_name = 'index.html'''


def delete(request, transaction_id):
	transaction = Transaction.objects.get(id=transaction_id)
	transaction.delete()
	return redirect('/')

def update(request, transaction_id):
	transaction = Transaction.objects.get(id=transaction_id)
	transaction.delete()
	return redirect('start_page')