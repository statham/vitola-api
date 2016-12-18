from common import messages
from common.errors import NotFound
from vitola_api.actions.humidors import get_humidor
from vitola_api.handlers.base_handler import BaseHandler
from vitola_api.validators.humidor_schema import HumidorSchema


class HumidorHandler(BaseHandler):
    def get(self, humidor_uid):
        self.validate_query_params_or_400()

        user_uid = self.get_user_id_from_header()
        humidor = _get_humidor_or_404(session=self.session, humidor_uid=humidor_uid, user_uid=user_uid)
        return HumidorSchema(strict=True).dump(humidor).data


def _get_humidor_or_404(session, humidor_uid, user_uid):
    humidor = get_humidor(session=session, uid=humidor_uid)
    if not humidor:
        raise NotFound(messages.humidor_not_found(humidor_uid))
    return humidor
