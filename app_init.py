from flask_sqlalchemy import SQLAlchemy

from vitola_api.handlers import routes

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URL'] = 'postgresql://localhost/vitola_dev'
    db = SQLAlchemy(app)
    db.init_app(app)

def init_routes(app):
    routes.init_routes(app)

def init(app):
    init_db(app)
    init_routes(app)
