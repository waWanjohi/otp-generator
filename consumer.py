from kafka import KafkaConsumer
import json
from send_sms import send_sms as send

consumer = KafkaConsumer(
    'otpCodes',
    bootstrap_servers=[' 0.0.0.0:9092'],
    auto_offset_reset='latest',
    enable_auto_commit=True,  # Acknowledges that they've read the message
    group_id='tmc-auth-otp-codes',

    # Important for extracting specific value from a ConsumerRecord
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

""" 
Sample ConsumerRecord |=> value_deserializer allows for something like consumer_obj.value
    consumer_obj = ConsumerRecord(
            topic='otpCodes', 
            partition=0, 
            offset=68, 
            timestamp=1628688594689, 
            timestamp_type=0, 
            key=None, 
            value=b'{"From Producer:": 39}', 
            headers=[], 
            checksum=None, 
            serialized_key_size=-1, 
            serialized_value_size=22,
            serialized_header_size=-1
        )
"""

RECEIVER = "+254773812611"

print("Listening ...")
for message in consumer:
    receiver = RECEIVER
    otp_code = f'{message.value}'
    print(f'GOT:: {message.value}')
    print(f'Sending to +254773812611:: ')
    send(code=otp_code, receipient=receiver)
    print("Done!")
