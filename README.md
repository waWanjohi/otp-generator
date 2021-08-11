# An OTP Code generator with Kafka and AfricasTalking SMS API

## Prerequisites
The following should be installed:
1. Docker
2. Python
3. Python virtualenv
4. An account on [AfricasTalking](africastalking.com).


## Setting up
1. Setup python virtual environment:

```bash
virtualenv venv
```
2. Install dependencies:

```bash
source venv/bin/activate && pip install -r requirements.txt
```

3. Create docker container:

```bash
 docker-compose -f docker-compose.yml up -d
 ```

 4. Setup your [AfricasTalking](africastalking.com) credentials:

 ```bash
 mv .env.example .env
 ```
 Edit appropriately

 5. Create a Kafka Topic called ```otpCodes``` (this is important):

 ```bash
 ./scripts/create.sh -n otpCodes -c kafka-tmc
 ```

 6. Now run the producer.py then consumer.py on separate terminals respectively. Happy coding :)