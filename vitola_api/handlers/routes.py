from flask_restful import Api

from vitola_api.handlers.cigar_create_handler import CigarCreateHandler
from vitola_api.handlers.cigar_handler import CigarHandler
from vitola_api.handlers.humidor_create_handler import HumidorCreateHandler


def init_routes(app):
    @app.route("/ping")
    def ping(*args, **kwargs):
        return "pong"

    api = Api(app, prefix='/v1')

    api.add_resource(
        HumidorCreateHandler,
        '/humidors',
        methods=['POST'])

    api.add_resource(
        CigarCreateHandler,
        '/cigars',
        methods=['POST']
    )

    api.add_resource(
        CigarHandler,
        '/cigars/<string:cigar_uid>',
        methods=['GET'])
