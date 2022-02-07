from dotenv import load_dotenv

import os
import tweepy
import requests

load_dotenv()

BLACK, YELLOW, GREEN = '\U00002B1B', '\U0001F7E8', '\U0001F7E9'

def get_pass():
    return os.getenv('PASS')

def tweet(text):
    client = tweepy.Client(
        bearer_token=os.getenv('BEARER_TOKEN'),
        consumer_key=os.getenv('CONSUMER_KEY'),
        consumer_secret=os.getenv('CONSUMER_SECRET'),
        access_token=os.getenv('BOT_ACCESS_TOKEN'),
        access_token_secret=os.getenv('BOT_ACCESS_TOKEN_SECRET'),
        return_type=requests.Response,
        wait_on_rate_limit=True
    )

    tweet = text
    response = client.create_tweet(text=tweet)
    # print(response)
if __name__ == "__main__":
    tweet(BLACK+YELLOW+GREEN)