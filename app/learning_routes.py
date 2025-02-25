from flask import Blueprint, render_template

learning_bp = Blueprint("learning", __name__)

# Route for flashcards
@learning_bp.route("/learning")
def flashcards():
    return render_template("flashcards.html")