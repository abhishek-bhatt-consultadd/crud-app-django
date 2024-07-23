import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from contacts.models import Contact, Category
from contacts.utils import create_jwt

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user():
    return User.objects.create_user(username='testuser', password='testpassword')

@pytest.fixture
def auth_client(api_client, user):
    url = reverse('login')
    data = {
        'username': 'testuser',
        'password': 'testpassword'
    }
    response = api_client.post(url, data)
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {response.data['token']}")
    return api_client

@pytest.mark.django_db
def test_signup_view(api_client):
    url = reverse('signup')
    data = {
        'username': 'newuser',
        'password': 'newpassword'
    }
    response = api_client.post(url, data)
    assert response.status_code == 201
    assert 'token' in response.data

@pytest.mark.django_db
def test_login_view(api_client, user):
    url = reverse('login')
    data = {
        'username': 'testuser',
        'password': 'testpassword'
    }
    response = api_client.post(url, data)
    assert response.status_code == 200
    assert 'token' in response.data

@pytest.mark.django_db
def test_contact_viewset(auth_client):
    url = reverse('contact-list')
    response = auth_client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_create_contact(auth_client):
    url = reverse('contact-list')
    data = {
        'name': 'Jane Doe',
        'phone_no': '0987654321',
        'email': 'jane@example.com',
        'address': '456 Main St'
    }
    response = auth_client.post(url, data)
    assert response.status_code == 201
    assert response.data['name'] == 'Jane Doe'

@pytest.mark.django_db
def test_category_viewset(auth_client):
    url = reverse('category-list')
    response = auth_client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_create_category(auth_client):
    url = reverse('category-list')
    data = {
        'name': 'Colleagues'
    }
    response = auth_client.post(url, data)
    assert response.status_code == 201
    assert response.data['name'] == 'Colleagues'
