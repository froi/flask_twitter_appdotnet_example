from flask import Flask, render_template
import json
import yaml
import feeds

app = Flask(__name__)
config = yaml.load(open('app_config'))
debug = config.get('debug')

if debug:
    app.debug = True
    print 'debug is on:'

# gets both feeds at once in a page
@app.route('/feeds/')
def get_feeds():
    twitterResults = feeds.get_feed_twitter()
    appNetResults = feeds.get_feed_app_net()

    return render_template('feeds.html', twitter_feed=twitterResults, app_net_feed=appNetResults)

# gets only the twitter feed
@app.route('/feeds/twitter')
def get_twitter():
    results = feeds.get_feed_twitter()
    return render_template('feed.html', feed=results, feed_name='Twitter')

# get only the app.net feed
@app.route('/feeds/appdotnet')
def get_app_net():
    results = feeds.get_feed_app_net()
    return render_template('feed.html', feed=results, feed_name='App.net')

if __name__ == '__main__':
    app.run()