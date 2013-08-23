from twython import Twython
from appdotnet import *
import yaml

config = yaml.load(open('app_config'))
debug = config.get('debug')

# twitter credentials
TWITTER_APP_TOKEN = config.get('twitter').get('app_token')
TWITTER_APP_SECRET = config.get('twitter').get('app_secret')
TWITTER_ACCESS_TOKEN = config.get('twitter').get('access_token')
TWITTER_ACCESS_SECRET = config.get('twitter').get('access_secret')

# app.net credentials
APP_NET_ACCESS_TOKEN = config.get('appdotnet').get('access_token')

# method to hit the twitter api and return the home timeline feed
def get_feed_twitter():
    
    if debug:
        print 'Feed Name: Twitter'
        print 'TWITTER_APP_TOKEN:' + TWITTER_APP_TOKEN
        print 'TWITTER_APP_SECRET:' + TWITTER_APP_SECRET
        print 'TWITTER_ACCESS_TOKEN: ' + TWITTER_ACCESS_TOKEN
        print 'TWITTER_ACCESS_SECRET: ' + TWITTER_ACCESS_SECRET

    twitter = Twython(TWITTER_APP_TOKEN, TWITTER_APP_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
    streamResults = twitter.get_home_timeline()

    if debug:
        for item in streamResults:
            print json.dumps(item, indent=4, separators=[',', ':'])

    return streamResults

# method to hit the app.net api and return the global stream feed
def get_feed_app_net():
    if debug:
        print 'Feed Name: App.net'
        print 'APP_NET_ACCESS_TOKEN: ' + APP_NET_ACCESS_TOKEN

    api = appdotnet(access_token=APP_NET_ACCESS_TOKEN)

    # get the globalStream and change the encoding to utf-8 from unicode
    streamResults = json.loads(api.getGlobalStream().encode('utf-8'))
    jsonResults = streamResults['data']

    if debug:
        print json.dumps(jsonResults, indent=4, separators=[',', ':'])

    return jsonResults