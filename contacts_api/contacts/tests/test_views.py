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

@pytest.mark.django_db
def test_get_contacts_by_category():
    client = APIClient()
    category = Category.objects.create(name='Office')
    contact1 = Contact.objects.create(name='John Doe', phone_no='1234567890', email='john@example.com', category=category)
    contact2 = Contact.objects.create(name='Jane Doe', phone_no='0987654321', email='jane@example.com', category=category)


    user = CustomUser.objects.create_user(username='admin', password='password', role='admin')
    client.force_authenticate(user=user)

    url = reverse('category-contacts', kwargs={'pk': category.id})
    response = client.get(url)
    
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2
    assert response.data[0]['name'] == contact1.name
    assert response.data[1]['name'] == contact2.name

@pytest.mark.django_db
def test_get_contacts_by_invalid_category():
    client = APIClient()
    user = CustomUser.objects.create_user(username='admin', password='password', role='user')
    client.force_authenticate(user=user)

    url = reverse('category-contacts', kwargs={'pk': 999})
    response = client.get(url)
    
    assert response.status_code == status.HTTP_404_NOT_FOUND

@pytest.mark.django_db
def test_get_contacts_by_category_no_contacts():
    client = APIClient()
    user = CustomUser.objects.create_user(username='admin', password='password', role='user')
    client.force_authenticate(user=user)
    category = Category.objects.create(name='Friends')

    url = reverse('category-contacts', kwargs={'pk': category.id})
    response = client.get(url)
    
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 0
