from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serializers import OrderSerializer
from .models import Transaction


def start_page(request):
	return render(request, 'index.html')

class TransactionView(ModelViewSet):
	queryset = Transaction.objects.all()
	serializer_class = OrderSerializer