import tweepy
import tweepy.errors
from givemeback import *

# Replace with your actual Twitter API credentials
API_KEY = credentials['API_KEY']
API_KEY_SECRET = credentials['API_KEY_SECRET']
ACCESS_TOKEN = credentials['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = credentials['ACCESS_TOKEN_SECRET']
BEARER_TOKEN = credentials['BEARER_TOKEN']

def post(text: str="Hello world this is a test !"):
    # # Authenticate with the Twitter API
    # auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
    # auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # # Create an API object
    # api = tweepy.API(auth)

    # # Try posting the tweet
    # try:
    #     api.update_status(status=text)
    #     print("Tweet posted successfully!")
    # except Exception as e:
    #     print("Error occurred while posting the tweet: " + str(e))
    # print(type(BEARER_TOKEN))

    # client = tweepy.Client(bearer_token=BEARER_TOKEN)
    # auth = tweepy.OAuth1UserHandler(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    client = tweepy.Client(consumer_key=API_KEY,
                           consumer_secret=API_KEY_SECRET,
                           access_token=ACCESS_TOKEN,
                           access_token_secret=ACCESS_TOKEN_SECRET)
    # api = tweepy.API(auth)
    try:
        # api.update_status(status=text)
        r= client.create_tweet(text=text)
        print("Tweet sent !")
        print(r)
    except tweepy.errors.Forbidden as e:
        print(f'Tweepy error Forbidden : {e}')
    except Exception as e:
        print(e)
        print(type(e))

def test():
    print(c['TEST'])