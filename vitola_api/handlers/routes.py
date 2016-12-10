from flask import Blueprint

from vitola_api.handlers.cigar_create_handler import CigarCreateHandler
from vitola_api.handlers.cigar_handler import CigarHandler

def init_routes(app):
    @app.route("/ping")
    def ping(*args, **kwargs):
        return "pong"

    api = Blueprint('api', __name__)

    api.add_resource(
        CigarHandler,
        '/cigars/<string:cigar_uid>',
        methods=['GET'])

    api.add_resource(
        CigarCreateHandler,
        '/cigars',
        methods=['POST']
    )

    app.register_blueprint(api)
