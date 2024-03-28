from django.shortcuts import render,redirect
from Leads.models import Leads,Lead_Timeline
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime

today = datetime.today()

# Create your views here.

@login_required
def leads(request,status):
    leads = Leads.objects.filter(Status=status).order_by('-Date')

    context = {
        'page' : 'leads',
        'status' : status,
        'leads' : leads
    }
    return render(request,'Dashboard/Leads/leads.html',context)


@login_required
def add_lead(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        place = request.POST.get('place')

        try:
            Leads.objects.create(Name=name,Mobile=mobile,Place=place,Staff=request.user)
            messages.success(request,'Lead Created Successfully ... !')
            return redirect('leads',status='PENDING')

        except Exception as exception:
            messages.warning(request,exception)
            return redirect('add-lead')
        
    context = {
        'page' : 'leads'
    }

    return render(request,'Dashboard/Leads/lead-add.html',context)

@login_required
def delete_lead(request):
    if request.method == 'POST':
        lead_id = request.POST.get('lead_id')
        lead = Leads.objects.get(id=lead_id)
        lead.delete()

    return redirect('leads',status=lead.Status)

@login_required
def edit_lead(request,lead_id):
    lead = Leads.objects.get(id=lead_id)

    if request.method == 'POST':
        lead.Name = request.POST.get('name')
        lead.Mobile = request.POST.get('mobile')
        lead.Place = request.POST.get('place')

        try:
            lead.save()
            messages.success(request,'Lead edited successfully ... !')
            return redirect('leads',status=lead.Status)
        except Exception as exception:
            messages.warning(request,exception)
            return redirect('edit-lead',lead_id=lead.id)
    
    context = {
        'page' : 'leads',
        'lead' : lead
    }
    return render(request,'Dashboard/Leads/lead-edit.html',context)

@login_required
def view_lead(request,lead_id):
    lead = Leads.objects.get(id=lead_id)
    timelines = Lead_Timeline.objects.filter(Lead=lead).order_by('-Date','-id')
    context = {
        'page' : 'leads',
        'lead' : lead,
        'today' : today,
        'timelines' : timelines
    }
    return render(request,'Dashboard/Leads/lead-details.html',context)

@login_required
def add_timeline(request,lead_id):
    lead = Leads.objects.get(id=lead_id)
    if request.method == 'POST':
        date = request.POST.get('date')
        title = request.POST.get('title')
        color = request.POST.get('color')

        try:
            Lead_Timeline.objects.create(Lead=lead,Date=date,Title=title,Color=color)
            messages.success(request,'Timeline Updated Successfully ... !')
        
        except Exception as exception:
            messages.warning(request,exception)

    return redirect('lead-details',lead.id)