from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Categories(models.Model):
    field=models.CharField(max_length=20)
    
    def __str__(self):
        return self.field

class Blog(models.Model):
    title=models.CharField(max_length=30)
    date_posted=models.DateTimeField(default=timezone.now)
    content=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    field_tag=models.ForeignKey(Categories,on_delete=models.CASCADE,blank=True,null=True)
    image=models.ImageField(default='default.jpg',upload_to='blog_pics')
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'pk':self.id})

class Comment(models.Model):
    author=models.CharField(max_length=30)
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    date_posted=models.DateTimeField(default=timezone.now)
    comment=models.TextField()

    def __str__(self):
        return self.blog.title

    def get_absolute_url(self):
        return reverse('blog_detail',kwargs={'pk':self.blog.id})



