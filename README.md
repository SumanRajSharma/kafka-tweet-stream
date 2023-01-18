# kafka-tweet-stream

## Project Description
This project is designed to stream tweets containing certain keywords or hashtags, publish them to a Kafka topic, and then consume the tweets from the topic and store them in an S3 bucket. The project uses the Twitter API for streaming tweets, Apache Kafka for message queueing, and Amazon S3 for storage.

## Prerequisites
Before running this project, you will need to have the following:

- A Twitter developer account and a valid bearer token for accessing the Twitter API
- A Kafka cluster running on a bootstrap server
- An Amazon S3 bucket and access key and secret for storing the tweets

## Project Structure
- tweet_stream.py: Stream tweets based on given hashtag and send it to a kafka topic
- kafka_producer_consumer.py: Kafka producer and consumer implementation
- consume_tweet.py: Consume tweets from the kafka topic and store it in S3 bucket
- docker-compose.yml: Docker Compose file to run the project
- Dockerfile: Docker file to create the image
- requirements.txt: Required python packages

## Architecture
```
                                                   +-------------+
                                                   | Tweet Stream|
                                                   +-----+-------+
                                                         |
                                                         |
                                                         |
                                                   +-----+----------+
                                                   |  Kafka Producer|
                                                   +-----+----------+
                                                         |
                                                         |
                                                         |
                                                   +-----+------+
                                                   |   Kafka    |
                                                   +-----+------+
                                                         |
                                                         |
                                                         |
                                                   +-----+----------+
                                                   | Kafka Consumer |
                                                   +-----+----------+
                                                         |
                                                         |
                                                         |
                                                   +-----+---------+
                                                   |   S3 Bucket   |
                                                   +---------------+

```

## How to Run
1. Make sure you have all the prerequisites mentioned above.
2. Clone the repository and navigate to the project directory.
3. Create a .env file in the project directory and add the following environment variables:
   - BEARER_TOKEN: Your Twitter bearer token
   - BOOTSTRAP_SERVER: The URL of your Kafka bootstrap server
   - AWS_ACCESS_KEY_ID: Your Amazon S3 access key
   - AWS_SECRET_ACCESS_KEY: Your Amazon S3 secret access key
   - S3_BUCKET: The name of your S3 bucket
4. Run docker-compose up in your terminal to start the services.
5. The tweets will be streamed, published to the Kafka topic, consumed and stored in the S3 bucket.

## About Zookeeper
Apache Kafka uses Zookeeper as a coordination service to manage the Kafka cluster. Zookeeper is responsible for maintaining configuration information, naming, providing distributed synchronization, and group services. It is used to track status of Kafka brokers, topics and partitions. Zookeeper is a centralized service that provides a distributed configuration service, synchronization service and naming registry for distributed systems.

## Setup
1. Create a virtual environment
   ```
   virtualenv venv
   source venv/bin/activate
   ```
2. Install the required packages
   ```
   pip install -r requirements.txt
   ```
3. Run Zookeeper and Kafka
   ```
   docker-compose up zookeeper kafka
   ```
4. Run the producer
   ```
   docker-compose up producer
   ```
5. Run the consumer
   ```
   docker-compose up consumer
   ```

## Note
- Make sure you have the correct version of docker and docker-compose installed.
- In this project we are using wurstmeister/zookeeper and wurstmeister/kafka as base images for zookeeper and kafka respectively.
- s3fs is used to mount s3 bucket to the container and access it.
- It is assumed that you have kafka cluster up and running.
- In case you face any issues related to the kafka, please refer to the official documentation of Kafka: https://kafka.apache.org/documentation/
- In case you face any issues related to the zookeeper, please refer to the official documentation of zookeeper: https://zookeeper.apache.org/doc/r3.5.9/

## Output
The tweets will be stored in the specified S3 bucket.

## Troubleshooting
- In case you are facing issues related to the kafka or zookeeper, please refer to their official documentation
- If you are not seeing any logs, try running docker-compose logs -f
- If you are getting s3fs: command not found make sure you have s3fs installed in your system

