from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'Frontpage/index.html')

def about(request):
    return render(request,'Frontpage/about.html')

def courses(request,department):
    context = {
        'department' : department
    }
    return render(request,'Frontpage/courses.html',context)

def course(request,course_id):
    return render(request,'Frontpage/course.html')

def events(request):
    return render(request,'Frontpage/events.html')

def event(request):
    return render(request,'Frontpage/event.html')

def study_india(request):
    return render(request,'Frontpage/studyindia.html')

def study_abroad(request):
    return render(request,'Frontpage/studyabroad.html')

def contact(request):
    return render(request,'Frontpage/contact.html')