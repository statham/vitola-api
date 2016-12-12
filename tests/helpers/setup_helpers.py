import random
import string

from vitola_api.actions.users import create_user


def setup_user(session, email=None):
    if not email:
        email = ''.join(random.choice(string.ascii_lowercase) for _ in range(5)) + '@test.com'
    user = create_user(session=session, email=email, password='secure')
    session.commit()
    return user
