from app import app, db
from datetime import datetime, timezone, timedelta

# New class that extends db.Model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable= False)
    date = db.Column(db.DateTime, default=datetime.utcnow() - timedelta(hours=5), nullable = False)

    def __repr__(self):
        return f'{self.title.title()} created on {self.date.strftime("%A, %B %d, %Y at %I:%M:%S %p CST")}'