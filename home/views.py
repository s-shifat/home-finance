from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Sum
from datetime import datetime as dt
from .models import Bill, BillTransaction
from .forms import BillTransactionForm
from pytz import timezone
from django import forms
from .bills_updater import get_bills


# Create your views here.
@login_required(login_url='login')
def home_page(request):
    today = dt.now(timezone('Asia/Dhaka'))
    bill_model = get_bills(model=Bill)
    bills = bill_model.objects.filter(due_date__month=today.month, due_date__year=today.year).order_by('-amount','due_date')
    context = {'today': today, 'bills': bills}
    return render(request, 'home/dashboard.html', context=context)


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

#@login_required(login_url='login')
#def bill_update_page(request, pk):
#    bill = Bill.objects.get(id=pk)
#    form = BillTransactionForm(request.POST or None)
#    if form.is_valid():
#        form = form.save(commit=False)
#        paid_amount = form.paid_amount
#        if paid_amount + bill.paid_amount > bill.amount:
#            form = BillTransactionForm()
#            return render(request, 'home/error_page.html', context={'paid_bill': paid_amount, 'required_bill': bill.amount-bill.paid_amount, 'id': pk})
#        elif paid_amount + bill.paid_amount == bill.amount:
#            bill.status = True
#            bill.clearance_date = dt.now()
#            bill.save()
#        form.bill = bill
#        form.paid_by = request.user
#        form.save()
#        # update the Bill data also
#        paid_amount = BillTransaction.objects.filter(bill=bill).aggregate(Sum('paid_amount'))['paid_amount__sum']
#        bill_payers = BillTransaction.objects.filter(bill=bill).values_list('paid_by__username', flat=True)
#        bill.paid_amount = paid_amount
#        bill.payers = ', '.join(list(bill_payers)) or request.user.username
#        bill.save()
#        return redirect('dashboard')
#
#    context = {
#        'bill': bill,
#        'form': form
#    }
#    return render(request, 'home/bill_update_page.html', context=context)
#

