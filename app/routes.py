from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, make_response, request 

books_bp = Blueprint("books_bp", __name__, url_prefix="/books")

@books_bp.route("", methods=["POST", "GET"])
def handle_books():
    if request.method == "POST":
        request_body = request.get_json()
        if "title" not in request_body or "description" not in request_body:
            return make_response("Invalid Request", 400)

        new_book = Book(
            title = request_body["title"],
            description = request_body["description"]
        )
        db.session.add(new_book)
        db.session.commit()

        return make_response(
            f"Book {new_book.title} successfully created", 201
        )
    elif request.method == "GET":
        books = Book.query.all()
        books_response = []
        for book in books:
            books_response.append(
                {
                    "id": book.id,
                    "title": book.title,
                    "description": book.description
                }
            )
        return jsonify(books_response)

@books_bp.route("/<book_id>", methods=["GET"])
def handle_book(book_id):
    book = Book.query.get(book_id)

    if book is None:
        return make_response(f"Book {book_id} is not found", 404)

    return {
            "id": book.id,
            "title": book.title,
            "description": book.description
        }
    
# @books_bp.route("", methods=["GET"])
# def handle_books():
#     books_response = []
#     for book in books:
#         books_response.append({
#             "id": book.id,
#             "title": book.title,
#             "description": book.description
#         })
#     return jsonify(books_response)

# @books_bp.route("/<book_id>", methods=["GET"])
# def handle_book(book_id):
#     for book in books:
#         if book.id == book_id:
#            return {
#               "id": book.id,
#               "title": book.title,
#               "description": book.description
#           }

