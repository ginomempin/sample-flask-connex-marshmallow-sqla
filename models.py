from datetime import datetime

from config import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import fields


class Note(db.Model):
    __tablename__ = "note"
    note_id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey("person.person_id"))
    content = db.Column(db.String, nullable=False)
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class NotePersonSchema(SQLAlchemyAutoSchema):  # noqa
    """
    This class exists to get around a recursion issue
    """

    person_id = fields.Int()
    lname = fields.Str()
    fname = fields.Str()
    timestamp = fields.Str()


class NoteSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Note
        include_relationships = True
        load_instance = True

    person = fields.Nested("NotePersonSchema", default=None)


class Person(db.Model):
    __tablename__ = "person"
    person_id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32))
    fname = db.Column(db.String(32))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    notes = db.relationship(
        "Note",
        backref="person",
        cascade="all, delete, delete-orphan",
        single_parent=True,
        order_by="desc(Note.timestamp)",
    )


class PersonNoteSchema(SQLAlchemyAutoSchema):  # noqa
    """
    This class exists to get around a recursion issue
    """

    note_id = fields.Int()
    person_id = fields.Int()
    content = fields.Str()
    timestamp = fields.Str()


class PersonSchema(SQLAlchemyAutoSchema):  # noqa
    class Meta:
        model = Person
        include_relationships = True
        load_instance = True

    notes = fields.Nested("PersonNoteSchema", default=[], many=True)
