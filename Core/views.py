from django.shortcuts import render,redirect
from Core.pre_fun import setip,resize_image,random_string
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.

#----------------------------------- DASHBOARD -----------------------------------#

@login_required
def dashboard(request):
    return render(request,'Dashboard/Core/dashboard.html')