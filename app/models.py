from app import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, nullable=False)
    salary = db.Column(db.Numeric(10,2), index=True, nullable=False)
