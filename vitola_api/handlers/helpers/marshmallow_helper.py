from common.errors import BadRequest


def raise_bad_request_for_schema_errors(schema_errors):
    # These errors look like {'name': ['error_msg']}
    for key in schema_errors:
        # Only return first one
        raise BadRequest(schema_errors[key][0])
