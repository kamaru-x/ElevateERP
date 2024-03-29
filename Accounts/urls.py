from django.urls import path
from Accounts import views

urlpatterns = [
    path('',views.accounts,name='accounts'),
    path('get/entry-categories/',views.get_entry_categories,name='get-entry-categories'),
    path('entry/add/',views.entry_add,name='add-entry'),
    path('get/fot/',views.get_fot,name='get-fot'),
    path('delete/transaction/',views.delete_transaction,name='delete-transaction')
]