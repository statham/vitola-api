import flask
import flask_restful
from flask import g
from flask import request

from common import errors
from common import messages
from vitola_api.handlers.helpers.marshmallow_helper import raise_bad_request_for_schema_errors
from vitola_api.validators.pagination_params_schema import EmptyParamsSchema


class BaseHandler(flask_restful.Resource):
    def __init__(self):
        self.config = flask.current_app.config
        self.session = g.database.session

    @staticmethod
    def get_json_body_or_400():
        if 'application/json' not in request.headers.get('content-type', ''):
            raise errors.BadRequest(messages.content_type_not_json)

        # raises no body error
        if (not request.data) or (len(request.data) == 0):
            raise errors.BadRequest(messages.payload_not_json)

        # raises json error
        json_data = request.get_json()

        # raises no body error
        if json_data is None or len(json_data) == 0:
            raise errors.BadRequest(messages.no_fields_in_json_body)

        return json_data

    @staticmethod
    def get_request_data_or_400(validation_schema):
        unvalidated_request_data = BaseHandler.get_json_body_or_400()

        # raise payload not json
        if not isinstance(unvalidated_request_data, dict):
            raise errors.BadRequest(messages.payload_not_json)

        validated_request_data, schema_errors = validation_schema().load(unvalidated_request_data)
        if schema_errors:
            raise_bad_request_for_schema_errors(schema_errors=schema_errors)

        return validated_request_data

    @staticmethod
    def get_user_id_from_header():
        return request.headers.get('X-Vitola-UserId')

    @staticmethod
    def get_query_params_or_400(SchemaClass=EmptyParamsSchema):
        validated_query_params, errors = SchemaClass().load(request.args.to_dict())
        if errors:
            raise_bad_request_for_schema_errors(errors)
        return validated_query_params

    @staticmethod
    def validate_query_params_or_400(SchemaClass=EmptyParamsSchema):
        BaseHandler.get_query_params_or_400(SchemaClass)
