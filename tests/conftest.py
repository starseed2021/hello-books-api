from app.models.book import Book
import pytest
from app import create_app
from app import db

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    with app.app_context(): # Encapsulates our app and test db for the following test
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def two_saved_books(app):
    # Arrange
    ocean_book = Book(
        title = "Ocean Book",
        description = "The ocean as a divine entity."
    )
    food_book = Book(
        title = "Food Book",
        description = "A book about food and its origins."
    )

    db.session.add_all([ocean_book, food_book])
    # Alternatively, we could do
    # db.session.add(ocean_book)
    # db.session.add(food_book)
    db.session.commit()


