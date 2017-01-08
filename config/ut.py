import os
from .base import BaseConfig


class Config(BaseConfig):
    TESTING = True

    SECRET_KEY = 'dummy'
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL', 'postgresql://localhost/vitola_test')
