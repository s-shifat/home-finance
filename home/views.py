from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Sum
from datetime import datetime as dt
from .models import Bill, BillTransaction
from .forms import BillTransactionForm, BillForm
from pytz import timezone
from django import forms
from .bills_updater import get_bills
import calendar



# Create your views here.
@login_required(login_url='login')
def home_page(request):
    today = dt.now(timezone('Asia/Dhaka'))
    month = calendar.month_name[today.month]
    bill_model = get_bills(model=Bill)
    bills = bill_model.objects.filter(due_date__month=today.month, due_date__year=today.year).order_by('status', '-amount','due_date')

    context = {'today': today, 'month': month, 'bills': bills}
    return render(request, 'home/dashboard.html', context=context)

@login_required(login_url='login')
def bill_adjust_page(request, pk):
    bill = Bill.objects.get(pk=pk)
    form = BillForm(request.POST or None, instance=bill)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    context = {'bill': bill, 'form': form}
    return render(request, 'home/bill_adjust_page.html', context=context)


@login_required(login_url='login')
def bill_update_page(request, pk):
    bill = Bill.objects.get(id=pk)
    bill_ts = BillTransaction(paid_by=request.user, bill=bill)
    form = BillTransactionForm(request.POST or None, instance=bill_ts)
    if form.is_valid():
        try:
            form = form.save()
        except ValidationError as e:
#            cleaned_data = form.cleaned_data()
            required_amount = bill.paid_amount - bill.amount
            return render(request, 'home/error_page.html', context={'paid_bill': request.POST['paid_amount'], 'required_bill':required_amount, 'id': pk, 'error': e})
        return redirect('dashboard')

    context = {
        'bill': bill,
        'form': form
    }
    return render(request, 'home/bill_update_page.html', context=context)
