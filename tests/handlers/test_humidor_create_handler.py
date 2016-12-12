from common import messages
from vitola_api.actions.humidors import get_humidor
from tests.helpers.setup_helpers import setup_user
from tests.test_base import BaseTestCase


class HumidorCreateHandlerTest(BaseTestCase):
    def setUp(self):
        super(HumidorCreateHandlerTest, self).setUp()
        self.user = setup_user(session=self.session)
        self.login(self.user.uid)

    def test_should_create_humidor(self):
        name = 'mr. peanutbutters house'
        response, code = self.post_humidor({'name': name})

        self.assertEqual(201, code)

        new_humidor_uid = response['uid']
        new_humidor_name = response['name']
        new_humidor = get_humidor(session=self.session, uid=new_humidor_uid)

        self.assertEqual(name, new_humidor_name)
        self.assertEqual([], new_humidor.cigars)
        self.assertEqual(self.user.uid, new_humidor.created_by)

    def test_should_400_with_extra_fields(self):
        response, code = self.post_humidor({'name': 'blah', 'hollywoo_stars_and_celebrities_what_do_they_know_do_they_know_things': 'lets_find_out'})
        self.assertEqual(400, code)
        self.assertEqual(response['message'], messages.unsupported_fields)

    def test_should_400_without_name(self):
        response, code = self.post_humidor({})
        self.assertEqual(400, code)
        self.assertEqual(response['message'], messages.no_fields_in_json_body)

    def post_humidor(self, data):
        return self.post_json('/v1/humidors', data=data)
