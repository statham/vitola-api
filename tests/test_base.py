import json

from flask import Flask
from flask_testing import TestCase

from app_init import init
from vitola_api.handlers.helpers.auth_helper import generate_access_token
from vitola_api.handlers.helpers.auth_helper import generate_claims


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

    def get_json(self, url, headers=None):
        if not headers:
            headers = self.test_headers
        response = self.test_client.get(url, headers=headers)
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
        claims = generate_claims(session=self.session, user_id=user_id)
        access_token_dict = generate_access_token(claims=claims)
        self.test_headers['authorization'] = 'Bearer: {}'.format(access_token_dict['access_token'])

    def logout(self):
        if 'authorization' in self.test_headers:
            del self.test_headers['authorization']
