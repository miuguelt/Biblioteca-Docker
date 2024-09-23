from flask import Blueprint, render_template, request, redirect, url_for
from app.models.loans import Loan
from app.models.books import Book
from app.models.users import User
from app import db
from datetime import datetime, timedelta

bp = Blueprint('loan', __name__, url_prefix='/Loan')

@bp.route('/')
def index():
    loans = Loan.query.all()
    return render_template('loans/index.html', loans=loans)

@bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        book_id = request.form['bookIdLoan']
        user_id = request.form['userIdLoan']
        return_date = datetime.now() + timedelta(days=14)  # Préstamo por 14 días
        
        new_loan = Loan(bookIdLoan=book_id, userIdLoan=user_id, returnDateLoan=return_date)
        db.session.add(new_loan)
        db.session.commit()
        
        return redirect(url_for('loan.index'))
    
    books = Book.query.all()
    users = User.query.all()
    return render_template('loans/add.html', books=books, users=users)

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    loan = Loan.query.get_or_404(id)
    
    if request.method == 'POST':
        loan.returnDateLoan = datetime.strptime(request.form['returnDateLoan'], '%Y-%m-%d')
        loan.fineLoan = float(request.form['fineLoan'])
        loan.statusLoan = request.form['statusLoan']
        db.session.commit()
        return redirect(url_for('loan.index'))
    
    return render_template('loans/edit.html', loan=loan)

@bp.route('/delete/<int:id>')
def delete(id):
    loan = Loan.query.get_or_404(id)
    db.session.delete(loan)
    db.session.commit()
    return redirect(url_for('loan.index'))

@bp.route('/return/<int:id>')
def return_book(id):
    loan = Loan.query.get_or_404(id)
    loan.statusLoan = 'Returned'
    
    if datetime.now() > loan.returnDateLoan:
        days_late = (datetime.now() - loan.returnDateLoan).days
        loan.fineLoan = days_late * 1.0  # Multa de 1.0 por día de retraso
    
    db.session.commit()
    return redirect(url_for('loan.index'))
