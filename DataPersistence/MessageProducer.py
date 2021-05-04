from kafka import KafkaProducer
from db import Database


class MessageProducer:
    producer = KafkaProducer('database')

    def send_db_update(self):
        started = Database.start_db()
        if started:
            self.producer.send('database', 'Connection Successful')
        else:
            self.producer.send('database', 'Connection Failed')
