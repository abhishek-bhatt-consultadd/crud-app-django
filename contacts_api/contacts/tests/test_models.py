
import pytest
from django.urls import reverse
from contacts.models import Category, Contact, CustomUser
from django.db.utils import IntegrityError

@pytest.mark.django_db
def test_category_model():
    category = Category.objects.create(name='Family')
    assert str(category) == 'Family'

@pytest.mark.django_db
def test_contact_model():
    category = Category.objects.create(name='Friends')
    contact = Contact.objects.create(
        name='John Doe',
        phone_no='1234567890',
        email='john@example.com',
        address='123 Elm St',
        category=category
    )
    assert str(contact) == 'John Doe'
    assert Contact.objects.get(email='john@example.com').phone_no == '1234567890'

@pytest.mark.django_db
def test_custom_user_model():
    user = CustomUser.objects.create_user(username='testuser', password='testpassword', role='user')
    assert user.username == 'testuser'
    assert user.check_password('testpassword')
    assert user.role == 'user'

