import datetime
import json
import os
import re
import psycopg2 as dbapi2
from database import initialize_database, saveuser, savetweet, saveFavoriteUser
from flask import Flask, render_template, redirect, request
from flask.helpers import url_for
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home_page():
    now = datetime.now()
    day = now.strftime('%A')
    initialize_database(app.config['dsn'])
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

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/saveuser', methods=['POST'])
def save():
    saveuser(app.config['dsn'])
    return 'User is inserted'

@app.route('/savetweet', methods=['POST'])
def savetw():
	savetweet(app.config['dsn'])
	return 'Your tweet has been successfully posted'

@app.route('/saveFavoriteUser', methods=['POST'])
def savefavorites():
	saveFavoriteUser(app.config['dsn'])
	return 'Favorite user information is inserted'

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
