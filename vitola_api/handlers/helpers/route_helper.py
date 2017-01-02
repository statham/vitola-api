from flask import current_app


def get_base_url():
    vitola_url = current_app.config.get('SERVER_NAME')
    return u'{}/'.format(vitola_url)


def create_humidor_list_route():
    return u'humidors'
