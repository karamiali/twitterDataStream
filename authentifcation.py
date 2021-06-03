from tweepy import OAuthHandler
import conf


def getTwitterAuth():
    auth = OAuthHandler(conf.consumer_key, conf.consumer_secret)
    auth.set_access_token(conf.access_token, conf.access_token_secret)
    return auth
