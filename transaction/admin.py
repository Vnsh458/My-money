from django.contrib import admin

from .models import Category, Transaction, IncomeCategory, Income


admin.site.register(Category)
admin.site.register(Transaction)
admin.site.register(IncomeCategory)
admin.site.register(Income)