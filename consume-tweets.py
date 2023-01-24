from kafka_producer_consumer import kafka_consumer
from s3fs import S3FileSystem
import json
import os

BOOTSTRAP_SERVER = os.environ.get("BOOTSTRAP_SERVER")
TOPIC='AusOpen'

S3_ACCESS_KEY = os.environ.get("S3_ACCESS_KEY")
S3_SECRET_KEY = os.environ.get("S3_SECRET_KEY")

if __name__ == "__main__":
    print("consume")
    consumer = kafka_consumer(TOPIC, BOOTSTRAP_SERVER)
    # Create an S3FS object
    s3 = S3FileSystem(key=S3_ACCESS_KEY, secret=S3_SECRET_KEY)
    # Check if the S3 bucket exists
    if not s3.exists('kafka-tweet-bucket-dataalgo'):
        s3.mkdir('kafka-tweet-bucket-dataalgo')
    
    for tweet in consumer:
        print(tweet.value)
        with s3.open("s3://kafka-tweet-bucket-dataalgo/tweet_{}.json".format(list(tweet.value.keys())[0]), 'w') as file:
            json.dump(tweet.value, file)  
