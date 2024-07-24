from django.urls import reverse
import pytest
from rest_framework import status
from rest_framework.test import APIClient
from contacts.models import Contact, Category, CustomUser





@pytest.mark.django_db
def test_get_contact_list():
    client = APIClient()
    category = Category.objects.create(name='Office')
    Contact.objects.create(name='example', phone_no='111223', email='example@example.com', category=category)
    user = CustomUser.objects.create_user(username='admin', password='password', role='admin')
    client.force_authenticate(user=user)
    response = client.get(reverse('contact-list'))
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_create_contact():
    client = APIClient()
    category = Category.objects.create(name='Office')
    user = CustomUser.objects.create_user(username='admin', password='password', role='admin')
    client.force_authenticate(user=user)
    data = {
        'name': 'Bob Brown',
        'phone_no': '4445556666',
        'email': 'bob@example.com',
        'category': category.id
    }
    response = client.post(reverse('contact-list'), data, format='json')
    assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
def test_signup_view():
    client = APIClient()
    data = {
        'username': 'signupuser',
        'password': 'signuppassword',
        'role': 'user'
    }
    response = client.post(reverse('signup'), data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert 'token' in response.data

@pytest.mark.django_db
def test_login_view():
    client = APIClient()
    CustomUser.objects.create_user(username='loginuser', password='loginpassword', role='user')
    data = {
        'username': 'loginuser',
        'password': 'loginpassword'
    }
    response = client.post(reverse('login'), data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert 'token' in response.data



@pytest.mark.django_db
def test_create_contact_unauthorized():
    client = APIClient()
    category = Category.objects.create(name='Office')
    data = {
        'name': 'Ab',
        'phone_no': '5777',
        'email': 'a@example.com',
        'category': category.id
    }
    response = client.post(reverse('contact-list'), data, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_create_contact_with_invalid_data():
    client = APIClient()
    category = Category.objects.create(name='Office')
    user = CustomUser.objects.create_user(username='admin', password='password', role='admin')
    client.force_authenticate(user=user)
    data = {
        'name': '', 
        'phone_no': '46',
        'email': 'b@example.com',
        'category': category.id
    }
    response = client.post(reverse('contact-list'), data, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST