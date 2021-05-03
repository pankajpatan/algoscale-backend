from django.db import models

# Create your models here.
class Submissions(models.Model):
    FirstName = models.CharField(max_length=100,blank=True)
    LastName = models.CharField(max_length=100,blank=True)
    Email = models.CharField(max_length=100)
    Message = models.TextField()
    date_created = models.DateField(auto_now_add=True)