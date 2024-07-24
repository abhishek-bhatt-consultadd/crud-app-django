import pytest
from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from contacts.serialisers import ContactSerializer, UserSerializer, LoginSerializer
from contacts.models import Contact, Category, CustomUser

@pytest.mark.django_db
def test_contact_serializer():
    category = Category.objects.create(name='Office')
    contact = Contact.objects.create(
        name='Jane Doe',
        phone_no='0987654321',
        email='jane@example.com',
        category=category
    )
    serializer = ContactSerializer(contact)
    data = serializer.data
    assert data['name'] == 'Jane Doe'
    assert data['phone_no'] == '0987654321'

@pytest.mark.django_db
def test_user_serializer_create():
    data = {
        'username': 'newuser',
        'password': 'newpassword',
        'role': 'user'
    }
    serializer = UserSerializer(data=data)
    assert serializer.is_valid()
    user = serializer.save()
    assert user.username == 'newuser'

@pytest.mark.django_db
def test_user_serializer_invalid():
    data = {'username': 'invaliduser'}
    serializer = UserSerializer(data=data)
    assert not serializer.is_valid()
