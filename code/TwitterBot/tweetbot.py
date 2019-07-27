import tweepy
import time

# Simple version deployed from your local machine
# CONSUMER_KEY = 'replace with your key'
# CONSUMER_SECRET = 'replace with your secret'
# ACCESS_KEY = 'replace with your access key'
# ACCESS_SECRET = 'replace with your access secret'

# If you deploy from GitHub you won't want to expose your keys publicly, so need to use Env Vars
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_KEY = os.environ['ACCESS_KEY']
ACCESS_SECRET = os.environ['ACCESS_SECRET']

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
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id,tweet_mode='extended')
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







