import tweepy
from config import consumer_key, consumer_secret, access_token, access_token_secret
import dummy

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)


def home_timeline(use_dummy=False):
    if use_dummy:
        return dummy.text
    public_tweets = api.home_timeline()
    out = []
    for tweet in public_tweets:
        print(tweet.text)
        out.append(tweet.text)
    return out


if __name__ == "__main__":
    home_timeline()
