from flask_login import UserMixin
from app import db

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    idUser = db.Column(db.Integer, primary_key=True)
    nameUser = db.Column(db.String(80), unique=True, nullable=False)
    passwordUser = db.Column(db.String(120), nullable=False)
    
    loansUser = db.relationship("Loan", back_populates="user", lazy='dynamic')
    computerLoansUser = db.relationship('ComputerLoan', back_populates='user', lazy='dynamic')

    def get_id(self):
        return str(self.idUser)