import flask
import flask_restful


class BaseHandler(flask_restful.Resource):
    def __init__(self):
        self.config = flask.current_app.config
