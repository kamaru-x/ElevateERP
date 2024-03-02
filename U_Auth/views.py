from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from U_Auth.models import User

# Create your views here.

#------------------------------------------------- SIGN IN ---------------------------------------------------#

def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request,'incorrect username or password')
            return redirect('.')
    return render(request,'Dashboard/Auth/sign-in.html')

#----------------------------------------------CHANGE PASSWORD -----------------------------------------------#

@login_required
def changepassword(request):
    user = request.user
    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            messages.warning(request,'password does not matching')
            return redirect('/change-password/')
        else:
            user.set_password(password1)
            user.save()
            return redirect('dashboard')
    return render(request,'Dashboard/Auth/change-password.html')

#------------------------------------------------- SIGN OUT --------------------------------------------------#

@login_required
def signout(request):
    logout(request)
    return redirect('sign-in')

#------------------------------------------------- STAFFS --------------------------------------------------#

@login_required
def staffs(request):
    staffs = User.objects.filter(is_telecaller=True)
    context = {
        'page' : 'masters',
        'staffs' : staffs
    }
    return render(request,'Dashboard/Staffs/staffs.html',context)

#------------------------------------------------- ADD STAFF --------------------------------------------------#

@login_required
def add_staff(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')

        try:
            user = User.objects.create(username=email,first_name=name,Image=image,email=email,Mobile=mobile,is_telecaller=True)
            user.set_password('123456')
            user.save()
            messages.success(request,'Added new staff successfully ... !')
            return redirect('staffs')
        
        except Exception as exception:
            messages.warning(request,exception)
            return redirect('add-staff')

    return render(request,'Dashboard/Staffs/staff-add.html')

#------------------------------------------------- EDIT STAFF --------------------------------------------------#

@login_required
def edit_staff(request,username):
    user = User.objects.get(username=username)
    if request.method == 'POST':

        if len(request.FILES) > 0 :
            user.Image = request.FILES.get('image')

        user.first_name = request.POST.get('name')
        user.email = request.POST.get('email')
        user.Mobile = request.POST.get('mobile')
        user.username = request.POST.get('email')

        try:
            user.save()
            messages.success(request,'Staff details edited successfully ... !')
            return redirect('staffs')
        except Exception as exception:
            messages.success(request,exception)
            return redirect('edit-staff',staff_id=user.username)
        
    context = {
        'page' : 'masters',
        'staff' : user
    }

    return render(request,'Dashboard/Staffs/staff-edit.html',context)