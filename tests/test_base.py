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
        self.test_headers = {}

    def tearDown(self):
        super(BaseTestCase, self).tearDown()
        self.db.session.remove()
        self.db.drop_all()
        self.db.engine.dispose()

    def get_json(self, url):
        response = self.test_client.get(url, headers=self.test_headers)
        return json.loads(response.data), response.status_code

    def post(self, url, data, content_type=None):
        response = self.test_client.post(url,
                                         data=data,
                                         headers=self.test_headers,
                                         content_type=content_type)
        return response.data, response.status_code

    def post_json(self, url, data, content_type='application/json'):
        data, status_code = self.post(url=url,
                                      data=json.dumps(data),
                                      content_type=content_type)
        return json.loads(data), status_code

    def login(self, user_id):
        self.test_headers['X-Vitola-UserId'] = user_id

    def logout(self):
        if 'X-Vitola-UserId' in self.test_headers:
            del self.test_headers['X-Vitola-UserId']
