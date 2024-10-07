import tweepy
import tweepy.errors
from givemeback import *

# Replace with your actual Twitter API credentials
API_KEY = credentials['API_KEY']
API_KEY_SECRET = credentials['API_KEY_SECRET']
ACCESS_TOKEN = credentials['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = credentials['ACCESS_TOKEN_SECRET']
BEARER_TOKEN = credentials['BEARER_TOKEN']

def post(text: str, dry_run: bool=False) -> None:

    client = tweepy.Client(consumer_key=API_KEY,
                           consumer_secret=API_KEY_SECRET,
                           access_token=ACCESS_TOKEN,
                           access_token_secret=ACCESS_TOKEN_SECRET)
    
    try: client.create_tweet(text=text)
    except tweepy.errors.Forbidden as e: print(f'Tweepy error Forbidden : {e}')
    except Exception as e: print(f'Exception : {e}')