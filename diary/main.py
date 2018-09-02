from flask import Flask
from flask_restful import Api, Resource
from config import app_config
from diary.models.db import DbConnection
from flask_cors import CORS


db = DbConnection()


def create_app(configuration):
    """Configures app based on the environment"""

    app = Flask(__name__)
    app.config.from_object(app_config[configuration])
    CORS(app, resources={r'/api/v1/profile': {'origins': '*'}})
    app.config['CORS_HEADERS'] = 'Content-Type'
    # creates tables in the database
    db.create_tables()

    # Creates applications endpoints
    api = Api(app)

    from .controller.entries_resource import AllEntries, SingleEntry
    from .controller.users_resources import SigninResource, SignupResource, UserProfile

    # Defines methods for resources
    api.add_resource(SignupResource, '/api/v1/auth/signup')
    api.add_resource(SigninResource, '/api/v1/auth/signin')
    api.add_resource(AllEntries, '/api/v1/entries')
    api.add_resource(SingleEntry, '/api/v1/entries/<int:entry_id>')
    api.add_resource(UserProfile, '/api/v1/profile')

    # runs the application
    return app
