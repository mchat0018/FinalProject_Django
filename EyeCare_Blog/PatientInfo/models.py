from django.db import models

# Create your models here.

class Locations(models.Model):
    place=models.CharField(max_length=50)
    address=models.TextField()
    contact=models.CharField(max_length=16)

    def __str__(self):
        return self.place

class Appointments(models.Model):
    
    phone=models.CharField(max_length=16)
    email=models.EmailField()
    full_name=models.CharField(max_length=30)
    location=models.ForeignKey(Locations, on_delete=models.SET_NULL, null=True)
    query=models.TextField()
    date_of_appointment=models.DateField(blank=True,null=True)
    time_of_appointment=models.TimeField(blank=True,null=True)

    def __str__(self):
        return self.full_name

class Queries(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.CharField(max_length=16)
    query=models.TextField()

    def __str__(self):
        return self.name




