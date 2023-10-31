from app import db
from datetime import datetime, timedelta

# New class that extends db.Model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable= False)
    date = db.Column(db.DateTime, default=datetime.utcnow() - timedelta(hours=5), nullable = False)

    def __repr__(self):
        # Return task.date to the desired time zone (CST) and format as a string
        return f'{self.title.capitalize()} created on {self.date.strftime("%A, %B %d, %Y at %I:%M:%S %p CST")}'