from flask import current_app
from marshmallow import fields
from marshmallow import ValidationError

from common import constants
from common import messages


class Limit(fields.Field):
    def _deserialize(self, val, attr, data):
        try:
            val = int(val)
        except ValueError:
            raise ValidationError(messages.limit_not_integer(val))
        return super(Limit, self)._deserialize(val, attr, data)

    def _serialze(self, val, attr, obj):
        try:
            val = int(val)
        except ValueError:
            raise ValidationError(messages.limit_not_integer(val))
        return super(Limit, self)._serialize(val, attr, obj)

    def _validate(self, val):
        if val <= 0:
            raise ValidationError(messages.limit_zero_or_negative(val))
        if val > int(current_app.config.get('PAGINATION_LIMIT_MAX', constants.PAGINATION_LIMIT_MAX)):
            raise ValidationError(messages.limit_too_large(val))
        return super(Limit, self)._validate(val)


class Skip(fields.Field):
    def _deserialize(self, val, attr, data):
        try:
            val = int(val)
        except ValueError:
            raise ValidationError(messages.skip_not_integer(val))
        return super(Skip, self)._deserialize(val, attr, data)

    def _serialize(self, val, attr, obj):
        try:
            val = int(val)
        except ValueError:
            raise ValidationError(messages.skip_not_integer(val))
        return super(Skip, self)._serialize(val, attr, obj)

    def _validate(self, val):
        if val < 0:
            raise ValidationError(messages.skip_negative(val))
        return super(Skip, self)._validate(val)
