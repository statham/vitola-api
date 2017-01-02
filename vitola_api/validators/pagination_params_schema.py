from flask import current_app
from marshmallow import Schema

from common import constants
from vitola_api.validators.fields import Limit
from vitola_api.validators.fields import Skip
from vitola_api.validators.utils import ExtraFieldsMixin


def get_default_limit():
    return int(current_app.config.get('PAGINATION_LIMIT_MAX', constants.PAGINATION_LIMIT_MAX))


class EmptyParamsSchema(Schema, ExtraFieldsMixin):
    pass


class SkipLimitSchema(Schema, ExtraFieldsMixin):
    skip = Skip(required=False, missing=0)
    limit = Limit(required=False, missing=get_default_limit)
