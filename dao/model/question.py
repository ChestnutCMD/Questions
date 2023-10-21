"""Models, Serializers"""

from marshmallow import fields, Schema
from setup_db import db


class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True)
    id_question = db.Column(db.Integer)
    question = db.Column(db.String)
    answer = db.Column(db.String)
    created_at = db.Column(db.String)


class QuestionSchema(Schema):
    id = fields.Int()
    id_question = fields.Int()
    question = fields.Str()
    answer = fields.Str()
    created_at = fields.Str()
