from passlib.hash import sha256_crypt
from diary.models.db import DbConnection

db = DbConnection()


class Users:
    """Class for creating users"""
    def __init__(self, name, username, email, password):
        self.name = name
        self.username = username
        self.email = email
        # encrypts the password to be stored as hash
        self.password = sha256_crypt.encrypt(str(password))

    def signup_user(self):
        db.query(
            # stores the instance for each user
            "INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)",
            (self.name, self.email, self.username, self.password))

    
