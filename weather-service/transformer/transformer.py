import os
import time
from confluent_kafka import Consumer, KafkaError
import json

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
    consumer_group = LOCATION+"Consumer"
    consumer = Consumer({"bootstrap.servers": KAFKA_HOST, "group.id": consumer_group, "auto.offset.reset": "latest"})
    topic = topic = "weather_" + LOCATION
    consumer.subscribe([topic,])
    try:
        while True:
            msg = consumer.poll(timeout=1.0)  # Poll for message (timeout in seconds)
            if msg is None:
                continue  # No message this time
            if msg.error():
                print(f"❌ Error: {msg.error()}")
                continue

            # Message received
            print(f"✅ Received message: {msg.value().decode('utf-8')}")

            # If it's JSON, decode it
            try:
                data = json.loads(msg.value())
                print(f"🔍 Parsed JSON: {data}")
            except json.JSONDecodeError:
                print("⚠️ Not a valid JSON message")

    except KeyboardInterrupt:
        print("👋 Stopping consumer...")

    finally:
        # Always close the consumer on exit
        consumer.close()
