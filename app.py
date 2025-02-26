from app import create_app, db
import csv
from app import create_app, db
from app.models import Flashcard

app = create_app()

# with app.app_context():
#     db.drop_all()  # This will drop all tables in the database
#     db.create_all()  # Recreate them

# app.app_context().push()

# with open('app/static/csv/A1_word_list.csv', newline='', encoding='utf-8') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         card = Flashcard(
#             german_text=row['Question'],
#             english_translation=row['Answer']
#         )
#         db.session.add(card)
#     db.session.commit()
#
# print("A1 flashcards loaded successfully!")

if __name__ == "__main__":

    app.run(debug=True)
