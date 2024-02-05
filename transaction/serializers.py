from rest_framework.serializers import ModelSerializer

from .models import Transaction


class OrderSerializer(ModelSerializer):
	class Meta:
		model = Transaction
		fields = [
			'date',
			'name',
			'category',
			'expenses',
		]