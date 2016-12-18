content_type_not_json = u"Only payloads with 'content-type' 'application/json' are supported."
no_fields_in_json_body = u"JSON body must contain at least one field."
payload_not_json = u"Fields must be in JSON body."
unsupported_fields = u"Unsupported fields are not allowed in request."
error500 = u"Sorry, Vitola's system had an error. Please try again later."

# Humidors
humidor_name_required = u"Humidor name required to create a humidor."


def humidor_not_found(humidor_uid):
    return u"Humidor ({}) does not exist.".format(humidor_uid)
