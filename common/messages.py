from flask import current_app

from common import constants

content_type_not_json = u"Only payloads with 'content-type' 'application/json' are supported."
no_fields_in_json_body = u"JSON body must contain at least one field."
payload_not_json = u"Fields must be in JSON body."
unsupported_fields = u"Unsupported fields are not allowed in request."
error500 = u"Sorry, Vitola's system had an error. Please try again later."
incorrect_login = u"The password you entered is incorrect."


def incorrect_email_login(email):
    return u"No user found with email ({}).".format(email)


# Humidors
humidor_name_required = u"Humidor name required to create a humidor."


def humidor_not_found(humidor_uid):
    return u"Humidor ({}) does not exist.".format(humidor_uid)


# Skip
def skip_negative(input_value):
    return u"Pagination skip ({}) must be 0 or a positive integer.".format(input_value)


skip_not_integer = skip_negative


# Limit
def limit_zero_or_negative(input_value):
    return "Pagination limit ({}) must be a positive integer.".format(input_value)


def limit_too_large(input_value):
    limit_max = current_app.config.get('PAGINATION_LIMIT_MAX', constants.PAGINATION_LIMIT_MAX)
    return u"Pagination limit ({}) must be less than or equal to {}.".format(input_value, limit_max)
