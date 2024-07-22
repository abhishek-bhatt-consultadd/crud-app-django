from rest_framework import viewsets
from .models import Contact, Category
from .serialisers import ContactSerializer, CategorySerializer

class ContactViewSet(viewsets.ModelViewSet):  
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


