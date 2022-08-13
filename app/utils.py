from functools import wraps
import jwt
from flask import request, make_response, jsonify
from app.exceptions import AuthenticationError
from app.config import Config


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'authorization' in request.headers:
            token = request.headers['authorization']
        if not token:
            raise AuthenticationError("Authorization header is missing")
        try:
            data = jwt.decode(token.split(
                ' ')[1], Config.SECRET_KEY, algorithms=['HS256'])
        except:
            raise AuthenticationError("Invalid Token")
        return f(data, *args, **kwargs)
    return decorator
