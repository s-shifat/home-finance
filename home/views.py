from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Sum
from datetime import datetime as dt
from .models import Bill, BillTransaction
from .forms import BillTransactionForm
from pytz import timezone
from django import forms

# Create your views here.
@login_required(login_url='login')
def home_page(request):
    today = dt.now(timezone('Asia/Dhaka'))
    time_yes = f"{today.day}/{today.month}/{today.year} at {today.hour}:{today.minute}"
    bills = Bill.objects.filter(due_date__month=today.month, due_date__year=today.year).order_by('-amount','due_date')
    context = {'today': today, 'bills': bills}
    return render(request, 'home/dashboard.html', context=context)


@login_required(login_url='login')
def bill_update_page(request, pk):
    bill = Bill.objects.get(id=pk)
    initial = {'bill': bill, 'paid_by': request.user}
    form = BillTransactionForm(request.POST or None, initial=initial)
    if form.is_valid():
        form = form.save(commit=False)
        paid_amount = form.paid_amount
        if paid_amount + bill.paid_amount > bill.amount:
            form = BillTransactionForm()
            return render(request, 'home/error_page.html', context={'paid_bill': paid_amount, 'required_bill': bill.amount-bill.paid_amount, 'id': pk})
        elif paid_amount + bill.paid_amount == bill.amount:
            bill.status = True
            bill.clearance_date = dt.now()
        form.bill = bill
        form.paid_by = request.user
        form.save()
        # update the Bill data also
        paid_amount = BillTransaction.objects.filter(bill=bill).aggregate(Sum('paid_amount'))['paid_amount__sum']
        bill_payers = BillTransaction.objects.filter(bill=bill).values_list('paid_by__username', flat=True)
        bill.paid_amount = paid_amount
        bill.payers = ', '.join(list(bill_payers)) or request.user.username
        bill.save()
        return redirect('dashboard')

    context = {
        'bill': bill,
        'form': form
    }
    return render(request, 'home/bill_update_page.html', context=context)


