from functools import wraps
from datetime import datetime
from datetime import timedelta

from flask import current_app
from flask import request
from python_jwt import generate_jwt
from python_jwt import verify_jwt

from common import errors
from common import messages
from common.constants import ACCESS_TOKEN_TYPES

from vitola_api.actions.users import get_user_permissions


def require_auth(handler, *args, **kwargs):
    @wraps(handler)
    def wrapper(*args, **kwargs):
        if request.headers.get('authorization') is None:
            raise errors.Unauthorized(messages.authentication_token_missing_or_not_provided)

        request_token = str(request.headers['authorization']).split(': ')  # i.e. ['Bearer ', 'some_token_value']
        if request_token[0] not in ACCESS_TOKEN_TYPES:
            raise errors.Unauthorized(messages.unsupported_access_token_type(request_token[0]))

        try:
            header, claims = verify_jwt(request_token[1], current_app.config.get('SECRET_KEY'), [current_app.config.get('ACCESS_TOKEN_SIGNING_ALGORITHM')])
        except Exception as e:
            raise errors.Unauthorized(e.message)

        return handler(*args, **kwargs)

    return wrapper


def generate_access_token(claims, key=None, algorithm=None, lifetime=None):
    if not key:
        key = current_app.config.get('SECRET_KEY')
    if not algorithm:
        algorithm = current_app.config.get('ACCESS_TOKEN_SIGNING_ALGORITHM')
    if not lifetime:
        default_lifetime = int(current_app.config.get('ACCESS_TOKEN_LIFETIME'))
        lifetime = timedelta(seconds=default_lifetime)
    now = datetime.utcnow()
    access_token = generate_jwt(claims=claims, priv_key=key, algorithm=algorithm, lifetime=lifetime)
    return {'access_token': access_token, 'token_type': 'bearer', 'expires_on': now + lifetime}


def generate_claims(session, user_id):
    permissions = get_user_permissions(session=session, user_id=user_id)
    return {'user_id': user_id, 'scope': permissions}
