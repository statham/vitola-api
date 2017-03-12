import os

from flask_cors import CORS

from vitola_api.handlers import routes
from vitola_api.resources import db


class Initializer():
    def __init__(self, app, env_name):
        self.app = app
        self.env_name = env_name
        self.routes_initialized = False

    def init_config(self):
        config_name = self.get_config_object_name(self.env_name)
        self.app.config.from_object(config_name)
        self.app.config['ENV'] = self.env_name

    def init_routes(self):
        if not self.routes_initialized:
            self.routes_initialized = True
            routes.init_routes(self.app)

    def init_db(self):
        db.init_app(self.app)
        self.app.app_ctx_globals_class.database = db

    def init_cors(self):
        CORS(self.app)


    def get_config_object_name(self, env_name):
        return 'config.{}.Config'.format(env_name)


def init(app, env_name='dev'):
    env_name = os.environ.get('CONFIG', env_name)
    initializer = Initializer(app, env_name=env_name)


    initializer.init_config()
    initializer.init_cors()
    initializer.init_routes()
    initializer.init_db()
