__all__ = (
    'STATUS_DESCRIPTIONS',
    'JSONError',
    'NotModified',
    'BadRequest',
    'Unauthorized',
    'Forbidden',
    'NotFound',
    'Conflict',
    'Gone',
    'PreconditionFailed',
    'InternalError',
    'NotImplemented',
    'BadGateway',
    'ServiceUnavailable',
    'GatewayTimeout'
)

STATUS_DESCRIPTIONS = {
    200: 'OK',
    201: 'Created',
    202: 'Accepted',
    204: 'No Content',
    303: 'See Other',
    304: 'Not Modified',
    400: 'Bad Request',
    401: 'Unauthorized',
    403: 'Forbidden',
    404: 'Not Found',
    409: 'Conflict',
    410: 'Gone',
    412: 'Precondition Failed',
    500: 'Internal Server Error',
    501: 'Not Implemented',
    502: 'Bad Gateway',
    503: 'Service Unavailable',
    504: 'Gateway Timeout',
}


class JSONError(Exception):
    headers = [
        ('Content-Type', 'application/json; content-type=UTF-8'),
    ]

    def __init__(self, msg=None, translation_key=None):
        self.status_code = '%d %s' % \
            (self.code, STATUS_DESCRIPTIONS[self.code])
        self.data = unicode(msg or self.message)
        self.t = translation_key
        super(JSONError, self).__init__(self.data or self.status)


class NotModified(JSONError):
    code, message = 304, ''


class BadRequest(JSONError):
    code, message = 400, 'invalid request'


class Unauthorized(JSONError):
    code, message = 401, 'not logged in'


class Forbidden(JSONError):
    code, message = 403, 'forbidden'


class NotFound(JSONError):
    code, message = 404, "not found"


class Conflict(JSONError):
    code, message = 409, 'conflict'


class Gone(JSONError):
    code, message = 410, 'gone'


class PreconditionFailed(JSONError):
    code, message = 412, 'precondition failed'


class InternalError(JSONError):
    code, message = 500, 'server error; please try again later'


class NotImplemented(JSONError):
    code, message = 501, 'not implemented'


class BadGateway(JSONError):
    code, message = 502, 'upstream server error; please try again later'


class ServiceUnavailable(JSONError):
    code, message = 503, 'service unavailable; please try again later'


class GatewayTimeout(JSONError):
    code, message = 504, 'upstream server timed out; please try again later'
