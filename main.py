import tweepy
import time
import pandas as pd
print("Running App.py")
pd.set_option('display.max_colwidth', 1000)

# api key
api_key = "bvslKyerdSERLQere64XilQYx"

# api secret key
api_secret_key = "2YB7CPzEWBQLFQRzy7xXjyxcPpbgarVj8617extbB4GQwRTTbC"
# access token
access_token = "1362198643474857985-u15tmUT3Dz6MxU2uxyE0mxRgc6R7dd"
# access token secret
access_token_secret = "Krl8jdTf1QU6ynG1TaVwRcI3GaLwpVEUtgXH10Cl5Sqi3"

# authorize the API Key
authentication = tweepy.OAuthHandler(api_key, api_secret_key)

# authorization to user's access token and access token secret
authentication.set_access_token(access_token, access_token_secret)

# call the api
api = tweepy.API(authentication, wait_on_rate_limit=True)



def get_related_tweets(text_query):
    # list to store tweets
    tweets_list = []
    # no of tweets
    count = 50
    try:
        # Pulling individual tweets from query
        for tweet in api.search(q=text_query, count=count):
            print(tweet.text)
            # Adding to list that contains all tweets
            tweets_list.append({'created_at': tweet.created_at,
                                'tweet_id': tweet.id,
                                'tweet_text': tweet.text})
        return pd.DataFrame.from_dict(tweets_list)

    except BaseException as e:
        print('failed on_status,', str(e))
        time.sleep(3)