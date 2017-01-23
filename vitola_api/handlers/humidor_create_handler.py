from vitola_api.actions.humidors import create_humidor
from vitola_api.handlers.base_handler import BaseHandler
from vitola_api.handlers.helpers.auth_helper import require_auth
from vitola_api.validators.humidor_schema import HumidorCreateSchema
from vitola_api.validators.humidor_schema import HumidorSchema


class HumidorCreateHandler(BaseHandler):
    @require_auth
    def post(self):
        user_id = self.get_user_id_from_header()
        request_data = self.get_request_data_or_400(validation_schema=HumidorCreateSchema)

        humidor = create_humidor(session=self.session, name=request_data['name'], created_by=user_id)

        if humidor:
            self.session.commit()

        return HumidorSchema(strict=True).dump(humidor).data, 201
