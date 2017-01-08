import random
import string

from vitola_api.actions.humidors import create_humidor
from vitola_api.actions.users import create_user


def setup_user(session, email=None, password=None):
    if not email:
        email = ''.join(random.choice(string.ascii_lowercase) for _ in range(5)) + '@test.com'
    if not password:
        password = 'secure'
    user = create_user(session=session, email=email, password=password)
    session.commit()
    return user


def setup_humidor(session, user_uid, name=None):
    if not name:
        name = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
    humidor = create_humidor(session=session, name=name, created_by=user_uid)
    session.commit()
    return humidor
