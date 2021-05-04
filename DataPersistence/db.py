import sqlite3


class Database:
    conn = None

    def start_db(self):
        self.conn = sqlite3.connect('./raw_data.db')
        if self.conn:
            return True
        else:
            return False

    def get_db(self):
        if not self.conn:
            self.conn = sqlite3.connect('./raw_data.db')
        try:
            self.conn.cursor()
            return self.conn
        except Exception as ex:
            return None

    def close_db(self):
        self.conn.close()
        self.conn = None
        return

    def test_connection(self):
        try:
            self.conn.cursor()
            return True
        except Exception as ex:
            return False
