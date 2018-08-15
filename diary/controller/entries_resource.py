from flask import jsonify, request
from flask_restful import reqparse, Resource
import json
from .decorator import is_logged_in
from diary.models.db import DbConnection
from diary.models.entries_model import Entries
from diary.models.users_model import Users


db = DbConnection()


class AllEntries(Resource):
    """Validates all entries on entry"""
    parser = reqparse.RequestParser()
    parser.add_argument(
        'title',
        required=True,
        type=str,
        trim=True,
        help='Enter a valid title')

    parser.add_argument(
        'story',
        required=True,
        type=str,
        trim=True,
        help='Enter a valid text')

    @is_logged_in
    def post(self, user_id):
        results = AllEntries.parser.parse_args()
        title = results.get('title')
        story = results.get('story')
        # Adding post to database if not blank
        if title and story:
            #  Check if the title exists
            db.query(
                "SELECT * from entries where title=%s AND user_id=%s",
                (title, user_id))
            data = db.cur.fetchone()
            # posts entry if it does not exist
            if not data:
                entry = Entries(title=title, user_id=user_id, story=story)
                entry.post()
                return {'message': 'Entry posted successfully'}, 201
            else:
                # returns an error if it exits
                return {"message": "Title Already Exists"}, 403
        else:
            return {'message': 'Fields cannot be blank'}, 400

    @is_logged_in
    def get(self, user_id, entry_id=None):
        """This method gets the entry for a given user"""
        entry = Entries.get(user_id=user_id)
        if entry:
            return {
                'message': 'Entries found', 'entry': Entries.make_dict(entry)}, 200
        else:
            return {'message': 'Entries not found'}, 404


class SingleEntry(Resource):
    @is_logged_in
    def put(self, user_id, entry_id):
        """Edit an Entry"""
        entry = Entries.get(user_id=user_id, entry_id=entry_id)
        if not entry:
            return {'message': 'The entry does not exist'}, 404
        else:
            results = request.get_json()
            new_title = results['title']
            new_story = results['story']
            # adds validation
            if new_title and new_story:
                db.query(
                    "UPDATE entries SET title=%s, story=%s WHERE entry_id=%s",
                    (new_title, new_story, entry_id))
                return{'message': 'Entry Updated'}, 200
            else:
                return{'message': 'Field cannot be blank'}, 400

    @is_logged_in
    def get(self, user_id, entry_id):
        """This method gets a single entry"""
        entry = Entries.get(user_id=user_id, entry_id=entry_id)
        if entry:
            return {
                'message': 'Entry found', 'entry': Entries.make_dict(entry)}
        else:
            return {'message': 'Entry not found'}, 404

    @is_logged_in
    def delete(self, user_id, entry_id):
        """This method is used to delte an entry"""
        entry = Entries.get(user_id=user_id, entry_id=entry_id)
        if not entry:
            return {'message': 'Entry not found'}, 404
        else:
            db.query(
                "DELETE FROM entries WHERE entry_id=%s", [entry_id]
            )
            return {'message': 'Entry has been deleted successfully'}, 200
