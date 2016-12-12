import datetime

from werkzeug.security import generate_password_hash

from vitola_api.models.user import User


def create_user(session, email, password):
    created_on = datetime.datetime.utcnow()
    password_hash = generate_password_hash(password)
    user = User(email=email, password=password_hash, created_on=created_on)
    session.add(user)
    return user
