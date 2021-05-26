from tweepy.streaming import StreamListener
from tweepy import Stream
import authentifcation
# from kafka import KafkaProducer

# producer = KafkaProducer(bootstrap_servers='192.168.1.21:9092, 192.168.1.21:9093')

topic_name = "twitterdata"
track_words = ['kardashian']


class produceListener(StreamListener):
    def on_data(self, raw_data):
        print(raw_data)
        return True

    def on_error(self, status_code):
        print(status_code)


if __name__ == "__main__":
    auth = authentifcation.getTwitterAuth()
    listener = produceListener()
    stream = Stream(auth, listener)
    stream.filter(track=track_words)