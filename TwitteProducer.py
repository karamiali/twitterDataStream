from tweepy.streaming import StreamListener
from tweepy import Stream
from kafka import KafkaProducer
import Authentifcation
import Conf

producer = KafkaProducer(bootstrap_servers=Conf.zk_url)

topic_name = "twitterdata"
track_words = ['kardashian']


class produceListener(StreamListener):
    def on_data(self, raw_data):
        print(raw_data)
        producer.send(topic_name, str.encode(raw_data))
        return True

    def on_error(self, status_code):
        print(status_code)


if __name__ == "__main__":
    auth = Authentifcation.getTwitterAuth()
    listener = produceListener()
    stream = Stream(auth, listener)
    stream.filter(track=Conf.track_workds, languages=["fr"])
