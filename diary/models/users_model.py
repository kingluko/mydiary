from passlib.hash import sha256_crypt
from diary.models.db import DbConnection
from diary.models.entries_model import Entries
from diary.models.mail import send_email
import time
from apscheduler.schedulers.background import BackgroundScheduler

sched = BackgroundScheduler()

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

    @staticmethod
    def user_details(user_id):
        """This method return the user details"""
        db.query(
            "SELECT * FROM users WHERE id = %s", [user_id]
        )
        details = db.cur.fetchall()
        entries = Entries.get(user_id)
        display_details = {
            'name': details[0][1],
            'email': details[0][2],
            'username': details[0][3],
            'total_entries': len(entries),
            'reminder': details[0][5]
            }
        return display_details

    @staticmethod
    def add_reminder(user_id, reminder):
        """This method adds an reminder notification to the profile"""
        db.query(
           "UPDATE users SET reminder=%s WHERE id=%s",
           (reminder, user_id)
           )

    @staticmethod
    @sched.scheduled_job('interval', hours=24)
    def schedule_email():
        db.query("SELECT * FROM users WHERE reminder='true'")
        users = db.cur.fetchall()
        for user in users:
            email = str(list(user)[2])
            send_email(email)
    sched.start()
