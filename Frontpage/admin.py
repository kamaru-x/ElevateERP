from django.contrib import admin
from Frontpage.models import Review,Enquiry

# Register your models here.

@admin.register(Review)
class ReviewModelAdmin(admin.ModelAdmin):
    list_display = ['Date','Name','Description']

@admin.register(Enquiry)
class EnquiryModelAdmin(admin.ModelAdmin):
    list_display = ['Date','Name','Email','Subject','Description']