from django.shortcuts import render
from Core.models import Place
from Accounts.models import Entry

# Create your views here.

def accounts(request):
    transactions = Entry.objects.all()
    context = {
        'page' : 'accounts',
        'transactions' : transactions
    }
    return render(request,'Dashboard/Accounts/accounts.html',context)