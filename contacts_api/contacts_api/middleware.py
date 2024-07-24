import jwt
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.deprecation import MiddlewareMixin

class JWTAuthenticationMiddleware(MiddlewareMixin):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super().__init__(get_response)

    def process_request(self, request):
        token = request.META.get('HTTP_AUTHORIZATION', None)
        if token and token.startswith('Bearer '):
            token = token.split(' ')[1]
            try:
                payload = jwt.decode(token, settings.JWT_AUTH['JWT_SECRET_KEY'], algorithms=['HS256'])
                user = User.objects.get(id=payload['user_id'])
                request.user = user
            except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, User.DoesNotExist):
                request.user = None
        else:
            request.user = None

class DisableCSRFMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)
        response = self.get_response(request)
        return response
