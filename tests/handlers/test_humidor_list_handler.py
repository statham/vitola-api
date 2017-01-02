from tests.helpers.setup_helpers import setup_humidor
from tests.helpers.setup_helpers import setup_user
from tests.test_base import BaseTestCase


class HumidorListHandlerTest(BaseTestCase):
    def setUp(self):
        super(HumidorListHandlerTest, self).setUp()
        self.user = setup_user(session=self.session)
        self.login(self.user.uid)
        self.humidors = [setup_humidor(session=self.session, user_uid=self.user.uid) for _ in xrange(5)]

    def test_should_get_humidor_list(self):
        response, code = self.get_humidor_list()
        self.assertEqual(200, code)
        self.assertEqual(5, response['total_count'])
        response_uids = [humidor['uid'] for humidor in response['data']]
        for humidor in self.humidors:
            self.assertIn(humidor.uid, response_uids)

    def test_should_return_none_if_no_humidors(self):
        user = setup_user(session=self.session)
        self.login(user)
        response, code = self.get_humidor_list()
        self.assertEqual(200, code)
        self.assertEqual([], response['data'])
        self.assertEqual(0, response['total_count'])
        self.assertEqual(None, response['next_page_url'])

    def get_humidor_list(self):
        return self.get_json('/v1/humidors')
