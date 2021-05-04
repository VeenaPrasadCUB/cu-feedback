from kafka import KafkaConsumer


class MessageConsumer:

    consumer = KafkaConsumer('database')

    def check_messages(self):
        for message in self.consumer:
            print(message)

