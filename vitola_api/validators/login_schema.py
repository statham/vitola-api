from marshmallow import Schema, fields

from vitola_api.validators.utils import ExtraFieldsMixin


class LoginSchema(Schema, ExtraFieldsMixin):
    email = fields.String(required=True)
    password = fields.String(required=True)
