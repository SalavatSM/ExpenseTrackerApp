from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm
from django.db.models import Sum
from datetime import date


def index(request):
    expenses = Expense.objects.all()
    total_expenses = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    return render(request, 'tracker/index.html', {'expenses': expenses, 'total_expenses': total_expenses})


def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ExpenseForm()
    return render(request, 'tracker/add_expense.html', {'form': form})