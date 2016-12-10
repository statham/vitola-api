import json

from flask import Flask
from flask_testing import TestCase

from app_init import init


class BaseTestCase(TestCase):
    def create_app(self):
        app = Flask(__name__)
        init(app, 'ut')
        self.test_client = app.test_client()
        self.config = app.config
        self.db = app.app_ctx_globals_class.database

        return app

    def setUp(self):
        super(BaseTestCase, self).setUp()

        self.db.create_all()

        self.session = self.db.session

    def tearDown(self):
        super(BaseTestCase, self).tearDown()
        self.db.session.remove()
        self.db.drop_all()
        self.db.engine.dispose()

    def get_json(self, url):
        response = self.test_client.get(url, headers=self.test_headers)
        return json.loads(response.data), response.status_code
