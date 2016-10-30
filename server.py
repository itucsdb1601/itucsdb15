import datetime
import json
import os
import re

from database import initialize_database
from database import initialize_tweets
from database import initialize_followers
from flask import Flask, render_template, redirect
from flask.helpers import url_for
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home_page():
    now = datetime.now()
    day = now.strftime('%A')
    initialize_database(app.config['dsn'])
    initialize_tweets(app.config['dsn'])
    initialize_followers(app.config['dsn'])
    return render_template('home.html', day_name=day)


@app.route('/profiles')
def profiles():
    return render_template('profiles.html')

@app.route('/tweets')
def tweets():
    return render_template('tweets.html')

@app.route('/universities')
def universities():
    return render_template('universities.html')

@app.route('/favorites')
def favorites():
    return render_template('favorites.html')

@app.route('/followers')
def followers():
    return render_template('followers.html')

@app.route('/login')
def login():
    return render_template('login.html')


def get_elephantsql_dsn(vcap_services):
    """Returns the data source name for ElephantSQL."""
    parsed = json.loads(vcap_services)
    uri = parsed["elephantsql"][0]["credentials"]["uri"]
    match = re.match('postgres://(.*?):(.*?)@(.*?)(:(\d+))?/(.*)', uri)
    user, password, host, _, port, dbname = match.groups()
    dsn = """user='{}' password='{}' host='{}' port={}
             dbname='{}'""".format(user, password, host, port, dbname)
    return dsn



if __name__ == '__main__':

    VCAP_APP_PORT = os.getenv('VCAP_APP_PORT')
    if VCAP_APP_PORT is not None:
        port,debug = int(VCAP_APP_PORT),False
    else:
        port,debug = 5000, True

    VCAP_SERVICES = os.getenv('VCAP_SERVICES')
    if VCAP_SERVICES is not None:
        app.config['dsn'] = get_elephantsql_dsn(VCAP_SERVICES)
    else:
        app.config['dsn'] = """user='vagrant' password='vagrant'
                               host='localhost' port=5432 dbname='itucsdb'"""

    app.run(host='0.0.0.0', port=port, debug=debug)
