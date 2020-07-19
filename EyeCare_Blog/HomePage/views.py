from django.shortcuts import render,get_object_or_404
from blog.models import Blog
from .models import Services,PortFolio,Testimonials,ContactDetails
from PatientInfo.models import Appointments,Queries
from .forms import AppointmentForm,QueryForm
from django.contrib import messages
from django.views.generic import ListView
from django.urls import reverse
from django.db.models import Count

def home(request):
    
    if request.method == 'POST':
        if 'appoint_sub' in request.POST:
            a_form=AppointmentForm(request.POST)
            c_form=QueryForm()
            if a_form.is_valid():
                a_form.save()
                messages.success(request,f'Your form has been sent. You will receive a response either by phone or email')
                return reverse('home')

        elif 'contact_sub' in request.POST:
            c_form=QueryForm(request.POST)
            a_form=AppointmentForm()
            if c_form.is_valid():
                c_form.save()
                messages.success(request,f'Your form has been sent. You will receive a response either by phone or email')
                return reverse('home')
        
    else:
        a_form=AppointmentForm()
        c_form=QueryForm()
    
    context={
        'motto': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Fugiat eum vitae reiciendis atque sed illum incidunt quis',
        'about':PortFolio.objects.first(),
        'services':Services.objects.all(),
        'a_form':a_form,
        'latest':Blog.objects.order_by('-date_posted')[:3],
        'popular':Blog.objects.annotate(comment_count=Count('comment')).order_by('-comment_count')[:3] ,
        'testimonials':Testimonials.objects.all(),
        'c_form': c_form,
        'contact_details': ContactDetails.objects.first()
    }

    return render(request,'HomePage/index.html',context)

