from django.urls import path
from Core import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),

    path('places/',views.places,name='places'),
    path('place/add/',views.add_place,name='add-place'),
    path('place/edit/<str:place_id>/',views.edit_place,name='edit-place'),
    path('place/delete/',views.delete_place,name='delete-place'),

    path('agents/<str:rank>/',views.agents,name='agents'),
    path('agent/delete/',views.delete_agent,name='delete-agent'),
    path('agent/add/',views.add_agent,name='add-agent'),
    path('agent/edit/<str:agent_id>/',views.edit_agent,name='edit-agent'),

    path('courses/',views.courses,name='courses'),
    path('course/add/',views.add_course,name='add-course'),
    path('course/addons/<str:course_id>/',views.course_addons,name='course-addons'),
    path('course/addon/add/',views.add_addon,name='add-addon'),
    path('corse/addon/delete/',views.delete_addon,name='delete-addon'),
    path('course/delete/',views.delete_course,name='delete-course'),

    path('collages/',views.collages,name='collages'),
    path('collage/add/',views.add_collage,name='add-collage'),
    path('collage/edit/<str:collage_id>/',views.edit_collage,name='edit-collage'),
    path('collage/view/<str:collage_id>/',views.view_collage,name='view-collage'),
    path('collage/delete/',views.delete_collage,name='delete-collage'),

    path('students/',views.students,name='students'),
    path('student/add/',views.add_student,name='add-student'),
    path('get/addons/',views.get_addons,name='get-addons'),
    path('student/edit/<str:student_id>/',views.edit_student,name='edit-student'),
    path('student/details/<str:student_id>/',views.student_details,name='student-details'),
    path('student/delete/',views.delete_student,name='delete-student'),

    path('news/',views.news,name='news'),
    path('news/add/',views.add_news,name='add-news'),
    path('news/edit/<news_id>/',views.edit_news,name='edit-news'),
    path('news/delete/',views.delete_news,name='delete-news'),

    path('enquiries/',views.enquiries,name='enquiries'),
    path('reviews/',views.reviews,name='reviews'),
    path('review/add/',views.add_review,name='add-review'),
    path('review/delete/',views.delete_review,name='delete-review')
]