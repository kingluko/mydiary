from datetime import datetime
from diary.models.db import DbConnection


db = DbConnection()


class Entries:
    """This class handles CRUD operations for entries"""
    def __init__(self, user_id, title, story):
        self.user_id = user_id
        self.title = title
        self.story = story

    def post(self):
        """This method adds an entry into the database"""
        db.query(
            "INSERT INTO entries(user_id, title, story) VALUES(%s, %s, %s)",
            (self.user_id, self.title, self.story))

    @staticmethod
    def get(user_id, entry_id=None):
        """This method is used to get a single or all entries"""
        if entry_id:
            # gets a single entry once the entry_id value is true
            db.query(
                "SELECT * FROM entries WHERE user_id=%s AND entry_id=%s",
                (user_id, entry_id)
            )
            entries = db.cur.fetchall()
            return entries
        else:
            # gets all entries once the entry_id value is false
            db.query(
                "SELECT * FROM entries WHERE user_id = %s", [user_id]
            )
            entry = db.cur.fetchall()
            return entry   

    @staticmethod
    def make_dict(entry_list):
        """This method creates a list of dictionary entries """
        entries = []
        for entry in entry_list:
            # creates empty dictionary
            new_dict = {}
            # updates the dictionary with the entry details
            new_dict.update({
                'entry_id': entry[0],
                'title': entry[2],
                'story': entry[3],
                'date_created': entry[4].strftime("%A, %d %B, %Y")
                })
            # appends the list with entry dictionaries
            entries.append(new_dict)
        return entries

    
