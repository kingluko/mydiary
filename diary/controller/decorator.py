from functools import wraps
import jwt
from flask import request
import os
from diary.models.db import DbConnection
from config import Config


db = DbConnection()


def is_logged_in(f):
    # creates a wrapper
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # creates a token variable
        token = None
        # gets the token from the header
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        else:
            return {'message': 'Token is missing'}, 401
        # if token exists it decodes and fetches user_id
        try:
            data = jwt.decode(token, Config.SECRET)
            user_id = data['user_id']
        # returns an error on invalid token
        except:
            return {'message': ' Token is invalid'}, 400
        # passes user_id through each wrapped funtion
        return f(user_id=user_id, *args, **kwargs)
    return decorated_function

