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
    transactions = Entry.objects.all().order_by('-Date').order_by('-id')
    students = Student.objects.all()
    staffs = User.objects.filter(is_telecaller=True)
    collages = Collage.objects.all()
    main_agents = Agents.objects.filter(Rank='Main')
    sub_agents = Agents.objects.filter(Rank='Sub')

    expense_total = transactions.filter(Category__Type='Expense').aggregate(Sum('Amount'))['Amount__sum'] or 0
    income_total = transactions.filter(Category__Type='Income').aggregate(Sum('Amount'))['Amount__sum'] or 0
    balance = int(income_total) - int(expense_total)

    collage_transactions = transactions.exclude(Collage=None)
    agent_transactions = transactions.exclude(Agents=None)
    student_transactions = transactions.exclude(Student=None)
    staff_transactions = transactions.exclude(Staff=None)
    other_transactions = transactions.filter(Staff=None,Collage=None,Agents=None,Student=None)
    
    context = {
        'page' : 'accounts',
        'transactions' : transactions,
        'students' : students,
        'expense_total' : expense_total,
        'income_total' : income_total,
        'balance' : balance,
        'staffs' : staffs,
        'collages' : collages,
        'main_agents' : main_agents,
        'sub_agents' : sub_agents,
        'collage_transactions' : collage_transactions,
        'agent_transactions' : agent_transactions,
        'student_transactions' : student_transactions,
        'staff_transactions' : staff_transactions,
        'other_transactions' : other_transactions
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
        category_cid = request.POST.get('entry_category')
        category = Entry_Categories.objects.get(id=category_cid)

        student_id = request.POST.get('student')
        staff_id = request.POST.get('staff')
        collage_id = request.POST.get('collage')
        main_agent = request.POST.get('main_agent')
        sub_agent = request.POST.get('sub_agent')
        
        if student_id:
            student = Student.objects.get(id=student_id)
        else:
            student = None

        if staff_id:
            staff = User.objects.get(id=staff_id)
        else:
            staff = None

        if collage_id:
            collage = Collage.objects.get(id=collage_id)
        else:
            collage = None

        if main_agent:
            agent = Agents.objects.get(id=main_agent)
        elif sub_agent:
            agent = Agents.objects.get(id=sub_agent)
        else:
            agent = None

        title = request.POST.get('title')
        amount = request.POST.get('amount')

        try:
            Entry.objects.create(
                Title=title,Category=category,Date=now,Amount=amount,Student=student,Staff=staff,
                Collage=collage,Agents=agent
            )
            messages.success(request,'Entry added successfully ... !')
        except Exception as exception:
            messages.warning(request,exception)
            
    return redirect('accounts')

@csrf_exempt
def get_fot(request):
    if request.method == 'POST':
        cat_id = request.POST.get('id')
        category = Entry_Categories.objects.get(id=cat_id)
    return JsonResponse({'fot':category.FOT})

@login_required
def delete_transaction(request):
    if request.method == 'POST':
        transaction_id = request.POST.get('transaction_id')
        trasaction = Entry.objects.get(id=transaction_id)
        trasaction.delete()
        messages.warning(request,'transaction entry deleted successfully ... !')
    return redirect('accounts')