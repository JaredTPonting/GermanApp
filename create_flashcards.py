import csv
from app import create_app, db
from app.models import Flashcard


if __name__ =="__main__":
    app = create_app()
    app.app_context().push()

    with open('app/static/csv/A1_word_list.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            card = Flashcard(
                german_text=row['Question'],
                english_translation=row['Answer']
            )
            db.session.add(card)
        db.session.commit()

    print("A1 flashcards loaded successfully!")

