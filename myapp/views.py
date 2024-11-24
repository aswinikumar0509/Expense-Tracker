from django.shortcuts import render
from .forms import ExpenseForm

# Create your views here.

def index(request):

    expense_form = ExpenseForm()


    return render(request,'myapp/index.html',{'expense_form':expense_form})
