from marshmallow import validates_schema
from marshmallow.exceptions import ValidationError

from common import messages


class ExtraFieldsMixin(object):
    @validates_schema(pass_original=True)
    def disallow_unsupported_inputs(self, processed_data, original_data):
        input_fields = original_data.keys()
        expected_fields = self.fields.keys() + [field.load_from for field in self.fields.values() if field.load_from is not None]
        excluded_fields = self.exclude
        unsupported_fields = set(input_fields) - set(expected_fields) - set(excluded_fields)
        if len(unsupported_fields) > 0:
            raise ValidationError(messages.unsupported_fields)
