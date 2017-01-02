from copy import copy
from urllib import urlencode

from vitola_api.handlers.helpers.route_helper import get_base_url


def create_paginated_response(data, resource_base_url, query_params, total_count):
    response = {'data': data, 'total_count': total_count, 'next_page_url': None}
    if query_params['skip'] + query_params['limit'] < total_count:
        response['next_page_url'] = _make_next_page_url(resource_base_url, query_params)
    return response


def _make_next_page_url(resource_base_url, query_params):
    query_params_copy = copy(query_params)

    query_params_copy['skip'] += query_params_copy['limit']

    # Flatten params from list to a string
    for param, value in query_params_copy.items():
        if isinstance(value, list):
            query_params_copy[param] = ','.join(value)

    url_params = urlencode([(param, value) for param, value in query_params_copy.items()
                            if value is not None])

    return '{}{}?{}'.format(get_base_url(), resource_base_url, url_params)
