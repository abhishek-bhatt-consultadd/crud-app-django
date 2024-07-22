from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    phone_no = models.CharField(max_length=200, unique=True, blank=False) 
    email = models.EmailField(unique=True, blank=False) 
    address = models.TextField(blank=True) 

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, default='Office') 
    contacts = models.ManyToManyField(Contact, related_name='categories')  # Many-to-Many relationship

    def __str__(self):
        return self.name
