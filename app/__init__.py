from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy() #the library that facilitates the communication between Python programs and databases.
migrate = Migrate() # Handling database migrations

def create_app(test_config=None):
    app = Flask(__name__)

    # our appication doesn't use the Falsk_SQLAlchemy event system
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
    #We need to tell Flask where to find our new database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development'

    #Connects db and migrate to our Flask app, using the package's recommended syntax
    db.init_app(app) 
    migrate.init_app(app, db)

    #Book model will be available to the app
    from app.models.book import Book
    
    # Register Blueprints here
    from .routes import books_bp
    app.register_blueprint(books_bp)


    return app 


