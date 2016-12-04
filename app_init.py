from flask_sqlalchemy import SQLAlchemy

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URL'] = 'postgresql://localhost/vitola_dev'
    db = SQLAlchemy(app)
    db.init_app(app)

def init(app):
    init_db(app)
