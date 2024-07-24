import jwt
from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from django.http import HttpResponse
from unittest.mock import patch
from datetime import datetime, timedelta

from contacts_api.middleware import JWTAuthenticationMiddleware, DisableCSRFMiddleware

class MiddlewareTests(TestCase):
    
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def get_jwt_token(self, user):
        payload = {
            'user_id': user.id,
            'exp': datetime.utcnow() + settings.JWT_AUTH['JWT_EXPIRATION_DELTA']
        }
        token = jwt.encode(payload, settings.JWT_AUTH['JWT_SECRET_KEY'], algorithm='HS256')
        return token

    def test_jwt_authentication_valid_token(self):
        token = self.get_jwt_token(self.user)
        request = self.factory.get('/', HTTP_AUTHORIZATION=f'Bearer {token}')
        middleware = JWTAuthenticationMiddleware(self.factory)
        middleware.process_request(request)
        self.assertEqual(request.user, self.user)

    def test_jwt_authentication_invalid_token(self):
        request = self.factory.get('/', HTTP_AUTHORIZATION='Bearer invalidtoken')
        middleware = JWTAuthenticationMiddleware(self.factory)
        middleware.process_request(request)
        self.assertIsNone(request.user)

    @patch('jwt.decode', side_effect=jwt.ExpiredSignatureError)
    def test_jwt_authentication_expired_token(self, mock_decode):
        token = self.get_jwt_token(self.user)
        request = self.factory.get('/', HTTP_AUTHORIZATION=f'Bearer {token}')
        middleware = JWTAuthenticationMiddleware(self.factory)
        middleware.process_request(request)
        self.assertIsNone(request.user)

    def test_jwt_authentication_no_token(self):
        request = self.factory.get('/')
        middleware = JWTAuthenticationMiddleware(self.factory)
        middleware.process_request(request)
        self.assertIsNone(request.user)

    def test_disable_csrf_middleware(self):
        request = self.factory.get('/')
        response = HttpResponse('test response')
        middleware = DisableCSRFMiddleware(lambda req: response)
        response = middleware(request)
        self.assertTrue(getattr(request, '_dont_enforce_csrf_checks', False))
        self.assertEqual(response.content, b'test response')
