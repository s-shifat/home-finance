from django.urls import path
from . import views

urlpatterns = [
    path('', views.expense_page, name='personal-expense'),
]
