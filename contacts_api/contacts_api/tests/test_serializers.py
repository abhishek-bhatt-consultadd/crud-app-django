import pytest
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from contacts.serialisers import UserSerializer, LoginSerializer
from contacts.models import Contact, Category

@pytest.mark.django_db
def test_user_serializer_create():
    data = {
        'username': 'testuser',
        'password': 'testpassword'
    }
    serializer = UserSerializer(data=data)
    assert serializer.is_valid()
    user = serializer.save()
    assert User.objects.count() == 1
    assert user.username == 'testuser'
    assert user.check_password('testpassword')

@pytest.mark.django_db
def test_login_serializer_valid():
    user = User.objects.create_user(username='testuser', password='testpassword')
    data = {
        'username': 'testuser',
        'password': 'testpassword'
    }
    serializer = LoginSerializer(data=data)
    assert serializer.is_valid()
    user = serializer.validated_data
    assert user.username == 'testuser'

@pytest.mark.django_db
def test_login_serializer_invalid():
    data = {
        'username': 'testuser',
        'password': 'wrongpassword'
    }
    serializer = LoginSerializer(data=data)
    with pytest.raises(ValidationError):
        serializer.is_valid(raise_exception=True)
