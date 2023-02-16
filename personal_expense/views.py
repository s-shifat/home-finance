from django.shortcuts import render, redirect
from .models import Expense, Category
from .forms import ExpenseForm, CategoryForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def expense_page(request):
    user = request.user
    expenses = Expense.objects.filter(paid_by=user).order_by('-date')
    expense_form = ExpenseForm(request.POST or None)
    category_form = CategoryForm(request.POST or None)
    if expense_form.is_valid():
        expense_model = expense_form.save(commit=False)
        expense_model.paid_by = user
        expense_model.save()
        expense_form = ExpenseForm()
        return redirect('.')

    if category_form.is_valid():
        category_form.save()
        category_form = CategoryForm()
        return redirect('.')

    
    context = {
            'expenses': expenses,
            'expense_form': expense_form,
            'category_form': category_form,
    }
    return render(request, 'personal_expense/expense_page.html', context=context)
