import datetime

import bcrypt

from vitola_api.models.user import User
from common import vcrypt


def create_user(session, email, password):
    created_on = datetime.datetime.utcnow()
    password_hash = vcrypt.hashpw(password)
    user = User(email=email, password=password_hash, created_on=created_on)
    session.add(user)
    return user


def get_user_by_email(session, email):
    return session.query(User).filter(User.email == email).one_or_none()


def get_user_permissions(session, user_id):
    return 'can-read'
