from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='dashboard'),
    path('bill-update/<int:pk>', views.bill_update_page, name='bill_update_page'),
]
