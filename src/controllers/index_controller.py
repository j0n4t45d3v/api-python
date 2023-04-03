from flask import Blueprint, jsonify

index = Blueprint("index_bp", __name__)


@index.route('/')
def get_index():
    return jsonify({
        'message': "Hello World"
    })
