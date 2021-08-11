from time import sleep
from kafka import KafkaProducer
from json import dumps
import random
import settings as env
# producer creates a KafkaProducer object for the running docker container
# we map to :9092, the container port assigned to kafka

producer = KafkaProducer(
    bootstrap_servers=['0.0.0.0:9092'],
    value_serializer=lambda m: dumps(m).encode('utf-8')
)
USERS = 20

print("=== PRODUCER ===")
# We use the producer on the 'topic1' topic
for i in range(1, USERS):
    otp_code = ''.join(str(x) for x in random.sample(range(10), 4))
    print(otp_code)
    producer.send('otpCodes', value=otp_code)
    sleep(1.00)
