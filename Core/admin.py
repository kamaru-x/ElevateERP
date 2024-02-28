from django.contrib import admin
from Core.models import Place,Agents,Course,Collage,Student

# Register your models here.

@admin.register(Place)
class PlaceModelAdmin(admin.ModelAdmin):
    list_display = ['Name','Status','Added_Date']

@admin.register(Agents)
class AgentsModelAdmin(admin.ModelAdmin):
    list_display = ['Name','Mobile','Email','Place']

@admin.register(Course)
class CourseModelAdmin(admin.ModelAdmin):
    list_display = ['Name']

@admin.register(Collage)
class CollageModelAdmin(admin.ModelAdmin):
    list_display = ['Name','Mobile','Email','Place','Agent']

@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['Name','Mobile','Email','Place','Collage','Course']