from django.db import models
from django.contrib.auth.models import AbstractUser

class Category(models.Model):
    CATEGORY_CHOICES = [
        ('Family', 'Family'),
        ('Friends', 'Friends'),
        ('Office', 'Office'),
    ]
    name = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='Office')

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    phone_no = models.CharField(max_length=200, unique=True, blank=False)
    email = models.EmailField(unique=True, blank=False)
    address = models.TextField(blank=True)
    category = models.ForeignKey(Category, related_name='contacts', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

