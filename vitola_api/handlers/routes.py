from vitola_api.handlers.api import VitolaApi
from vitola_api.handlers.cigar_create_handler import CigarCreateHandler
from vitola_api.handlers.cigar_handler import CigarHandler
from vitola_api.handlers.humidor_create_handler import HumidorCreateHandler
from vitola_api.handlers.humidor_handler import HumidorHandler
from vitola_api.handlers.humidor_list_handler import HumidorListHandler
from vitola_api.handlers.login_handler import LoginHandler
from vitola_api.handlers.user_create_handler import UserCreateHandler


def init_routes(app):
    @app.route("/ping")
    def ping(*args, **kwargs):
        return "pong"

    api = VitolaApi(app, prefix='/v1', catch_all_404s=True)

    api.add_resource(
        HumidorCreateHandler,
        '/humidors',
        methods=['POST'])

    api.add_resource(
        HumidorListHandler,
        '/humidors',
        methods=['GET'])

    api.add_resource(
        HumidorHandler,
        '/humidors/<string:humidor_uid>',
        methods=['GET'])

    api.add_resource(
        CigarCreateHandler,
        '/cigars',
        methods=['POST']
    )

    api.add_resource(
        CigarHandler,
        '/cigars/<string:cigar_uid>',
        methods=['GET'])

    api.add_resource(
        LoginHandler,
        '/login',
        methods=['POST'])

    api.add_resource(
        UserCreateHandler,
        '/users',
        methods=['POST'])
