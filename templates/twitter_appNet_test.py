from twython import Twython
import json
from appdotnet import *
import yaml

config = yaml.load(open('app_config'))
debug = config.get('debug')

if debug:
    print 'debug is on:'

# twitter credentials
TWITTER_APP_TOKEN = config.get('twitter').get('app_token')
TWITTER_APP_SECRET = config.get('twitter').get('app_secret')
TWITTER_ACCESS_TOKEN = config.get('twitter').get('access_token')
TWITTER_ACCESS_SECRET = config.get('twitter').get('access_secret')

# app.net credentials
APP_NET_ACCESS_TOKEN = config.get('appdotnet').get('access_token')

def get_feed_twitter():
    feed_name = 'Twitter'
    if debug:
        print 'TWITTER_APP_TOKEN:' + TWITTER_APP_TOKEN
        print 'TWITTER_APP_SECRET:' + TWITTER_APP_SECRET
        print 'TWITTER_ACCESS_TOKEN: ' + TWITTER_ACCESS_TOKEN
        print 'TWITTER_ACCESS_SECRET: ' + TWITTER_ACCESS_SECRET

    twitter = Twython(TWITTER_APP_TOKEN, TWITTER_APP_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
    
    searchResults = twitter.get_home_timeline()

    if debug:
        for item in searchResults:
            print item

def get_feed_app_Net():
    feed_name = 'App.Net'
    if debug:
        print 'APP_NET_ACCESS_TOKEN: ' + APP_NET_ACCESS_TOKEN
    scope = ['messages']
    api = appdotnet(access_token=APP_NET_ACCESS_TOKEN, messages)

    searchResults = api.getUserStream()
    jsonResults = json.loads(searchResults.encode('utf-8'))

    if debug:
        help(jsonResults[0])
if __name__ == '__main__':
    #get_feed_twitter()
    get_feed_app_Net()