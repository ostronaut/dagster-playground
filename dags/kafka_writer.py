from dagster import job, op, schedule, repository
from kafka import KafkaProducer
from json import dumps
import random

@op
def send_random_number_to_kafka(context):
    producer = KafkaProducer(
        bootstrap_servers=["kafka:9092"],
        value_serializer=lambda x: dumps(x).encode('utf-8')
    )

    data = {'number' : random.randint(0, 1000)}
    future = producer.send("random_numbers", value=data)
    record_metadata = future.get(timeout=10)
    context.log.info(
        f"topic: {record_metadata.topic}; "
        "partition: {record_metadata.partition}; "
        "offset: {record_metadata.offset}"
    )

@job
def test_kafka_produser():
    send_random_number_to_kafka()


@schedule(
    cron_schedule="*/1 * * * *",
    job=test_kafka_produser,
    execution_timezone="utc",
)
def test_kafka_produser_schedule():
    pass

@repository
def test_kafka_produser_repository():
    return [test_kafka_produser, test_kafka_produser_schedule]
