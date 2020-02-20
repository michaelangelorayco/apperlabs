import json

import boto3
from faker import Faker


firehose = boto3.client('firehose')
fake = Faker()

delivery_stream_name = '<input your delivery stream here>'

customer_data = {}
while True:
    customer_data['name'] = fake.name()
    customer_data['location'] = fake.address()
    customer_data['job'] = fake.job()
    response = firehose.put_record(
        DeliveryStreamName=delivery_stream_name,
        Record={'Data': json.dumps(customer_data)})
    print(f"Sending Data to Kinesis: {customer_data}")
    
