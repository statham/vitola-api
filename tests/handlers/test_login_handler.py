from flask import current_app
from python_jwt import verify_jwt

from common import messages
from tests.helpers.setup_helpers import setup_user
from tests.test_base import BaseTestCase


class LoginHandlerTest(BaseTestCase):
    def setUp(self):
        super(LoginHandlerTest, self).setUp()
        self.email = 'saba@vitola.com'
        self.password = 'good dog'
        self.user = setup_user(session=self.session, email=self.email, password=self.password)

    def test_should_create_access_token(self):
        response, code = self.post_login(email=self.email, password=self.password)
        self.assertEqual(200, code)
        access_token = response['access_token']
        header, claims = verify_jwt(access_token,
                                    current_app.config.get('SECRET_KEY'),
                                    [current_app.config.get('ACCESS_TOKEN_SIGNING_ALGORITHM')])
        self.assertEqual(self.user.uid, claims['user_id'])
        self.assertEqual('can-read', claims['scope'])

    def test_should_401_on_wrong_password(self):
        response, code = self.post_login(email=self.email, password='uh oh')
        self.assertEqual(401, code)
        self.assertEqual(messages.incorrect_login, response['message'])

    def test_should_400_on_wrong_user(self):
        email = 'scoobert@mysteryinc.com'
        response, code = self.post_login(email=email, password='ruh roh')
        self.assertEqual(400, code)
        self.assertEqual(messages.incorrect_email_login(email=email), response['message'])

    def post_login(self, email, password):
        data = {'email': email, 'password': password}
        return self.post_json('/v1/login', data=data) 
