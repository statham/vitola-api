from flask import current_app
from python_jwt import verify_jwt

from common import messages
from vitola_api.actions.users import get_user_by_email
from tests.helpers.setup_helpers import generate_random_string
from tests.test_base import BaseTestCase


class UserCreateHandlerTest(BaseTestCase):
    def setUp(self):
        super(UserCreateHandlerTest, self).setUp()

    def test_should_create_user(self):
        email = generate_random_string(length=10) + '@test.com'
        password = generate_random_string(length=8)
        response, code = self.post_user(data={'email': email, 'password': password})

        self.assertEqual(201, code)
        access_token = response['access_token']
        header, claims = verify_jwt(access_token,
                                    current_app.config.get('SECRET_KEY'),
                                    [current_app.config.get('ACCESS_TOKEN_SIGNING_ALGORITHM')])
        user = get_user_by_email(session=self.session, email=email)
        self.assertEqual(user.uid, claims['user_id'])
        self.assertEqual('can-read', claims['scope'])

    def test_should_409_when_user_already_exists(self):
        email = generate_random_string(length=10) + '@test.com'
        password = generate_random_string(length=8)
        response, code = self.post_user(data={'email': email, 'password': password})

        response, code = self.post_user(data={'email': email, 'password': password})

        self.assertEqual(409, code)
        self.assertEqual(messages.user_already_exists(email=email), response['message'])

    def test_should_400_without_email(self):
        response, code = self.post_user(data={'password': 'doesnt matter'})

        self.assertEqual(400, code)

    def test_should_400_without_password(self):
        response, code = self.post_user(data={'email': 'doesnt@matter.com'})

        self.assertEqual(400, code)

    def post_user(self, data):
        return self.post_json('/v1/users', data=data)
