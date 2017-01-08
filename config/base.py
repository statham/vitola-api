import os


class BaseConfig(object):
    ACCESS_TOKEN_SIGNING_ALGORITHM = os.environ.get('ACCESS_TOKEN_SIGNING_ALGORITHM', 'HS256')
    ACCESS_TOKEN_LIFETIME = os.environ.get('ACCESS_TOKEN_LIFETIME', 3600)
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class Config(BaseConfig):
    pass
