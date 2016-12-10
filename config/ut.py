import os
from .base import BaseConfig


class config(BaseConfig):
    TESTING = True

    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL', 'postgresql://localhost/vitola_test')
