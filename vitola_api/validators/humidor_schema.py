from marshmallow import Schema, fields

from common import messages
from vitola_api.validators.utils import ExtraFieldsMixin


class HumidorSchema(Schema):
    uid = fields.String(required=True)
    name = fields.String(required=True)


class HumidorCreateSchema(Schema, ExtraFieldsMixin):
    name = fields.String(required=messages.humidor_name_required)
