from django.shortcuts import render,get_object_or_404
from blog.models import Blog
from .models import Services,PortFolio,Testimonials,ContactDetails
from PatientInfo.models import Appointments,Queries
from .forms import AppointmentForm,QueryForm
from django.contrib import messages
from django.views.generic import ListView
from django.urls import reverse

def start(request):
    context={
        'motto': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Fugiat eum vitae reiciendis atque sed illum incidunt quis'
    }
    return render(request,'HomePage/index.html#home',context)

def about(request):
    context:{
        'about': PortFolio.objects.first()
    }
    return render(request,'HomePage/index.html#about-section',context)

def bookAppointment(request):
    if request.method == 'POST':
        form=AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Your form has been sent. You will receive a response either by phone or email')
            return reverse('home')
        
    else:
        form=AppointmentForm()

    context={
        'form': form,
        'services': Services.objects.all()
    }
    return render(request,'HomePage/index.html#service-section',context)

def blogSection(request):
    context={
        'latest':Blog.objects.order_by('-date_posted')[:3],
        'popular':Blog.objects.order_by('-comment_count')[:3]
    }
    return render(request,'HomePage/index.html#blog-section',context)

class Testimony(ListView):
    model:Testimonials
    template_name='HomePage/index.html#testimonial-section'

def contact(request):
    if request.method =='POST':
        form=QueryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Your form has been sent. You will receive a response either by phone or email')
            return reverse('home')
    else:
        form=QueryForm()
    
    context={
        'form': form,
        'contact_details': ContactDetails.objects.first()
    }
    return render(request,'HomePage/index.html#contact-section',context)    