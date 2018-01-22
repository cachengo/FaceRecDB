from app import db


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    vector = db.Column(db.String(128))
    model = db.Column(db.String(128))

    #def get_progress(self):
    #    job = self.get_rq_job()
    #    return job.meta.get('progress', 0) if job is not None else 100
