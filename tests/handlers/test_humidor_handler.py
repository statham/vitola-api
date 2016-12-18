from common import messages
from tests.helpers.setup_helpers import setup_humidor
from tests.helpers.setup_helpers import setup_user
from tests.test_base import BaseTestCase


class HumidorHandlerTest(BaseTestCase):
    def setUp(self):
        super(HumidorHandlerTest, self).setUp()
        self.user = setup_user(session=self.session)
        self.login(self.user.uid)
        self.humidor = setup_humidor(session=self.session, user_uid=self.user.uid)

    def test_should_get_humidor(self):
        response, code = self.get_humidor(self.humidor.uid)
        self.assertEqual(200, code)
        self.assertEqual(self.humidor.uid, response['uid'])
        self.assertEqual(self.humidor.name, response['name'])

    def test_should_404_if_not_found(self):
        humidor_uid = 'rare_pepe'
        response, code = self.get_humidor(humidor_uid)
        self.assertEqual(404, code)
        self.assertEqual(response['message'], messages.humidor_not_found(humidor_uid))

    def get_humidor(self, humidor_uid):
        return self.get_json('/v1/humidors/{}'.format(humidor_uid))
