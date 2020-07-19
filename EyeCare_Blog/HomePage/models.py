from django.db import models

# Create your models here.

class Services(models.Model):
    service=models.CharField(max_length=30)
    description=models.TextField()

    def __str__(self):
        return self.service

class PortFolio(models.Model):
    description=models.TextField()
    image=models.ImageField(upload_to='profile_pics')

class ContactDetails(models.Model): 
    email=models.EmailField()
    website=models.URLField()
    phone=models.CharField(max_length=16)

    def __str__(self):
        return 'Phone:{}  website:{}  email:{}'.format(self.phone,self.website,self.email)

class Testimonials(models.Model):
    name=models.CharField(max_length=30)
    profession=models.CharField(max_length=15)
    comment=models.TextField()
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
       return self.name