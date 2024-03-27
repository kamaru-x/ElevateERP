from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from Core.models import Place,Agents,Course,Course_Addon,Collage,Student,News
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from Accounts.models import Entry,Entry_Categories
from datetime import datetime
from django.db.models import Sum
from Frontpage.models import Review,Enquiry

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
    places = Place.objects.all().order_by('-Location','-id')
    context = {
        'page' : 'masters',
        'places' : places
    }
    return render(request,'Dashboard/Core/place-list.html',context)

#----------------------------------- ADD PLACE -----------------------------------#

@login_required
def add_place(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        name = request.POST.get('name')
        image = request.FILES.get('image')

        try:
            Place.objects.create(Location=location,Name=name,Image=image)
            messages.success(request,'New place added Successfully ... !')
        
        except Exception as exception:
            messages.warning(request,exception)

        return redirect('places')
    
    return render(request,'Dashboard/Core/place-add.html')

#----------------------------------- EDIT PLACE -----------------------------------#

@login_required
def edit_place(request,place_id):
    place = Place.objects.get(id=place_id)

    if request.method == 'POST':
        if len(request.FILES) > 0:
            place.Image = request.FILES.get('image')

        place.Location = request.POST.get('location')
        place.Name = request.POST.get('name')

        try:
            place.save()
            messages.success(request,'New place added Successfully ... !')
            return redirect('places')
        
        except Exception as exception:
            messages.warning(request,exception)
            return redirect('edit-place',place_id=place.id)
        
    context = {
        'page' : 'masters',
        'place' : place
    }
    
    return render(request,'Dashboard/Core/place-edit.html',context)

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
        degree = request.POST.get('degree')
        name = request.POST.get('name')

        try:
            Course.objects.create(Degree=degree,Name=name)
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

        place_id = request.POST.get('place')
        place = Place.objects.get(id=place_id)

        try:
            Collage.objects.create(Name=name,Place=place)
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

        place_id = request.POST.get('place')
        collage.Place = Place.objects.get(id=place_id)

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
    students = Student.objects.filter(Collage=collage)
    transactions = Entry.objects.filter(Collage=collage)
    context = {
        'page' : 'collage',
        'collage' : collage,
        'students' : students,
        'transactions' : transactions,
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
    sub_agents = Agents.objects.filter(Rank='Sub').order_by('-id')
    main_agents = Agents.objects.filter(Rank='Main').order_by('-id')

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

        try:
            addon = Course_Addon.objects.get(id=addon_id)
        except:
            addon = None

        sub_agent_id = request.POST.get('sub_agent')
        sub_agent = Agents.objects.get(id=sub_agent_id)

        main_agent_id = request.POST.get('main_agent')
        main_agent = Agents.objects.get(id=main_agent_id)

        fees = request.POST.get('fees') or 0.00
        donation = request.POST.get('donation') or 0.00
        discount = request.POST.get('discount') or 0.00
        total = request.POST.get('total') or 0.00
        first_payment = request.POST.get('first_payment') or 0.00
        service = request.POST.get('service') or 0.00
        collage_payment = request.POST.get('collage_payment') or 0.00
        commission = request.POST.get('commission') or 0.00

        try:
            Student.objects.create(
                Name=name,Mobile=mobile,Email=email,Place=place,Collage=collage,Course=course,
                Addon=addon,Sub_Agent=sub_agent,Main_Agent=main_agent,Fees=fees,Donation=donation,Discount=discount,Total=total,
                First_Payment=first_payment,Service=service,Collage_Payment=collage_payment,Agent_Commission=commission
            )

            messages.success(request,'New student addedd successfully ... !')
            return redirect('students')
        
        except Exception as exception:
            messages.warning(request,exception)
            return redirect('add-student')

    context = {
        'page' : 'students',
        'collages' : collages,
        'courses' : courses,
        'sub_agents' : sub_agents,
        'main_agents' : main_agents
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
    sub_agents = Agents.objects.filter(Rank='Sub').order_by('-id')
    main_agents = Agents.objects.filter(Rank='Main').order_by('-id')
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
        try:
            student.Addon = Course_Addon.objects.get(id=addon_id)
        except:
            pass

        sub_agent_id = request.POST.get('sub_agent')
        student.Sub_Agent = Agents.objects.get(id=sub_agent_id)

        main_agent_id = request.POST.get('main_agent')
        student.Main_Agent = Agents.objects.get(id=main_agent_id)

        student.Fees = request.POST.get('fees') or 0.00
        student.Donation = request.POST.get('donation') or 0.00
        student.Discount = request.POST.get('discount') or 0.00
        student.Total = request.POST.get('total') or 0.00
        student.First_Payment = request.POST.get('first_payment') or 0.00
        student.Service = request.POST.get('service') or 0.00
        student.Collage_Payment = request.POST.get('collage_payment') or 0.00
        student.Agent_Commission = request.POST.get('commission') or 0.00

        try:
            student.save()
            messages.success(request,'Student details edited successfully ... !')
            return redirect('students')
        
        except Exception as exception:
            messages.warning(request,exception)
            return redirect('edit-student',student_id=student.id)

    context = {
        'page' : 'students',
        'student' : student,
        'collages' : collages,
        'courses' : courses,
        'addons' : addons,
        'sub_agents' : sub_agents,
        'main_agents' : main_agents,
    }
    return render(request,'Dashboard/Students/student-edit.html',context)

#----------------------------------- EDIT STUDENT -----------------------------------#

@login_required
def student_details(request,student_id):
    student = Student.objects.get(id=student_id)
    transactions = Entry.objects.filter(Student=student)

    amount_received = transactions.aggregate(total_amount=Sum('Amount'))['total_amount']
    balance_amount = float(student.First_Payment) - float(amount_received)

    context = {
        'student' : student,
        'page' : 'students',
        'amount_received' : amount_received,
        'balance_amount' : balance_amount,
        'transactions' : transactions
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

#----------------------------------- News List -----------------------------------#

@login_required
def news(request):
    newses = News.objects.all().order_by('-id')
    context = {
        'page' : 'website',
        'newses' : newses
    }
    return render(request,'Dashboard/News/news-list.html',context)

#----------------------------------- Add News -----------------------------------#

@login_required
def add_news(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        sub_title = request.POST.get('sub_title')
        image = request.FILES.get('image')
        description = request.POST.get('description')

        try:
            News.objects.create(Title=title,Sub_Title=sub_title,Image=image,Description=description)
            messages.success(request,'News added successfully ... !')
            return redirect('news')
        
        except Exception as exception:
            messages.warning(request,exception)
            return redirect('add-news')
        
    context = {
        'page' : 'website'
    }
    return render(request,'Dashboard/News/news-add.html',context)

#----------------------------------- Edit News -----------------------------------#

@login_required
def edit_news(request,news_id):
    news = News.objects.get(id=news_id)

    if request.method == 'POST':
        if len(request.FILES) > 0:
            news.Image = request.FILES.get('image')

        news.Title = request.POST.get('title')
        news.Sub_Title = request.POST.get('sub_title')
        news.Description = request.POST.get('description')

        try:
            news.save()
            messages.success(request,'News details edited successfully ... !')
            return redirect('news')
        
        except Exception as exception:
            messages.warning(request,exception)
            return redirect('edit-news',news_id=news.id)

    context = {
        'page' : 'news',
        'news' : news
    }
    return render(request,'Dashboard/News/news-edit.html',context)

#----------------------------------- DELETE NEWS -----------------------------------#

@login_required
def delete_news(request):
    if request.method == 'POST':
        news_id = request.POST.get('news_id')
        news = News.objects.get(id=news_id)

        try:
            news.delete()
            messages.success(request,'News deleated successfully ... !')
        except Exception as exception:
            messages.warning(request,exception)
    return redirect('news')

#----------------------------------- Enquiries -----------------------------------#

@login_required
def enquiries(request):
    enquiries = Enquiry.objects.all().order_by('-Date')
    context = {
        'page' : 'website',
        'enquiries' : enquiries
    }
    return render(request,'Dashboard/Core/enquiries.html',context)

#----------------------------------- Reviews -----------------------------------#

@login_required
def reviews(request):
    reviews = Review.objects.all().order_by('-Date')
    context = {
        'page' : 'website',
        'reviews' : reviews
    }
    return render(request,'Dashboard/Core/reviews.html',context)

#----------------------------------- Review add -----------------------------------#

@login_required
def add_review(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        review = request.POST.get('review')

        try:
            Review.objects.create(Name=name,Description=review)
            messages.success(request, 'Review Added Successfully ... !')
        except Exception as exception:
            messages.warning(request,exception)

    return redirect('reviews')

#----------------------------------- Review Delete -----------------------------------#

@login_required
def delete_review(request):
    if request.method == 'POST':
        review_id = request.POST.get('review_id')
        review = Review.objects.get(id=review_id)

        try:
            review.delete()
            messages.success(request,'Review deleated successfully ... !')
        except Exception as exception:
            messages.warning(request,exception)
    return redirect('reviews')