from app import db
class Book(db.Model):
    __tablename__ = 'books'
    idBook = db.Column(db.Integer, primary_key=True)
    titleBook = db.Column(db.String(255), nullable=False)
    authorIdBook = db.Column(db.Integer, db.ForeignKey('authors.idAuthor'))  # Cambia el nombre de la columna para mayor claridad
    
    authorBook = db.relationship("Author", back_populates="booksAuthor", lazy=True)  # Cambia lazy a True
    loansBook = db.relationship("Loan", back_populates="bookLoan", lazy='dynamic')
    
    def __repr__(self):
        return f'<Book {self.titleBook}>'
