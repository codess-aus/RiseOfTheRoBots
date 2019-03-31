## How to Build a Python Twitterbot :robot: and deploy it to Heroku  

1. Setup a Twitter Account for your bot to use
2. Link that new Twitter account to a developer account by logging in at https://apps.twitter.com/ and entering the information for your new twitter-bot app.
3. Go over to the “Keys and Access Tokens” tab and copy the Consumer Key (API Key) and Consumer Secret (API Secret). Also, click the “Create my access token” button at the bottom of the page and copy the resulting Access Token and Access Token Secret. You will use these codes to make API requests on your own account’s behalf.

Open up your favorite text editor (I use VS Code) and create a new Python script called something like tweetbot.py 

Copy in the following code:

```python

import tweepy
import time

print('this is my twitter bot')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('retrieving and replying to tweets...')
    # DEV NOTE: use 1060651988453654528 for testing.
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    # NOTE: We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#riseoftherobots' in mention.full_text.lower():
            print('found #riseoftherobots', flush=True)
            print('responding back...', flush=True)
            api.update_status('Hi ' '@' + mention.user.screen_name +
                    ' Live long and prosper', mention.id)

while True:
    reply_to_tweets()
    time.sleep(15)

```

