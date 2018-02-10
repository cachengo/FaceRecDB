from app import db


class PhotoFeatures(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_name = db.Column(db.String(128), index=True)
    vector = db.Column(db.PickleType())
    model = db.Column(db.String(128))
    filename = db.Column(db.String(300))

