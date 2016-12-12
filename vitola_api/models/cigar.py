from sqlalchemy.orm import relationship

from vitola_api.models.helpers.values import generate_unique_id
from vitola_api.resources import db


class Cigar(db.Model):
    __tablename__ = 'cigar'

    # fields
    uid = db.Column(db.String, primary_key=True, default=generate_unique_id)
    added_on = db.Column(db.DateTime(timezone=True), nullable=False)
    age_alert_on = db.Column(db.DateTime(timezone=True))
    brand = db.Column(db.String, nullable=False)
    custom_id = db.Column(db.String)
    humidor_id = db.Column(db.String, db.ForeignKey('humidor.uid', name='cigar_humidor_uid_fkey'))
    line = db.Column(db.String, nullable=False)
    note = db.Column(db.String)
    vitola = db.Column(db.String)
    rest_alert_on = db.Column(db.DateTime(timezone=True))

    # relationships
    humidor = relationship('Humidor', back_populates='cigars')
