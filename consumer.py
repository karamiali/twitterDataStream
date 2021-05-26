from kafka import KafkaConsumer

topic_name = "twitterdata"

consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=['192.168.1.21:9092', '192.168.1.21:9093'],
    auto_offset_reset='latest',
    enable_auto_commit=True,
    auto_commit_interval_ms=5000,
    fetch_max_bytes=128,
    max_poll_records=100
)

for message in consumer:
    value = message.value
    print(value)
