from flask_login import UserMixin
from app import db

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    idUser = db.Column(db.Integer, primary_key=True)
    nameUser = db.Column(db.String(80), unique=True, nullable=False)
    passwordUser = db.Column(db.String(120), nullable=False)
    
    booksUser = db.relationship("Loan", back_populates="userLoan", lazy='dynamic')  # Cambia el nombre de la relación
    loansUser = db.relationship("Loan", back_populates="userLoan", lazy='dynamic')  # Asegúrate de que el nombre coincida
    
    def get_id(self):
        return str(self.idUser)