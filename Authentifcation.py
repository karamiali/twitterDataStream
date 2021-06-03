from tweepy import OAuthHandler
import Conf


def getTwitterAuth():
    auth = OAuthHandler(Conf.consumer_key, Conf.consumer_secret)
    auth.set_access_token(Conf.access_token, Conf.access_token_secret)
    return auth
