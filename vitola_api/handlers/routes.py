from flask_restful import Api

from vitola_api.handlers.cigar_create_handler import CigarCreateHandler
from vitola_api.handlers.cigar_handler import CigarHandler


def init_routes(app):
    @app.route("/ping")
    def ping(*args, **kwargs):
        return "pong"

    api = Api(app, prefix='/v1')

    api.add_resource(
        CigarHandler,
        '/cigars/<string:cigar_uid>',
        methods=['GET'])

    api.add_resource(
        CigarCreateHandler,
        '/cigars',
        methods=['POST']
    )
