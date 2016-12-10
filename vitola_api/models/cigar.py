class Cigar(db.Model):
    __tablename__ = 'cigar'

    #fields
    added_on = db.Column(db.Datetime(timezone=True), nullable=False)
    age_alert_on = db.Column(db.Datetime(timezone=True))
    brand = db.Column(db.String, nullable=False)
    custom_id = db.Column(db.String)
    line = db.Column(db.String, nullable=False)
    note = db.Column(db.String)
    vitola = db.Column(db.String)
    rest_alert_on = db.Column(db.Datetime(timezone=True))
