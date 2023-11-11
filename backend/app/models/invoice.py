from app import db


class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    issued_to = db.Column(db.String(120))
    # ... more fields for the invoice
