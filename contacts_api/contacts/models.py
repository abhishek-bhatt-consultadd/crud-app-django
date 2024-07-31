from django.db import models
from django.contrib.auth.models import AbstractUser

class Category(models.Model):
    name = models.CharField(max_length=100, default='Office', unique=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    phone_no = models.CharField(max_length=200, unique=True, blank=False)
    email = models.EmailField(blank=False)
    address = models.TextField(blank=True)
    category = models.ForeignKey(Category, related_name='contacts', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class CustomUser(AbstractUser):
    role = models.CharField(max_length=10, default='user')

