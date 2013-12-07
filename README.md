flask_twitter_appdotnet_example
===============================

A simple Flask app that consumes the Twitter and App.net APIs. This is meant as an example / introduction to Flask for the Puerto Rico Python Interest Group.
You need to register as a developer @ both services in order to obtain the credentials needed to run this app.

More info can be found at:
* https://dev.twitter.com/
* http://developers.app.net/

Libraries
=========
Open requirements.txt for a listing of most libraries.

Additional library used: Python-App.net-API-Wrapper. This can be found on GitHub @ https://github.com/simondlr/Python-App.net-API-Wrapper.

Files of note
=============
* app_config: In this file contains all the app configuration including the Twitter and App.net authentication tokens.
* flask_twitter_appNet.py: Flask app. Here you will find the defined routes.
* feeds.py: here you will find the calls to the Twitter and App.net APIs.
* requirements.txt: list of dependencies.
* templates/ : template directory
  * feeds.html: main template. Displays both Twitter and App.net feeds.
  * feed.html: template that displays the queried feed by the flask app.

Usage
=============
Once downloaded and all dependencies are install run:
> python flask_twitter_appNet.py

This will run the flask app at it's default settings.
To access the app in your web browser go to any of the following:
- http://localhost:5000/feeds/
- http://localhost:5000/feeds/twitter
- http://localhost:5000/feeds/appdotnet




[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/froi/flask_twitter_appdotnet_example/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

