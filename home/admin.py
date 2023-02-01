from django.contrib import admin
from .models import Bill, BillTransaction

# Register your models here.
admin.site.register(Bill)
admin.site.register(BillTransaction)
