from datetime import datetime

from config import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class Person(db.Model):
    __tablename__ = "person"
    person_id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32))
    fname = db.Column(db.String(32))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class PersonSchema(SQLAlchemyAutoSchema):  # noqa
    class Meta:
        model = Person
        include_relationships = True
        load_instance = True
