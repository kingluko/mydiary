import os
import psycopg2
from config import Config
import sys


class DbConnection():
    """Initializes connection to the database and executes queries"""
    def __init__(self):
        # load credentials from environment
        database = os.getenv('DATABASE_NAME')
        user = os.getenv('DATABASE_USER')
        password = os.getenv('DATABASE_PASSWORD')
        host = os.getenv('DATABASE_HOST')
        # uses credentials from the environment to connect to the database
        self.conn = psycopg2.connect(
            f"""dbname={database}
                user={user}
                password={password}
                host={host}""")
        # saves every database execution aumatically
        self.conn.autocommit = True
        self.cur = self.conn.cursor()

    # performs database queries
    def query(self, *args):
        self.cur.execute(*args)

    # closes connection with the database
    def close(self):
        self.cur.close()
        self.conn.close()

    def create_tables(self):
        self.query("""CREATE TABLE IF NOT EXISTS users(id serial PRIMARY KEY,
                     name VARCHAR(100), email VARCHAR(100),
                     username VARCHAR(30), password VARCHAR(100));""")
        self.query("""CREATE TABLE IF NOT EXISTS entries(entry_id serial,
                     user_id INTEGER REFERENCES users(id), title VARCHAR(200),
                     story TEXT, date_created TIMESTAMP DEFAULT NOW());""")
