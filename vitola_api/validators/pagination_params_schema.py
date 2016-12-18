from marshmallow import Schema

from vitola_api.validators.utils import ExtraFieldsMixin


class EmptyParamsSchema(Schema, ExtraFieldsMixin):
    pass
