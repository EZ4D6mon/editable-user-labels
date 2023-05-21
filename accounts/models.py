from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length = 200, null = True)
    frequency = models.IntegerField(null = True)
    def __str__(self):
        return self.name
    
    
class Users(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length = 200, null = True)
    phone = models.CharField(max_length = 200, null = True, blank = True)
    email = models.CharField(max_length = 200, null = True, blank = True)
    date_created = models.DateTimeField(auto_now_add = True)
    tag = models.ManyToManyField(Tag, null = True, blank = True)
    def __str__(self):
        return self.name


    
