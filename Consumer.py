from kafka import KafkaConsumer
import Conf

topic_name = "twitterdata"

consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=[Conf.zk_url],
    auto_offset_reset='latest',
    enable_auto_commit=True,
    auto_commit_interval_ms=5000,
    fetch_max_bytes=128,
    max_poll_records=100
)

for message in consumer:
    value = message.value
    print(value)
