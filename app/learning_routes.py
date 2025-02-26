from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from app.models import Flashcard
from app import db

learning_bp = Blueprint("learning", __name__)

# Route for flashcards
@learning_bp.route("/flashcards")
@login_required
def flashcards():
    card = Flashcard.query.order_by(db.func.random()).first()
    return render_template("flashcards.html", card=card)


@learning_bp.route('/random_card')
@login_required
def random_card():
    card = Flashcard.query.order_by(db.func.random()).first()
    # Return the necessary fields as JSON.
    return jsonify({
        'id': card.id,
        'german': card.german_text,
        'translation': card.english_translation
    })