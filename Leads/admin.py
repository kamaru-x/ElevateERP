from django.contrib import admin
from Leads.models import Leads,Lead_Timeline

# Register your models here.

@admin.register(Leads)
class LeadsModelAdmin(admin.ModelAdmin):
    list_display = ['Name','Date','Mobile','Place']

@admin.register(Lead_Timeline)
class Lead_TimelineModelAdmin(admin.ModelAdmin):
    list_display = ['Lead','Date','Title','Color']