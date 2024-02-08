from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

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
		'form': form,
		'error': error
	}
	return render(request, 'index.html', data)

class TransactionView(ModelViewSet):
	queryset = Transaction.objects.all()
	serializer_class = OrderSerializer