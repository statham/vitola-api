from sqlalchemy.orm import relationship

from vitola_api.models.cigar import Cigar
from vitola_api.models.helpers.values import generate_unique_id
from vitola_api.resources import db


class Humidor(db.Model):
    __tablename__ = 'humidor'

    # fields
    uid = db.Column(db.String, primary_key=True, default=generate_unique_id)
    created_by = db.Column(db.String, nullable=False)
    created_on = db.Column(db.DateTime(timezone=True), nullable=False)
    name = db.Column(db.String, nullable=False)

    # relationships
    cigars = relationship(Cigar, back_populates='humidor')
