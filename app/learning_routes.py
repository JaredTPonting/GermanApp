from flask import Blueprint, render_template

learning_bp = Blueprint("learning", __name__)

# Route for flashcards
@learning_bp.route("/flashcards")
def flashcards():
    card = {
        "id": 1,
        "german": "Guten Morgen",
        "translation": "Good Morning"
    }
    return render_template("flashcards.html", card=card)