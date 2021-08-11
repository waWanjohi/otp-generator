import africastalking
import settings as env


"""
ASSUMPTIONS:
1. The producer is from the app-auth service
2. The message and receipient will be coming from the producer
"""

# Initialize SDK
username = env.USERNAME
api_key = env.API_KEY
africastalking.initialize(username, api_key)


# Initialize a service e.g. SMS
sms = africastalking.SMS


""" You can send a message synchronously ...
response = sms.send("Hello Message!", ["+2547xxxxxxxx"])
print(response)
"""


def send_sms(code, receipient):
    """ 
    Or asynchronously
    """
    def on_finish(error, response):
        if error is not None:
            raise error
        print(f'Message sent to :: {response}')
    msg = f'Your OTP Code is {code}'
    sms.send(f'{msg}', [receipient], callback=on_finish)
