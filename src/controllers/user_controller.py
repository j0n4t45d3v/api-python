from flask import Blueprint, jsonify, make_response, request
from src.services.user_service import get_all_user, get_by_id, insert_user, delete_user, update_user

user = Blueprint("user_bp", __name__)


@user.route('/users')
def find_all():
    try:
        users = get_all_user()
        data = [u.to_dict() for u in users]
        message = make_response(jsonify(data))
        message.status_code = 200

        return message
    except ValueError:
        return "ERROR"


@user.route('/users/<int:id>')
def find_one(id):
    try:
        one_user = get_by_id(id)
        data = one_user.to_dict()
        message = make_response(jsonify(data))
        message.status_code = 200

        return message
    except ValueError:
        return "ERROR"


@user.route('/users', methods=['POST'])
def create():
    try:
        insert_user(request.json)
        message = make_response(jsonify({'message': 'User Created'}))
        message.status_code = 201

        return message
    except ValueError:
        return "ERROR"


@user.route('/users/<int:id>', methods=['DELETE'])
def drop(id):
    try:
        delete_user(id)
        message = make_response(jsonify({'message': 'User Deleted'}))
        message.status_code = 200

        return message
    except ValueError:
        return "ERROR"


@user.route('/users/<int:id>', methods=['DELETE'])
def update(id):
    try:
        update_user(id, request.json)
        message = make_response(jsonify({'message': 'User Deleted'}))
        message.status_code = 200

        return message
    except ValueError:
        return "ERROR"
