from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import db, User

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")  # Get the username
        email = request.form.get("email")
        password = request.form.get("password")

        # Check if user already exists
        user_exists = User.query.filter_by(email=email).first()
        if user_exists:
            flash("Email already registered. Please log in.", category="warning")
        else:
            # Hash the password before storing it
            hashed_password = generate_password_hash(password, method="pbkdf2:sha256")
            new_user = User(username=username, email=email, password=hashed_password)  # Include username
            db.session.add(new_user)
            db.session.commit()
            flash("Account created successfully! Please log in.", category="success")
            return redirect(url_for("auth.login"))

    return render_template("signup.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        # Check if the user exists and the password is correct
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash("Logged in successfully!", category="success")
            return redirect(url_for("main.home"))
        else:
            flash("Invalid credentials. Please try again.", category="danger")

    return render_template("login.html")


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out successfully!", category="info")
    return redirect(url_for("main.home"))
