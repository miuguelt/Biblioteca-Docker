from flask import Blueprint, request, jsonify
from app import db
from app.models.cloans import ComputerUserLoan

cloans_bp = Blueprint('cloans', __name__)

@cloans_bp.route('/cloans', methods=['GET'])
def get_cloans():
    cloans = ComputerUserLoan.query.all()
    return jsonify([cloan.__repr__() for cloan in cloans])

@cloans_bp.route('/cloans/<int:id>', methods=['GET'])
def get_cloan(id):
    cloan = ComputerUserLoan.query.get_or_404(id)
    return jsonify(cloan.__repr__())

@cloans_bp.route('/cloans', methods=['POST'])
def create_cloan():
    data = request.get_json()
    new_cloan = ComputerUserLoan(
        computerId=data['computerId'],
        userId=data['userId'],
        loanDate=data.get('loanDate', datetime.utcnow()),
        returnDate=data.get('returnDate'),
        status=data.get('status', 'Active')
    )
    db.session.add(new_cloan)
    db.session.commit()
    return jsonify(new_cloan.__repr__()), 201

@cloans_bp.route('/cloans/<int:id>', methods=['PUT'])
def update_cloan(id):
    data = request.get_json()
    cloan = ComputerUserLoan.query.get_or_404(id)
    cloan.computerId = data.get('computerId', cloan.computerId)
    cloan.userId = data.get('userId', cloan.userId)
    cloan.loanDate = data.get('loanDate', cloan.loanDate)
    cloan.returnDate = data.get('returnDate', cloan.returnDate)
    cloan.status = data.get('status', cloan.status)
    db.session.commit()
    return jsonify(cloan.__repr__())

@cloans_bp.route('/cloans/<int:id>', methods=['DELETE'])
def delete_cloan(id):
    cloan = ComputerUserLoan.query.get_or_404(id)
    db.session.delete(cloan)
    db.session.commit()
    return '', 204
