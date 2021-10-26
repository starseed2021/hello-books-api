from flask import Flask
from flask_sqlalchemy import SQLAlchemy #allows us to write SQL queries using Python
from flask_migrate import Migrate #version control for our models
from dotenv import load_dotenv #imports the .env variables
import os #allows us to get those environments w/ the method it has


db = SQLAlchemy() #the library that facilitates the communication between Python programs and databases.

# Handling database migrations
migrate = Migrate(compare_type=True) 
load_dotenv() #loads the .env values so that the os module can see them

def create_app(test_config=None):
    app = Flask(__name__)

    # our appication doesn't use the Falsk_SQLAlchemy event system
    # create configuration flag

    if not test_config:
    #We need to tell Flask where to find our new database
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")
    else:
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_TEST_DATABASE_URI")

    #everytime Flask runs and we add queries, the terminal will display our sql commands
    app.config['SQLALCHEM_ECHO'] = True

    #Connects db and migrate to our Flask app, using the package's recommended syntax
    db.init_app(app) 
    migrate.init_app(app, db)

    #Book model will be available to the app
    from app.models.book import Book
    
    # Register Blueprints here
    from .routes import books_bp
    app.register_blueprint(books_bp)


    return app 



