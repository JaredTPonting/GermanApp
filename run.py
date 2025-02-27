from app import create_app, db
import csv
from app import create_app, db
from app.models import Flashcard

app = create_app()

if __name__ == "__main__":

    app.run(debug=True)
