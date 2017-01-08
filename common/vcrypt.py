import bcrypt
from flask import current_app


def hashpw(password):
    is_unittest = current_app.config.get("TESTING", False)
    if is_unittest:
        salt = bcrypt.gensalt(log_rounds=4)
    else:
        salt = bcrypt.gensalt()

    return bcrypt.hashpw(password.encode('utf-8'), salt)
