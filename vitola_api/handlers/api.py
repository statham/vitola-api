from flask_restful import Api

from common.errors import JSONError
from common.messages import error500


class VitolaApi(Api):
    def handle_error(self, e):
        code = getattr(e, 'code', 500)

        if code == 500:
            message = error500

        else:
            if isinstance(e, JSONError):
                message = e.data
            else:
                message = getattr(e, 'message', error500)

        response = {
                'message': message,
        }
        return self.make_response(response, code)
