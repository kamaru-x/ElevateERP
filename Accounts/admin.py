from django.contrib import admin
from Accounts.models import Entry_Categories,Entry

# Register your models here.

@admin.register(Entry_Categories)
class Entry_CategoriesModelAdmin(admin.ModelAdmin):
    list_display = ['Title','Type']

@admin.register(Entry)
class EntryModelAdmin(admin.ModelAdmin):
    list_display = ['Title','Category','Date','Amount']