import unittest
import json
import os
from diary.main import create_app
from diary.models.db import DbConnection
from config import app_config

db = DbConnection()
signup_url = '/api/v1/auth/signup'
signin_url = '/api/v1/auth/signin'


class BaseTestCase(unittest.TestCase):
    """Creates a base to test the entire application"""

    def setUp(self):
        config_test = os.getenv("APP_TESTING")
        self.app = create_app(config_test)
        self.client = self.app.test_client()

        self.signup_data = {
            "name": "Test Data",
            "username": "test123",
            "password": "123456789",
            "email": "test@123.com"
        }

        self.signin_data = {
            "username": "test123",
            "password": "123456789"
        }

        self.entry = {
            "title": "Test",
            "story": "This is a sample story"
        }

        self.entry_update = {
            "title": "Test123",
            "story": "This is an updated story"
        }
        # get entry ID
        self.signup_url = '/api/v1/auth/signup'
        self.signin_url = '/api/v1/auth/signin'

    def tearDown(self):
        db.query("DELETE FROM users WHERE username=%s", [self.signin_data["username"]])
