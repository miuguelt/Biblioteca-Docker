from app import db

class Computer(db.Model):
    __tablename__ = 'computers'

    idComputer = db.Column(db.Integer, primary_key=True)
    brandComputer = db.Column(db.String(50), nullable=False)
    modelComputer = db.Column(db.String(50), nullable=False)
    purchaseDateComputer = db.Column(db.DateTime, nullable=False)
    warrantyExpiryDateComputer = db.Column(db.DateTime, nullable=True)
    statusComputer = db.Column(db.String(20), nullable=False, default='Active')

    def __repr__(self):
        return f'<Computer {self.idComputer} - {self.brandComputer} {self.modelComputer}>'
