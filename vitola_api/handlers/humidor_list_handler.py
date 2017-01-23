from vitola_api.actions.humidors import get_humidors
from vitola_api.handlers.base_handler import BaseHandler
from vitola_api.handlers.helpers.auth_helper import require_auth
from vitola_api.handlers.helpers.pagination_helper import create_paginated_response
from vitola_api.handlers.helpers.route_helper import create_humidor_list_route
from vitola_api.validators.humidor_schema import HumidorSchema
from vitola_api.validators.pagination_params_schema import SkipLimitSchema


class HumidorListHandler(BaseHandler):
    @require_auth
    def get(self):
        validated_query_params = self.get_query_params_or_400(SchemaClass=SkipLimitSchema)

        skip = validated_query_params['skip']
        limit = validated_query_params['limit']

        user_id = self.get_user_id_from_header()

        humidors = get_humidors(session=self.session,
                                user_id=user_id,
                                skip=skip,
                                limit=limit)
        total_count = humidors.count()

        humidors_dict = HumidorSchema(many=True, strict=True).dump(humidors).data

        return create_paginated_response(data=humidors_dict,
                                         resource_base_url=create_humidor_list_route(),
                                         query_params=validated_query_params,
                                         total_count=total_count)
