import bcrypt

from common import messages
from common.errors import BadRequest
from common.errors import Unauthorized
from vitola_api.actions.users import get_user_by_email
from vitola_api.handlers.base_handler import BaseHandler
from vitola_api.handlers.helpers.auth_helper import generate_access_token
from vitola_api.handlers.helpers.auth_helper import generate_claims
from vitola_api.validators.access_token_schema import AccessTokenSchema
from vitola_api.validators.login_schema import LoginSchema


class LoginHandler(BaseHandler):
    def post(self):
        request_data = self.get_request_data_or_400(validation_schema=LoginSchema)

        user = _get_user_or_400(session=self.session, email=request_data['email'])

        _validate_hash_or_401(user=user, password=request_data['password'])

        claims = generate_claims(session=self.session, user_id=user.uid)
        access_token_dict = generate_access_token(claims=claims)
        return AccessTokenSchema(strict=True).dump(access_token_dict).data


def _get_user_or_400(session, email):
    user = get_user_by_email(session=session, email=email)
    if not user:
        raise BadRequest(messages.incorrect_email_login(email=email))
    return user


def _validate_hash_or_401(user, password):
    if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        raise Unauthorized(messages.incorrect_login)
