from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)


class Flashcard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    german_text = db.Column(db.String(255), nullable=False)
    english_translation = db.Column(db.String(255), nullable=False)

    total_attempts = db.Column(db.Integer, default=0)
    correct_attempts = db.Column(db.Integer, default=0)

    def calculate_strength(self):
        if self.total_attempts == 0:
            return 0  # No attempts, strength is 0
        return round((self.correct_attempts / self.total_attempts) * 100, 2)  # % accuracy
