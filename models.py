from datetime import datetime
from app import db

class Task(db.Model):
    id= db.Column(db.Integar, primary_key=True)
    title = db.Column(db.String(60), nullable = False)
    date = db.Column(db.Date, nullable = False)

    def __repr__(self):
        return f'{self.title}'