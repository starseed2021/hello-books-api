from app import db


class Book(db.Model): #The class Book inherits from the db.Model from SQLAlchemy
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    author = db.relationship("Author", back_populates="books")

    def to_string(self):
        return f"{self.id}: {self.title} Description: {self.description}"

