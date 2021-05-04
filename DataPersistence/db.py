import sqlite3
from kafka import KafkaProducer

# Kafka Producer to send database connection details
producer = KafkaProducer()


def get_db():
    conn = sqlite3.connect('./raw_data.db')
    try:
        conn.cursor()
        producer.send('database', b'Connection Successful')
        return conn
    except Exception as ex:
        producer.send('database', b'Connection Failed')
    return None


def close_db():
    db = get_db()
    db.close()
    producer.send('database', b'Connection Terminated')
    return


def test_connection(conn):
    try:
        conn.cursor()
        producer.send('database', b'Connection Successful')
    except Exception as ex:
        producer.send('database', b'Connection Failed')

