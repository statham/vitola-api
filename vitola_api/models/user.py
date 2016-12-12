from vitola_api.models.helpers.values import generate_unique_id
from vitola_api.resources import db


class User(db.Model):
    __tablename__ = 'user'

    # fields
    uid = db.Column(db.String, primary_key=True, default=generate_unique_id)
    created_on = db.Column(db.DateTime(timezone=True), nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
