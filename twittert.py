import tweepy
import json
import time

# Replace with your Twitter API keys
consumer_key = "EbDQcqGfgdoaScMrnkfZTHLHm"
consumer_secret = "gYplFvB9gGwVkNeHiA1vO20t0M334FZGe8FBYFiukbqaw0PUyC"
bearer = "AAAAAAAAAAAAAAAAAAAAANsXuQEAAAAATSjbVW5gXWbkdiUW5rxgjptGGmk%3DpOhB4eBMU8hWlDIkyEWc2ZJjfwz4e8ePoPKBbAJC7eRQil7lko"
access_token = "1800955061226393601-V9MW5rLfRxAONJmygXf3uXC11ne06g"
access_token_secret = "RTbWaRVSAj6gSBbgUbhfCEDCt4nVWXWHNgCUqos5rO5lr"

# Authenticate to Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)


# Define the stocks for which you want tweets
stocks = [
    "HDFC Bank",
    "IRCTC",
    "Infosys",
    "ICICI Bank",
    "TCS",
    "Reliance Industries",
    "Hindustan Unilever",
    "Asian Paints",
    "Bajaj Finance",
    "Maruti Suzuki",
]

# Fetch tweets for each stock
tweets = {}
for stock in stocks:
    try:
        fetched_tweets = api.search_tweets(q=stock, count=100, lang="en")
        tweets[stock] = [tweet._json for tweet in fetched_tweets]
    except Exception as e:
        print(f"Error fetching tweets for {stock}: {e}")
        time.sleep(60)  # Wait for a minute before retrying

# Save the tweets to a JSON file
with open("tweets.json", "w") as f:
    json.dump(tweets, f)
