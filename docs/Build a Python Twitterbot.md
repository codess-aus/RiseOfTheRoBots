## How to Build a Python Twitterbot :robot: and deploy it to Heroku  

1. Setup a Twitter Account for your bot to use
2. Link that new Twitter account to a developer account by logging in at https://apps.twitter.com/ and entering the information for your new twitter-bot app.
3. Go over to the “Keys and Access Tokens” tab and copy the Consumer Key (API Key) and Consumer Secret (API Secret). Also, click the “Create my access token” button at the bottom of the page and copy the resulting Access Token and Access Token Secret. You will use these codes to make API requests on your own account’s behalf.

4. Open up your favorite text editor (I use VS Code) and create a new Python script called something like tweetbot.py 

This is the full tweetbot code for a bot that will respond when tweeted at if the tweet includes #riseoftherobots It will tweet back "Hi @*twitteruser* Live long and Prosper":

```python

import tweepy
import time
CONSUMER_KEY = 'replace with your key'
CONSUMER_SECRET = 'replace with your secret'
ACCESS_KEY = 'replace with your access key'
ACCESS_SECRET = 'replace with your access secret'

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
        print(str(mention.id) + ' - ' + mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#riseoftherobots' in mention.full_text.lower():
            print('found #riseoftherobots')
            print('responding back...')
            api.update_status('Hi ' '@' + mention.user.screen_name +
                    ' Live long and prosper', mention.id)

while True:
    reply_to_tweets()
    time.sleep(15)

```
5. Create a text file in the same directory called last_seen_id.txt in it 
6. Now, you can run that directly from your terminal with the command:

```
C:\Users\*username*\Documents\GitHub\RiseOfTheRoBots>python tweetbot.py
```
7. Or, we can set it up to run independantly of your workstation, i.e. in the cloud. The simplest way to do that for free is using a service called Heroku, where you will set-up an App - which is just a container that will hold your code and run it

Go to the website and setup a free account:

https://www.heroku.com/

![Image of Heroku](https://github.com/msandfor/RiseOfTheRoBots/blob/gh-pages/images/Herokusignup.PNG){:height="50%" width="50%"}


