from urllib import urlencode


from vitola_api.handlers.helpers.pagination_helper import create_paginated_response
from vitola_api.handlers.helpers.route_helper import get_base_url
from tests.test_base import BaseTestCase


# class PaginationHelperGetCurrentPageOfDataTest(BaseTestCase):
#     def test_get_current_page_of_data(self):
#         data = [i for i in xrange(10)]
#         current_page = get_current_page_of_data(data=data, skip=8, limit=2)
#         self.assertEqual(data[8:10], current_page)
#
#     def test_should_return_an_empty_list_for_pages_with_no_data(self):
#         data = [i for i in xrange(10)]
#         current_page = get_current_page_of_data(data=data, skip=60, limit=2)
#         self.assertEqual([], current_page)
#
#     def test_should_return_an_empty_list_when_no_data_is_given(self):
#         data = []
#         current_page = get_current_page_of_data(data=data, skip=2, limit=2)
#         self.assertEqual([], current_page)


class CreatePaginatedResponseTest(BaseTestCase):

    def test_paginated_response(self):
        mock_route = '/hell'
        total_count = 10
        data = range(total_count)
        query_params = {'skip': 7, 'limit': 2}
        response = create_paginated_response(data, mock_route, query_params, total_count)
        self.assertEqual(data, response['data'])
        self.assertEqual(total_count, response['total_count'])
        self.assertEqual(
            '{}{}{}'.format(
                get_base_url(),
                mock_route,
                "?skip=9&limit=2"),
            response['next_page_url'])

    def test_paginated_response_last_page(self):
        data = 'data'
        total_count = 10
        query_params = {'skip': 666, 'limit': 999}
        response = create_paginated_response(data, "hell", query_params, total_count)
        self.assertEqual(data, response['data'])
        self.assertEqual(total_count, response['total_count'])
        self.assertIsNone(response['next_page_url'])

    def test_paginated_response_next_page_encoded_correctly(self):
        data = 'data'
        total_count = 10
        query_params = {'skip': 1, 'limit': 5, 'some_list_param': ['value1', 'value2']}
        response = create_paginated_response(data, "hell", query_params, total_count)
        self.assertEqual(data, response['data'])
        self.assertEqual(total_count, response['total_count'])
        self.assertIsNotNone(response['next_page_url'])

        encoded_params = urlencode({'some_list_param': 'value1,value2'})
        self.assertTrue(encoded_params in response['next_page_url'])
