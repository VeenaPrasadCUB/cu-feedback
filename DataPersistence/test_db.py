import unittest
import sqlite3
from db import Database


class TestDatabase(unittest.TestCase):

    def test_db_connection(self):
        db = Database()
        started = db.start_db()
        self.assertTrue(started, 'DB Connection Successful')
