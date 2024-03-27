from django.shortcuts import render,redirect
from Core.models import Place,News,Course,Course_Addon
from Frontpage.models import Enquiry,Review
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
    newses = News.objects.all()[:3]
    reviews = Review.objects.all().order_by('-id')
    context = {
        'page' : 'home',
        'newses' : newses,
        'reviews' : reviews
    }
    return render(request,'Frontpage/index.html',context)

def about(request):
    reviews = Review.objects.all().order_by('-id')
    context = {
        'page' : 'about',
        'reviews' : reviews
    }
    return render(request,'Frontpage/about.html',context)

def courses(request,department):
    programs = Course.objects.filter(Degree=department)
    courses = []

    for program in programs:
        addons = Course_Addon.objects.filter(Course=program)
        for addon in addons:
            courses.append(addon)

    context = {
        'department' : department,
        'programs' : programs,
        'courses' : courses,
        'page' : 'courses'
    }
    return render(request,'Frontpage/courses.html',context)

def course(request,course_id):
    return render(request,'Frontpage/course.html')

def events(request):
    last_news = News.objects.last()
    newses = News.objects.exclude(id=last_news.id)

    context = {
        'page' : 'events',
        'last_news' : last_news,
        'newses' : newses
    }
    return render(request,'Frontpage/events.html',context)

def event(request):
    return render(request,'Frontpage/event.html')

def study_india(request):
    places = Place.objects.filter(Location='India')
    context = {
        'page' : 'SI',
        'places' : places
    }
    return render(request,'Frontpage/studyindia.html',context)

def study_abroad(request):
    places = Place.objects.filter(Location='Abroad')
    context = {
        'page' : 'SA',
        'places' : places
    }
    return render(request,'Frontpage/studyabroad.html',context)

@csrf_exempt
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        subject = request.POST.get('subject')
        description = request.POST.get('description')

        Enquiry.objects.create(Name=name,Email=email,Mobile=mobile,Subject=subject,Description=description)
        
        return JsonResponse({'status':'success'})
    
    context = {
        'page' : 'contact',
    }
    
    return render(request,'Frontpage/contact.html',context)