from django.urls import path
from . import views


app_name = 'transaction'


urlpatterns = [
	path('', views.start_page, name='start_page'),
	path('delete/<int:transaction_id>/', views.delete, name='delete'),
	path('update/<int:transaction_id>/', views.update, name='update'),
]