from flask import Blueprint

# Create a Blueprint for better modularity
main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def home():
    return "Welcome to the German Learning App!"
