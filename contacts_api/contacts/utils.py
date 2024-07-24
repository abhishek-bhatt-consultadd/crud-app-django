import jwt
from django.conf import settings
from datetime import datetime, timedelta

def create_jwt(user, exp_delta=None):
    if exp_delta is None:
        exp_delta = settings.JWT_AUTH['JWT_EXPIRATION_DELTA']
    
    payload = {
        'user_id': user.id,
        'username': user.username,
        'exp': datetime.utcnow() + exp_delta
    }
    token = jwt.encode(payload, settings.JWT_AUTH['JWT_SECRET_KEY'], algorithm='HS256')
    return token

def decode_jwt(token):
    try:
        payload = jwt.decode(token, settings.JWT_AUTH['JWT_SECRET_KEY'], algorithms=['HS256'])
        return payload
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        return None
