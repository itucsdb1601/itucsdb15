import datetime
import json
import os
import re
import psycopg2 as dbapi2
<<<<<<< HEAD
from database import initialize_database, saveFavoriteUser, saveuser, users_page_db, users_page_db_delete, users_page_db_update, users_page_db_update_apply, favorites_db, favorites_db_delete, favorites_db_update favorites_db_update_applyusers_page_db_update_apply, search, follow, unfollow, update
=======
from database import initialize_database, saveuser, savetweet, saveFavoriteUser
>>>>>>> 72451323770cee9de3c5a2d8fc3a1441ffa8b894
from flask import Flask, render_template, redirect, request
from flask.helpers import url_for
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home_page():
    now = datetime.now()
    day = now.strftime('%A')
    #initialize_database(app.config['dsn'])
    return render_template('home.html', day_name=day)


@app.route('/followers/unfollow/<deletefollower>/', methods=['GET','POST'])
def unfollowM(deletefollower):
    return unfollow(app.config['dsn'],deletefollower)


@app.route('/followers/search/<searchfollower>/', methods=['GET','POST'])
def searchM(searchfollower):
    return search(app.config['dsn'], searchfollower)


@app.route('/followers/follow/<insertfollower>/', methods=['GET','POST'])
def followM(insertfollower):
    return follow(app.config['dsn'],insertfollower)


@app.route('/followers/update/<updatefollower>/)', methods=['POST'])
def updateM(updatefollower):
    return update(app.config['dsn'],updatefollower)

@app.route('/profiles')
def profiles():
    return users_page_db(app.config['dsn'])

@app.route('/profiles/delete/<deleteuserlogin>', methods=['GET', 'POST'])
def profile_delete(deleteuserlogin):
    return users_page_db_delete(app.config['dsn'],deleteuserlogin)

@app.route('/profiles/update/<updateuserlogin>/', methods=['GET', 'POST'])
def profile_update(updateuserlogin):
    return users_page_db_update(app.config['dsn'],updateuserlogin)

@app.route('/profiles/update/<updateuserlogin>/apply', methods=['GET', 'POST'])
def profile_update_apply(updateuserlogin):
    return users_page_db_update_apply(app.config['dsn'],updateuserlogin)

@app.route('/tweets')
def tweets():
    return render_template('tweets.html')

@app.route('/universities')
def universities():
    return render_template('universities.html')

@app.route('/universities/delete/<deleteuni_name>', methods=['GET', 'POST'])
def universities_delete(deleteuni_name):
    return university_users_page_db_delete(app.config['dsn'],deleteuni_name)

@app.route('/universities/update/<updateuni_name>/', methods=['GET','POST'])
def universities_update(updateuni_name):
    return university_users_page_db_update(app.config['dsn'],updateuni_name)

@app.route('/universities/update/<updateuserlogin>/apply', methods=['GET','POST'])
def universities_update_apply(updateuni_name):
    return universities_page_db_update_apply(app.config['dsn'],updateuni_name)


@app.route('/favorites')
def favorites():
    return render_template('favorites.html')

@app.route('/favorites/delete/<deletefavorites>', methods=['GET', 'POST'])
def favorites_delete(deletefavorites):
    return favorites_db_delete(app.config['dsn'],deletefavorites)

@app.route('/favorites/update/<updatefavorites>/', methods=['GET', 'POST'])
def favorites_update(updatefavorites):
    return favorites_db_update(app.config['dsn'],updatefavorites)

@app.route('/favorites/update/<updatefavorites>/apply', methods=['GET', 'POST'])
def favorites_update_apply(updatefavorites):
    return favorites_db_update_apply(app.config['dsn'],updatefavorites)	
	
	@app.route('/saveFavoriteUser', methods=['POST'])

def savefavorites():

	saveFavoriteUser(app.config['dsn'])
	return 'Favorite user information is inserted'

@app.route('/followers')
def followers():
    return render_template('followers.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/about')
def about():
    return render_template('about.html')

<<<<<<< HEAD
@app.route('/saveuser', methods=['GET','POST'])
def save():
    return saveuser(app.config['dsn'])
=======
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
>>>>>>> 72451323770cee9de3c5a2d8fc3a1441ffa8b894

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
