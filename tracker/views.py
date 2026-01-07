from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense

def add_expense(request):
    if request.method == "POST":
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        date = request.POST.get("date")

        Expense.objects.create(
            amount=amount,
            description=description,
            date=date
        )

        return redirect("expense_list")

    return render(request, "add_expense.html")


def expense_list(request):
    expenses = Expense.objects.all().order_by('-date')  # newest first
    return render(request, "view.html", {"expenses": expenses})

def delete_expense(request, id):
    expense = get_object_or_404(Expense, id=id)
    expense.delete()
    return redirect("expense_list")