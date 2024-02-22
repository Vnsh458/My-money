from django.urls import path
from . import views


app_name = 'transaction'


urlpatterns = [
	path('', views.TransactionHome.as_view(), name='start_page'),
	path('transaction/<int:pk>/delete/', views.Delete.as_view(), name='delete'),
	path('<int:pk>/update', views.Update.as_view(), name='update'),
	path('shopping_list/', views.show_sopping_list, name='shopping_list'),
	path('categories/', views.ShowCategories.as_view(), name='categories'),
	path('<int:category_id>', views.TransactionCategory.as_view(), name='formatting'),
	path('autorisation/', views.show_autorisation_page, name='autorisation')
]