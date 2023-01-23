from kafka import KafkaProducer, KafkaConsumer
from json import loads, dumps

def kafka_producer(BOOTSTRAP_SERVER):
    producer = KafkaProducer(bootstrap_servers=[BOOTSTRAP_SERVER], value_serializer=lambda x: dumps(x).encode('utf-8'))
    return producer

def kafka_consumer(topic, BOOTSTRAP_SERVER):
    print(BOOTSTRAP_SERVER)
    consumer = KafkaConsumer(topic, bootstrap_servers=[BOOTSTRAP_SERVER], value_deserializer=lambda x: loads(x.decode('utf-8')))
    return consumer