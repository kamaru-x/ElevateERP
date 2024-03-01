from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from Core.models import Place,Agents,Course,Course_Addon,Collage,Student
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from Accounts.models import Entry,Entry_Categories
from datetime import datetime

now = datetime.now()

# Create your views here.

#----------------------------------- DASHBOARD -----------------------------------#

@login_required
def dashboard(request):
    places = Place.objects.all()
    collages = Collage.objects.all()
    courses = Course.objects.all()
    students = Student.objects.all()
    
    context = {
        'page' : 'dashboard',
        'places' : places,
        'collages' : collages,
        'courses' : courses,
        'students' : students
    }
    return render(request,'Dashboard/Core/dashboard.html',context)

#----------------------------------- PLACES -----------------------------------#

@login_required
def places(request):
    places = Place.objects.all()
    context = {
        'page' : 'masters',
        'places' : places
    }
    return render(request,'Dashboard/Core/place-list.html',context)

#----------------------------------- ADD PLACE -----------------------------------#

@login_required
def add_place(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        try:
            Place.objects.create(Name=name)
            messages.success(request,'New place added Successfully ... !')
        
        except Exception as exception:
            messages.warning(request,exception)

    return redirect('places')

#----------------------------------- DELETE PLACE -----------------------------------#

@login_required
def delete_place(request):
    if request.method == 'POST':
        place_id = request.POST.get('place_id')
        place = Place.objects.get(id=place_id)

        try:
            place.delete()
            messages.success(request,'Place deleated successfully ... !')
        except Exception as exception:
            messages.warning(request,exception)

    return redirect('places')

#----------------------------------- PLACES -----------------------------------#

@login_required
def agents(request,rank):
    agents = Agents.objects.filter(Rank=rank).order_by('-id')
    context = {
        'page' : 'agents',
        'agents' : agents,
        'rank' : rank
    }
    return render(request,'Dashboard/Core/Agent/agents-list.html',context)

#----------------------------------- ADD AGENT -----------------------------------#

@login_required
def add_agent(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        rank = request.POST.get('rank')
        # place = request.POST.get('place')

        try:
            Agents.objects.create(Name=name,Mobile=mobile,Email=email,Rank=rank)
            messages.success(request,'Agent added successfully ... !')
            return redirect('agents',rank=rank)
        
        except Exception as exception:
            messages.warning(request,exception)
            return redirect('add-agent')
        
    context = {
        'page' : 'agents'
    }

    return render(request,'Dashboard/Core/Agent/agent-add.html',context)

#----------------------------------- EDIT AGENT -----------------------------------#

@login_required
def edit_agent(request,agent_id):
    agent = Agents.objects.get(id=agent_id)
    if request.method == 'POST':
        agent.Name = request.POST.get('name')
        agent.Mobile = request.POST.get('mobile')
        agent.Email = request.POST.get('email')
        agent.Rank = request.POST.get('rank')

        try:
            agent.save()
            messages.success(request,'Agent detals edited successfully ... !')
            return redirect('agents',rank=agent.Rank)
        
        except Exception as exception:
            messages.warning(request,exception)
            return redirect('edit-agent',agent_id=agent.id)
        
    context = {
        'page' : 'agents',
        'agent' : agent
    }

    return render(request,'Dashboard/Core/Agent/agent-edit.html',context)

#----------------------------------- DELETE AGENT -----------------------------------#

@login_required
def delete_agent(request):
    if request.method == 'POST':
        agent_id = request.POST.get('agent_id')
        agent = Agents.objects.get(id=agent_id)

        try:
            agent.delete()
            messages.success(request,'Agent deleated successfully ... !')
        except Exception as exception:
            messages.warning(request,exception)

    return redirect('agents')

#----------------------------------- COURSES -----------------------------------#

@login_required
def courses(request):
    courses = Course.objects.all().order_by('-id')
    context = {
        'page' : 'courses',
        'courses' : courses
    }
    return render(request,'Dashboard/Core/courses.html',context)

#----------------------------------- ADD COURSE -----------------------------------#

@login_required
def add_course(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        try:
            Course.objects.create(Name=name)
            messages.success(request,'New Course added Successfully ... !')
        
        except Exception as exception:
            messages.warning(request,exception)

    return redirect('courses')

#----------------------------------- DELETE COURSE -----------------------------------#

@login_required
def delete_course(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        course = Course.objects.get(id=course_id)

        try:
            course.delete()
            messages.success(request,'Course deleated successfully ... !')
        except Exception as exception:
            messages.warning(request,exception)

    return redirect('courses')

#----------------------------------- COURSE ADDONS -----------------------------------#

@login_required
def course_addons(request,course_id):
    course = Course.objects.get(id=course_id)
    addons = Course_Addon.objects.filter(Course=course)
    context = {
        'page' : 'courses',
        'course' : course,
        'addons' : addons
    }
    return render(request,'Dashboard/Core/course-details.html',context)

#----------------------------------- ADD ADDON -----------------------------------#

@login_required
def add_addon(request):
    if request.method == 'POST':
        course_id = request.POST.get('course')
        course = Course.objects.get(id=course_id)
        title = request.POST.get('name')

        try:
            Course_Addon.objects.create(Course=course,Title=title)
            messages.success(request,'New addon created ... !')
            return redirect('course-addons',course_id=course.id)

        except Exception as exception:
            messages.warning(request,exception)
            return redirect('course-addons',course_id=course.id)
        

#----------------------------------- DELETE ADDON -----------------------------------#
        
@login_required
def delete_addon(request):
    if request.method == 'POST':
        addon_id = request.POST.get('addon_id')
        addon = Course_Addon.objects.get(id=addon_id)
        c_id = addon.Course.id

        try:
            addon.delete()
            messages.success(request,'Addon deleated successfully ... !')
        except Exception as exception:
            messages.warning(request,exception)

    return redirect('course-addons',course_id=c_id)

#----------------------------------- COLLAGES -----------------------------------#

@login_required
def collages(request):
    collages = Collage.objects.all()
    context = {
        'page' : 'collage',
        'collages' : collages
    }
    return render(request,'Dashboard/Collages/collages.html',context)

#----------------------------------- ADD COLLAGE -----------------------------------#

@login_required
def add_collage(request):
    places = Place.objects.all()
    agents = Agents.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')

        place_id = request.POST.get('place')
        place = Place.objects.get(id=place_id)

        agent_id = request.POST.get('agent')
        agent = Agents.objects.get(id=agent_id)

        try:
            Collage.objects.create(Name=name,Mobile=mobile,Email=email,Place=place,Agent=agent)
            messages.success(request,'Collage added successfully ... !')
            return redirect('collages')
        
        except Exception as exception:
            messages.warning(request,exception)
            return redirect('add-collage')
        
    context = {
        'page' : 'collage',
        'places' : places,
        'agents' : agents
    }
    return render(request,'Dashboard/Collages/collage-add.html',context)

#----------------------------------- EDIT COLLAGE -----------------------------------#

@login_required
def edit_collage(request,collage_id):
    collage = Collage.objects.get(id=collage_id)
    places = Place.objects.all()
    agents = Agents.objects.all()

    if request.method == 'POST':
        collage.Name = request.POST.get('name')
        collage.Mobile = request.POST.get('mobile')
        collage.Email = request.POST.get('email')

        place_id = request.POST.get('place')
        collage.Place = Place.objects.get(id=place_id)

        agent_id = request.POST.get('agent')
        collage.Agent = Agents.objects.get(id=agent_id)

        try:
            collage.save()
            messages.success(request,'Collage details edited successfully ... !')
            return redirect('collages')
        except Exception as exception:
            messages.warning(request,exception)
            return redirect('edit-collage' , collage_id=collage.id)

    context = {
        'page' : 'collage',
        'collage' : collage,
        'places' : places,
        'agents' : agents
    }
    return render(request,'Dashboard/Collages/collage-edit.html',context)

#----------------------------------- VIEW COLLAGE -----------------------------------#

@login_required
def view_collage(request,collage_id):
    collage = Collage.objects.get(id=collage_id)
    context = {
        'page' : 'collage',
        'collage' : collage
    }
    return render(request,'Dashboard/Collages/collage-view.html',context)

#----------------------------------- DELETE COLLAGE -----------------------------------#

@login_required
def delete_collage(request):
    if request.method == 'POST':
        collage_id = request.POST.get('collage_id')
        collage = Collage.objects.get(id=collage_id)

        try:
            collage.delete()
            messages.success(request,'Collage deleated successfully ... !')
        except Exception as exception:
            messages.warning(request,exception)

    return redirect('collages')

#----------------------------------- STUDENTS -----------------------------------#

@login_required
def students(request):
    students = Student.objects.all().order_by('-id')
    context = {
        'page' : 'students',
        'students' : students
    }
    return render(request,'Dashboard/Students/students.html',context)

#----------------------------------- ADD STUDENT -----------------------------------#

@login_required
def add_student(request):
    collages = Collage.objects.all().order_by('-id')
    courses = Course.objects.all().order_by('-id')
    agents = Agents.objects.all().order_by('-id')

    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        place = request.POST.get('place')

        collage_id = request.POST.get('collage')
        collage = Collage.objects.get(id=collage_id)

        course_id = request.POST.get('course')
        course = Course.objects.get(id=course_id)

        addon_id = request.POST.get('addon')
        addon = Course_Addon.objects.get(id=addon_id)

        agent_id = request.POST.get('agent')
        agent = Agents.objects.get(id=agent_id)

        fees = request.POST.get('fees')
        donation = request.POST.get('donation')
        discount = request.POST.get('discount')
        total = request.POST.get('total')
        first_payment = request.POST.get('first_payment')
        service = request.POST.get('service')
        collage_payment = request.POST.get('collage_payment')

        try:
            student = Student.objects.create(
                Name=name,Mobile=mobile,Email=email,Place=place,Collage=collage,Course=course,
                Addon=addon,Agent=agent,Fees=fees,Donation=donation,Discount=discount,Total=total,
                First_Payment=first_payment,Service=service,Collage_Payment=collage_payment
            )
            
            title = f'1st Payment from {name}'
            category = Entry_Categories.objects.get(CATID='SFPTOES')

            Entry.objects.create(Title=title,Category=category,Date=now,Amount=first_payment,Student=student)

            messages.success(request,'New student addedd successfully ... !')
            return redirect('students')
        
        except Exception as exception:
            messages.warning(request,exception)
            return redirect('add-student')

    context = {
        'page' : 'students',
        'collages' : collages,
        'courses' : courses,
        'agents' : agents
    } 
    return render(request,'Dashboard/Students/student-add.html',context)

#----------------------------------- GET ADDONS -----------------------------------#

@csrf_exempt
def get_addons(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        course = Course.objects.get(id=course_id)

        addons = Course_Addon.objects.filter(Course=course)
        addon_list = list(addons.values())

        return JsonResponse({'status':'success','addons':addon_list})

#----------------------------------- EDIT STUDENT -----------------------------------#

@login_required
def edit_student(request,student_id):
    student = Student.objects.get(id=student_id)
    collages = Collage.objects.all().order_by('-id')
    courses = Course.objects.all().order_by('-id')
    agents = Agents.objects.all().order_by('-id')
    addons = Course_Addon.objects.filter(Course=student.Course)

    if request.method == 'POST':
        student.Name = request.POST.get('name')
        student.Mobile = request.POST.get('mobile')
        student.Email = request.POST.get('email')
        student.Place = request.POST.get('place')

        collage_id = request.POST.get('collage')
        student.Collage = Collage.objects.get(id=collage_id)

        course_id = request.POST.get('course')
        student.Course = Course.objects.get(id=course_id)

        addon_id = request.POST.get('addon')
        student.Addon = Course_Addon.objects.get(id=addon_id)

        agent_id = request.POST.get('agent')
        student.Agent = Agents.objects.get(id=agent_id)

        student.Fees = request.POST.get('fees')
        student.Donation = request.POST.get('donation')
        student.Discount = request.POST.get('discount')
        student.Total = request.POST.get('total')
        student.First_Payment = request.POST.get('first_payment')
        student.Service = request.POST.get('service')
        student.Collage_Payment = request.POST.get('collage_payment')

        try:
            student.save()
            messages.success(request,'Student details edited successfully ... !')
            return redirect('students')
        
        except Exception as exception:
            messages.warning(request,exception)
            return redirect('edit-student',student_id=student.id)

    context = {
        'student' : student,
        'collages' : collages,
        'courses' : courses,
        'addons' : addons,
        'agents' : agents
    }
    return render(request,'Dashboard/Students/student-edit.html',context)

#----------------------------------- EDIT STUDENT -----------------------------------#

@login_required
def student_details(request,student_id):
    student = Student.objects.get(id=student_id)
    context = {
        'student' : student
    }
    return render(request,'Dashboard/Students/student-details.html',context)

#----------------------------------- DELETE STUDENT -----------------------------------#

@login_required
def delete_student(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        student = Student.objects.get(id=student_id)

        try:
            student.delete()
            messages.success(request,'Student deleated successfully ... !')
        except Exception as exception:
            messages.warning(request,exception)
    return redirect('students')