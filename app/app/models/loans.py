from app import db
from datetime import datetime

class Loan(db.Model):
    __tablename__ = 'loans'

    idLoan = db.Column(db.Integer, primary_key=True)
    loanDateLoan = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    returnDateLoan = db.Column(db.DateTime, nullable=True)
    fineLoan = db.Column(db.Float, default=0.0)
    statusLoan = db.Column(db.String(20), nullable=False, default='Active')

    # Relationships
    bookIdLoan = db.Column(db.Integer, db.ForeignKey('books.idBook'), nullable=False)
    userIdLoan = db.Column(db.Integer, db.ForeignKey('users.idUser'), nullable=False)

    bookLoan = db.relationship('Book', back_populates="loansBook", lazy=True)
    userLoan = db.relationship('User', back_populates="loansUser", lazy=True)

    def __repr__(self):
        return f'<Loan {self.idLoan} of Book {self.bookIdLoan} to User {self.userIdLoan}>'