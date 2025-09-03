import os
import time, datetime
from confluent_kafka import Producer


LOCATION_KEY="LOCATION"
# Optional delivery callback
def delivery_report(err, msg):
    if err is not None:
        print(f"❌ Message delivery failed: {err}")
    else:
        print(f"✅ Message delivered to {msg.topic()} [{msg.partition()}]")


if __name__=="__main__":
    time.sleep(30)
    LOCATION = os.getenv(LOCATION_KEY)
    KAFKA_HOST = "kafka:9092" # Or the address you want
    producer = Producer({"bootstrap.servers": KAFKA_HOST})
    topic = "testTopic"
    while True:
        MESSAGE = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        ENCODED_MESSAGE = MESSAGE.encode("utf-8")
        try:
            producer.produce(topic=topic, key=LOCATION, value=ENCODED_MESSAGE, on_delivery=delivery_report)
            producer.flush()
        except Exception as ex:
            print("Exception happened :",ex)
        time.sleep(3)
