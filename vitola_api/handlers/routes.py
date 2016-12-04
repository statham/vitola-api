from flask import Blueprint

def init_routes(app):
    @app.route("/ping")
    def ping(*args, **kwargs):
        return "pong"

    api = Blueprint('api', __name__)

    app.register_blueprint(api)
