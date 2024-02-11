from django.urls import path
from . import views


app_name = 'transaction'


urlpatterns = [
	path('', views.start_page, name='start_page'),
	path('delete/<int:transaction_id>/', views.delete, name='delete'),
	path('<int:pk>/update', views.Update.as_view(), name='update'),
]