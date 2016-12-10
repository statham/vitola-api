import os


class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class Config(BaseConfig):
    pass
