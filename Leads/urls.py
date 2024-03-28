from django.urls import path
from Leads import views

urlpatterns = [
    path('l/<str:status>/',views.leads,name='leads'),
    path('add/',views.add_lead,name='add-lead'),
    path('edit/<str:lead_id>/',views.edit_lead,name='edit-lead'),
    path('details/<str:lead_id>/',views.view_lead,name='lead-details'),
    path('delete/',views.delete_lead,name='delete-lead'),

    path('timeline/add/<str:lead_id>/',views.add_timeline,name='add-timeline')
]