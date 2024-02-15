from django.urls import path
from . import views


app_name = 'transaction'


urlpatterns = [
	path('', views.start_page, name='start_page'),
	path('<int:transaction_id>', views.delete, name='delete'),
	path('<int:pk>/update', views.Update.as_view(), name='update'),
	path('shopping_list/', views.show_sopping_list, name='shopping_list'),
	path('categories/', views.show_categories, name='categories'),
	path('<int:category_id>', views.format, name='formatting')
]