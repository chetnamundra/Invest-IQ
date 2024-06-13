import tweepy
import json
import time

# Replace with your Twitter API v2 Bearer Token
bearer_token = "YOUR_BEARER_TOKEN"
bearer_token = "AAAAAAAAAAAAAAAAAAAAANsXuQEAAAAATSjbVW5gXWbkdiUW5rxgjptGGmk%3DpOhB4eBMU8hWlDIkyEWc2ZJjfwz4e8ePoPKBbAJC7eRQil7lko"


# Authenticate to Twitter API v2
client = tweepy.Client(bearer_token=bearer_token, wait_on_rate_limit=True)

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
        query = f"{stock} -is:retweet lang:en"
        fetched_tweets = client.search_recent_tweets(query=query, max_results=100)
        tweets[stock] = [tweet.data for tweet in fetched_tweets.data]
    except Exception as e:
        print(f"Error fetching tweets for {stock}: {e}")
        time.sleep(60)  # Wait for a minute before retrying

# Save the tweets to a JSON file
with open("tweets_v2.json", "w") as f:
    json.dump(tweets, f, indent=4)

print("Tweets fetched and saved to tweets_v2.json")
