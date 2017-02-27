from marshmallow import Schema, fields

from common import messages
from vitola_api.validators.utils import ExtraFieldsMixin


class UserSchema(Schema):
    email = fields.String(required=True)


class UserCreateSchema(Schema, ExtraFieldsMixin):
    email = fields.String(required=messages.user_email_missing)
    password = fields.String(required=messages.user_password_missing)
