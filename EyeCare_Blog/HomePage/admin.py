from django.contrib import admin
from .models import PortFolio,Services,ContactDetails,Testimonials

# Register your models here.
admin.site.register(PortFolio)
admin.site.register(Services)
admin.site.register(ContactDetails)
admin.site.register(Testimonials)