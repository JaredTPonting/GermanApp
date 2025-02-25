from flask import Blueprint, render_template
from flask_login import login_required

# Create a Blueprint for better modularity
main_bp = Blueprint("main", __name__)

# Route for Home page
@main_bp.route("/")
def home():
    return render_template("home.html")


@main_bp.route("/profile")
def profile():
    return render_template("profile.html")

