from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.start,name='home'),
    path('about/',views.about,name='about'),
    path('appointment/',views.bookAppointment,name='appointment'),
    path('blogsection/',views.blogSection,name='blogsection'),
    path('testimonials/',views.Testimony.as_view(),name='testimonials'),
    path('contact/',views.contact,name='contact'),
]