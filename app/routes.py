from flask.helpers import make_response
from app import db
from app.models.book import Book
from app.models.author import Author
from flask import Blueprint, jsonify, request

books_bp = Blueprint("books_bp", __name__, url_prefix="/books")

@books_bp.route("", methods=["POST", "GET"])
def handle_books():
    if request.method == "POST":
        request_body = request.get_json()
        if "title" not in request_body or "description" not in request_body:
            return jsonify("Invalid Request"), 400

        new_book = Book(
            title = request_body["title"],
            description = request_body["description"]
        )
        db.session.add(new_book)
        db.session.commit()
        
        new_book_response = {
            "id": new_book.id,
            "title": new_book.title,
            "description": new_book.description
        }

        return jsonify(new_book_response), 201
        
    elif request.method == "GET":
        title_query = request.args.get("title")
        description_query = request.args.get("description") #Optional; I can limit the what can be searched for

        if title_query:
            books = Book.query.filter(Book.title.contains(title_query))
        elif description_query: 
            books = Book.query.filter_by(description=description_query) # Optional
        else:
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
        return jsonify(books_response), 200

@books_bp.route("/<book_id>", methods=["GET", "PUT", "DELETE"])
def handle_book(book_id):
    book = Book.query.get(book_id) # either I get the book back or None
    if book is None:
        return jsonify(book_id), 404 

    if request.method == "GET":
        return {
                "id": book.id,
                "title": book.title,
                "description": book.description
            }
            
    elif request.method =="PUT":
        if book is None:
            return jsonify(book_id), 404

        request_body = request.get_json()
        if "title" not in request_body or "description" not in request_body:
            return jsonify("Invalid Request"), 400

        book.title = request_body["title"]
        book.description = request_body["description"]

        db.session.commit()

        return jsonify(book_id), 201

    elif request.method == "DELETE":   
        if book is None:
            return jsonify(book_id), 404

        db.session.delete(book)
        db.session.commit()

        return jsonify(book_id), 200

authors_bp = Blueprint("authors_bp", __name__, url_prefix="/authors")

@authors_bp.route("authors/<author_id>/books", methods=["GET", "POST"])
def get_authors(author_id):
    author = Author.query.get(id=author_id)
    if author is None:
        return jsonify(None), 404

    if request.method == "POST":
        request_body = request.get_json()
        if "title" not in request_body or "description" in request_body:
            return jsonify("Invalid Request"), 400
        
        new_book = Book(
            title = request_body["title"],
            description = request_body["description"],
            author = author
        )
        db.session.add(new_book)
        db.session.commit()

        # new_book_response = {
        #     "id": new_book.id,
        #     "name": new_book.name
        # }

        return make_response(f"Book {new_book.title} by {new_book.author.name} successfully created", 201)

    elif request.method == "GET":
        # name_query = request.args.get("name")

        # if name_query:
        #     authors = Author.query.filter(Author.name.contains(name_query))
        # else:
        #     authors = Author.query.all()

        books_response = []
        for book in author.books:
            books_response.append(
                {
                    "id": book.id,
                    "title": book.title,
                    "description": book.description
                }
            )
        return jsonify(books_response), 200

