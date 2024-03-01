from django.urls import path
from Accounts import views

urlpatterns = [
    path('',views.accounts,name='accounts')
]