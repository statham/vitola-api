import datetime

from vitola_api.models.humidor import Humidor


def get_humidor(session, uid):
    return session.query(Humidor).get(uid)


def create_humidor(session, name, created_by):
    created_on = datetime.datetime.utcnow()
    humidor = Humidor(name=name, created_by=created_by, created_on=created_on)
    session.add(humidor)
    return humidor
