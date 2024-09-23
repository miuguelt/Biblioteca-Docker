from app import db
from datetime import datetime

class ComputerUserLoan(db.Model):
    __tablename__ = 'computer_user_loans'

    idLoan = db.Column(db.Integer, primary_key=True)
    loanDate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    returnDate = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(20), nullable=False, default='Active')

    # Relationships
    computerId = db.Column(db.Integer, db.ForeignKey('computers.idComputer'), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('users.idUser'), nullable=False)

    computer = db.relationship('Computer', back_populates="loans", lazy=True)
    user = db.relationship('User', back_populates="loans", lazy=True)

    def __repr__(self):
        return f'<ComputerUserLoan {self.idLoan} of Computer {self.computerId} to User {self.userId}>'
