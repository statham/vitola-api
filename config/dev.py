import os

from config.base import BaseConfig


class Config(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://localhost/vitola_api_dev')
