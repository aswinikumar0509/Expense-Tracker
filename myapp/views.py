from django.shortcuts import render
from .forms import ExpenseForm
from .models import Expense

# Create your views here.

def index(request):

    if request.method=="POST":
        expense=ExpenseForm(request.POST)
        if expense.is_valid():
            expense.save()

    expenses = Expense.objects.all()



    expense_form = ExpenseForm()


    return render(request,'myapp/index.html',{'expense_form':expense_form,'expenses':expenses})
