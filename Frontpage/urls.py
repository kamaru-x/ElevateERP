from django.urls import path
from Frontpage import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('courses/<str:department>/',views.courses,name='courses'),
    path('contact/',views.contact,name='contact'),
    path('study-india/',views.study_india,name='study-india'),
    path('study-abroad/',views.study_abroad,name='study-abroad'),
    path('events/',views.events,name='events'),
]