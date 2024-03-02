from django.shortcuts import render,redirect
from Core.models import Place
from Accounts.models import Entry,Entry_Categories
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from U_Auth.models import User
from Core.models import Agents,Collage,Student
from django.contrib import messages
from datetime import datetime
from django.db.models import Sum
now = datetime.now()

# Create your views here.

@login_required
def accounts(request):
    transactions = Entry.objects.all()
    students = Student.objects.all()
    staffs = User.objects.filter(is_telecaller=True)

    expense_total = transactions.filter(Category__Type='Expense').aggregate(Sum('Amount'))['Amount__sum'] or 0
    income_total = transactions.filter(Category__Type='Income').aggregate(Sum('Amount'))['Amount__sum'] or 0

    balance = int(income_total) - int(expense_total)
    
    context = {
        'page' : 'accounts',
        'transactions' : transactions,
        'students' : students,
        'expense_total' : expense_total,
        'income_total' : income_total,
        'balance' : balance,
        'staffs' : staffs
    }
    return render(request,'Dashboard/Accounts/accounts.html',context)


@csrf_exempt
def get_entry_categories(request):
    if request.method == 'POST':
        type = request.POST.get('type')

        categories = Entry_Categories.objects.filter(Type=type)

        categories_list = list(categories.values())

    return JsonResponse({'categories':categories_list})

@login_required
def entry_add(request):
    if request.method == 'POST':
        entry_category_cid = request.POST.get('entry_category')
        entry_category = Entry_Categories.objects.get(CATID=entry_category_cid)

        student_id = request.POST.get('student')
        
        if student_id:
            student = Student.objects.get(id=student_id)
        else:
            student = None

        title = request.POST.get('title')
        amount = request.POST.get('amount')

        try:
            Entry.objects.create(Title=title,Category=entry_category,Date=now,Amount=amount,Student=student)
            messages.success(request,'Entry added successfully ... !')
        except Exception as exception:
            messages.warning(request,exception)
            
    return redirect('accounts')