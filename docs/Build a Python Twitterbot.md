## How to Build a Python Twitterbot and deploy it to Heroku :robot: 

1. Setup a Twitter Account for your bot to use
2. Link that new Twitter account to a developer account by logging in at https://apps.twitter.com/ and entering the information for your new twitter-bot app.
3. Go over to the “Keys and Access Tokens” tab and copy the Consumer Key (API Key) and Consumer Secret (API Secret). Also, click the “Create my access token” button at the bottom of the page and copy the resulting Access Token and Access Token Secret. You will use these codes to make API requests on your own account’s behalf.

Open up your favorite text editor and create a new Python script called something like tweetbot.py. Copy in the following code:
import tweepy

*CONSUMER_KEY = 'replace with your key'*

*CONSUMER_SECRET = 'replace with your secret'*

*ACCESS_KEY = 'replace with your access key'*

*ACCESS_SECRET = 'replace with your access secret'*

*auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)*

*auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)*

*api = tweepy.API(auth)*

*api.update_status("Hello World!")*

