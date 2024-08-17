from kafka import KafkaProducer, KafkaConsumer

# Kafka Producer configuration
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Produce a sample message
producer.send('data_topic', key=b'key', value=b'Sample data message')
producer.flush()

# Kafka Consumer configuration
consumer = KafkaConsumer('data_topic', bootstrap_servers='localhost:9092', auto_offset_reset='earliest')

# Consume and print messages
for message in consumer:
    print(f"Received message: {message.value.decode('utf-8')}")
