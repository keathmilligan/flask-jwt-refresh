"""
Sample Database Model Definition
"""

from marshmallow_sqlalchemy import field_for
from .. import db, ma


class Contact(db.Model):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(120))
    phone = db.Column(db.String(30))
    created = db.Column(db.DateTime)


class ContactSchema(ma.ModelSchema):
    class Meta:
        model = Contact
    id = field_for(Contact, 'id', dump_only=True)
