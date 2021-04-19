import sqlite3


def get_db():
    conn = sqlite3.connect('raw_data.db')
    return conn


def close_db():
    db = get_db()
    db.close()
    return


def test_connection(conn):
    try:
        conn.cursor()
        print("Connected to Database")
    except Exception as ex:
        print("Failed to Connect to Database")

