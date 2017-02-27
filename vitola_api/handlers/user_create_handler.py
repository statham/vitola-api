from common import messages
from common.errors import Conflict
from vitola_api.actions.users import create_user
from vitola_api.actions.users import get_user_by_email
from vitola_api.handlers.base_handler import BaseHandler
from vitola_api.handlers.helpers.auth_helper import generate_access_token
from vitola_api.handlers.helpers.auth_helper import generate_claims
from vitola_api.validators.access_token_schema import AccessTokenSchema
from vitola_api.validators.user_schema import UserCreateSchema


class UserCreateHandler(BaseHandler):
    def post(self):
        request_data = self.get_request_data_or_400(validation_schema=UserCreateSchema)

        user = get_user_by_email(session=self.session, email=request_data['email'])
        if user:
            raise Conflict(messages.user_already_exists(email=request_data['email']))

        user = create_user(session=self.session, email=request_data['email'], password=request_data['password'])

        if user:
            self.session.commit()

        claims = generate_claims(session=self.session, user_id=user.uid)
        access_token_dict = generate_access_token(claims=claims)
        return AccessTokenSchema(strict=True).dump(access_token_dict).data, 201
