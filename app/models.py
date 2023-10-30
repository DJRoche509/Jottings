from app import app, db
from datetime import datetime, timezone, timedelta

# New class that extends db.Model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable= False)
    date = db.Column(db.Date, nullable = False)
    print('item added successfully')

    def __repr__(self):
        utc_date = datetime.now(timezone.utc) - timedelta(hours = 5)
        return f'{self.title.title()} created on {self.date.strftime("on %A, %B %d, %Y at %I:%M:%S %p CST")}'