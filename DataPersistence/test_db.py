import unittest
import sqlite3


class TestDatabase(unittest.TestCase):


    def test_db_connection(self):
        conn = sqlite3.connect('./raw_data.db')
        try:
            conn.cursor()
            self.assertTrue(True, 'DB Connection Successful')
        except Exception as ex:
            self.assertTrue(False, 'DB Connection Failed')

