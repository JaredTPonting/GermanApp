from app import create_app, db

app = create_app()

with app.app_context():
    db.drop_all()  # This will drop all tables in the database
    db.create_all()  # Recreate them

if __name__ == "__main__":
    app.run(debug=True)
