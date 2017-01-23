import uuid
from datetime import timedelta

from common import messages
from vitola_api.handlers.api import VitolaApi
from vitola_api.handlers.base_handler import BaseHandler
from vitola_api.handlers.helpers.auth_helper import generate_access_token
from vitola_api.handlers.helpers.auth_helper import generate_claims
from vitola_api.handlers.helpers.auth_helper import require_auth
from tests.test_base import BaseTestCase


class AuthRequiredHandler(BaseHandler):
    @require_auth
    def get(self):
        return 'derp'


class AuthHelperTest(BaseTestCase):
    def create_app(self):
        app = super(self.__class__, self).create_app()
        VitolaApi(app).add_resource(AuthRequiredHandler, '/herp', methods=['GET'])
        return app

    def setUp(self):
        super(AuthHelperTest, self).setUp()
        self.user_id = str(uuid.uuid4())

    def test_should_401_if_no_header_token(self):
        response, code = self.get_json('/herp', headers={})
        self.assertEqual(401, code)
        self.assertEqual(response['message'], messages.authentication_token_missing_or_not_provided)

    def test_should_401_if_token_expired(self):
        claims = generate_claims(session=self.session, user_id=self.user_id)
        access_token_dict = generate_access_token(claims=claims, lifetime=timedelta(seconds=-1))
        headers = {}
        headers['authorization'] = 'Bearer: {}'.format(access_token_dict['access_token'])
        response, code = self.get_json('/herp', headers=headers)
        self.assertEqual(401, code)
        self.assertIn('expired', response['message'])

    def test_should_401_if_malformed_token(self):
        headers = {'authorization': 'Bearer: herblurdeblurdeblur'}
        response, code = self.get_json('/herp', headers=headers)
        self.assertEqual(401, code)

    def test_should_work_for_correct_token(self):
        self.login(user_id=self.user_id)
        response, code = self.get_json('/herp')
        self.assertEqual(200, code)
        self.assertEqual('derp', response)
        self.logout()
