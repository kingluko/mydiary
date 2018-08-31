from flask_restful import reqparse, Resource, inputs
from passlib.hash import sha256_crypt
import jwt
import re
import datetime
from diary.models.db import DbConnection
from diary.models.entries_model import Entries
from diary.models.users_model import Users
from config import Config
from .decorator import is_logged_in


db = DbConnection()


class SignupResource(Resource):
    """This class allows the user to register on the app"""
    # Validate the data that comes from the user
    parser = reqparse.RequestParser()
    parser.add_argument(
        'name',
        required=True,
        trim=True,
        type=inputs.regex(r"([a-zA-Z\-]+)\s+([a-zA-Z\-]+)"),
        help='Valid names are required')
    parser.add_argument(
        'email',
        required=True,
        type=inputs.regex(
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"),
        help='A valid email is required')
    parser.add_argument(
        'username',
        required=True,
        trim=True,
        type=inputs.regex(r"(^[A-Za-z0-9-]+$)"),
        help='A valid username is required')
    parser.add_argument(
        'password',
        required=True,
        trim=True,
        help='A valid password is required')

    def post(self):
        # parses arguments
        results = SignupResource.parser.parse_args()
        name = results.get('name')
        username = results.get('username').lower()
        password = results.get('password')
        email = results.get('email')                   
        # Validate on entry
        if len(username) < 4:
            return {'message': 'Username cannot be less than 4'}, 400
        if len(password) < 6:
            return {'message': 'Password cannot be less than 6'}, 400
        # Check if email exists on db
        db.query("SELECT * FROM users WHERE email = %s OR username = %s", [email, username])
        data = db.cur.fetchone()
        # if not sign up
        if not data:
            user = Users(
                name=name, email=email, username=username, password=password)
            Users.signup_user(user)
            return {'message': 'You have registered succesfully'}, 201
        else:
            return {'message': 'User already exists'}, 400


class SigninResource(Resource):
    """THis class allows the user to sign in to the app"""
    # Validate infformation entered by the user
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        required=True,
        trim=True,
        help='Enter a valid username')
    parser.add_argument(
        'password',
        required=True,
        trim=True,
        help='Enter a valid password')

    def post(self):
        results = SigninResource.parser.parse_args()
        username = results.get('username').lower()
        password_entered = results.get('password')
        if username and password_entered:
                # check if the username exists
            db.query(
                "SELECT * FROM users WHERE username = %s", [username])
            # Check if the username exists
            data = db.cur.fetchone()
            if data:
                password = data[4]
                if sha256_crypt.verify(password_entered, password):
                    # Generate a token for the user
                    user_id = int(data[0])
                    token = jwt.encode(
                        {'user_id': user_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
                        str(Config.SECRET))
                    return {'message': 'You have successfully logged in',
                            'token': token.decode('UTF-8')}, 201
                else:
                    return {'message': 'Invalid password'}, 400
            else:
                return {'message': 'User not found'}, 400
            # close database connection
            db.close()
        else:
            return {'message': 'Please enter login details'}


class UserProfile(Resource):
    """This class returns the user details"""
    parser = reqparse.RequestParser()
    parser.add_argument(
        'reminder',
        trim=True
        )

    @is_logged_in
    def get(self, user_id):
        # gets user details
        user_details = Users.user_details(user_id)
        return user_details

    # TODO
    # Add reminder field to database
    @is_logged_in
    def post(self, user_id):
        # fetches if eminder is set
        results = UserProfile.parser.parse_args()
        reminder = results.get('reminder').lower()
        Users.add_reminder(user_id, reminder)
        if reminder == 'true':            
            return {'message': 'You will receive daily notifications'}
        elif reminder == 'false':
            return {'message': 'You will not receive daily notifications'}