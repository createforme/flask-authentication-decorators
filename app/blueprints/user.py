from flask import Blueprint, jsonify
from app.utils import token_required

user = Blueprint('user', __name__)


@user.route('/test')
@token_required
def test_route(user):
    return jsonify({"hello": "world", "user": user})
