from django.contrib import admin
from .models import Appointments,Queries,Locations 

# Register your models here.
admin.site.register(Appointments)
admin.site.register(Queries)
admin.site.register(Locations)