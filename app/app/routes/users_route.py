from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.users import User
from app import db

bp = Blueprint('user', __name__, url_prefix='/User')

@bp.route('/')
def index():
    data = User.query.all()
    return render_template('users/index.html', data=data)

@bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nameUser = request.form['nameUser']
        passwordUser = request.form['passwordUser']        
        new_user = User(nameUser=nameUser, passwordUser=passwordUser)
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('user.index'))
    return render_template('users/add.html')

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    user = User.query.get_or_404(id)
    if request.method == 'POST':
        user.nameUser = request.form['nameUser']
        user.passwordUser = request.form['passwordUser']
        db.session.commit()        
        return redirect(url_for('user.index'))

    return render_template('users/edit.html', user=user)

@bp.route('/delete/<int:id>')
def delete(id):
    user = User.query.get_or_404(id)    
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('user.index'))
