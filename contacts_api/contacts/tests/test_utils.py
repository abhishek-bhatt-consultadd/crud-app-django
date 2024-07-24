from django.test import TestCase

from contacts.utils import create_jwt, decode_jwt
from datetime import datetime, timedelta
from contacts.models import CustomUser

class JWTTests(TestCase):
    
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', password='testpassword')

    def test_jwt_creation_and_decoding(self):
        token = create_jwt(self.user)
        self.assertIsNotNone(token)
        
        payload = decode_jwt(token)
        self.assertIsNotNone(payload)
        self.assertEqual(payload['user_id'], self.user.id)
        self.assertEqual(payload['username'], self.user.username)

    def test_jwt_expired(self):
        # Create a token with an expiration time in the past
        expired_delta = timedelta(seconds=-1)
        token = create_jwt(self.user, exp_delta=expired_delta)
        
        payload = decode_jwt(token)
        self.assertIsNone(payload)
