import datetime
import json
import os
import re
import psycopg2 as dbapi2
from database import initialize_database
from flask import Flask, render_template, redirect, request
from flask.helpers import url_for
from datetime import datetime
from Profile import Profile as profile
from Hobby import Hobby as hobby
from Interaction_c import Interaction_c
from Communication import Communication as communication
from tags import tags as tag
from tweets import tweets as tweet
from favorites import favorites as favorite
from favoritestweet import favoritestweet as favtweet
from university import university as university
from unisports import unisports as unisports
from academics import academics as academics

app = Flask(__name__)


@app.route('/')
def home_page():
    now = datetime.now()
    day = now.strftime('%A')
    #initialize_database(app.config['dsn'])
    return render_template('home.html', day_name=day)

@app.route('/initdb')
def init():
    return initialize_database(app.config['dsn'])


@app.route('/followers/search', methods=['POST'])
def searchM():
    return Interaction_c.search(app.config['dsn'])


@app.route('/followers/follow', methods=['POST'])
def insertM():
    Interaction_c.follow(app.config['dsn'])
    return render_template('followers.html')


@app.route('/following/search_following', methods=['POST'])
def searchM_following():
    return Interaction_c.search_following(app.config['dsn'])



@app.route('/following/follow_following', methods=['POST'])
def insertM_following():
    Interaction_c.follow_following(app.config['dsn'])
    return render_template('following.html')

@app.route('/blocked/search_blocked', methods=['POST'])
def searchM_blocked():
    return Interaction_c.search_blocked(app.config['dsn'])

@app.route('/blocked/follow_blocked', methods=['POST'])
def insertM_blocked():
    Interaction_c.follow_blocked(app.config['dsn'])
    return render_template('blocked.html')

@app.route('/following/check2', methods=['POST'])
def checkM2():
    return Interaction_c.check2(app.config['dsn'])

@app.route('/blocked/check3', methods=['POST'])
def checkM3():
    return Interaction_c.check3(app.config['dsn'])

@app.route('/following/find', methods=['POST'])
def find_following():
    return Interaction_c.find(app.config['dsn'])

@app.route('/followers/unfollow', methods=['POST'])
def unfollowM():
    Interaction_c.unfollow(app.config['dsn'])
    return render_template('followers.html')

@app.route('/followers/update', methods=['POST'])
def updateM():
    return Interaction_c.update(app.config['dsn'])

@app.route('/following/unfollow_following', methods=['POST'])
def unfollowM_following():
    Interaction_c.unfollow_following(app.config['dsn'])
    return render_template('following.html')

@app.route('/following/update_following', methods=['POST'])
def updateM_following():
    return Interaction_c.update_following(app.config['dsn'])

@app.route('/blocked/unfollow_blocked', methods=['POST'])
def unfollowM_blocked():
    Interaction_c.unfollow_blocked(app.config['dsn'])
    return render_template('blocked.html')

@app.route('/blocked/update_blocked', methods=['POST'])
def updateM_blocked():
    return Interaction_c.update_blocked(app.config['dsn'])

@app.route('/followers')
def followers():
    return render_template('followers.html')

@app.route('/search_display')
def search_display():
    return render_template('search_display.html')

@app.route('/interaction')
def interaction():
    return render_template('interaction.html')

@app.route('/blocked')
def blocked():
    return render_template('blocked.html')

@app.route('/following')
def following():
    return render_template('following.html')

@app.route('/followers/check', methods=['POST'])
def checkM():
    return Interaction_c.check(app.config['dsn'])

@app.route('/profiles')
def profiles():
    return profile.users_page_db(app.config['dsn'])

@app.route('/profiles/delete/<deleteuserlogin>', methods=['GET', 'POST'])
def profile_delete(deleteuserlogin):
    return profile.users_page_db_delete(app.config['dsn'],deleteuserlogin)

@app.route('/profiles/update/<updateuserlogin>/', methods=['GET', 'POST'])
def profile_update(updateuserlogin):
    return profile.users_page_db_update(app.config['dsn'],updateuserlogin)

@app.route('/profiles/update/<updateuserlogin>/apply', methods=['GET', 'POST'])
def profile_update_apply(updateuserlogin):
    return profile.users_page_db_update_apply(app.config['dsn'],updateuserlogin)

@app.route('/profiles/update_communication/', methods=['GET', 'POST'])
def communication_edit():
    return communication.users_page_db_communication_information_select(app.config['dsn'])

@app.route('/profiles/update_communication/select',methods=['GET'])
def communication_edit_select():
    return communication.users_page_db_communication_information_select(app.config['dsn'])

@app.route('/profiles/update_communication/delete', methods=['GET','POST'])
def communication_edit_delete():
    return communication.users_page_db_communication_information_delete(app.config['dsn'])

@app.route('/profiles/update_communication/apply', methods=['GET','POST'])
def communication_edit_insert_or_update():
    return communication.users_page_db_communication_information_apply(app.config['dsn'])

@app.route('/profiles/update_hobbies/', methods=['GET', 'POST'])
def hobbies_edit():
        return hobby.users_page_db_hobby_information_select(app.config['dsn'])

@app.route('/profiles/update_hobbies/select',methods=['GET'])
def hobbies_edit_select():
        return hobby.users_page_db_hobby_information_select(app.config['dsn'])

@app.route('/profiles/update_hobbies/apply', methods=['GET', 'POST'])
def hobbies_edit_insert_or_update():
        return hobby.users_page_db_hobby_information_apply(app.config['dsn'])

@app.route('/profiles/update_hobbies/delete', methods=['GET', 'POST'])
def hobbies_edit_delete():
        return hobby.users_page_db_hobby_information_delete(app.config['dsn'])



@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/saveuser', methods=['POST'])
def save():
    profile.saveuser(app.config['dsn'])
    return render_template('login.html')


@app.route('/tag_edit')
def tags_edit():
    return render_template('tags_edit.html')

@app.route('/tags')
def tags():
    return tag.tags_db(app.config['dsn'])

@app.route('/tags/delete/<deletetag>', methods=['GET', 'POST'])
def tag_delete(deletetag):
    return tag.tags_db_delete(app.config['dsn'],deletetag)


@app.route('/tags/update/<updatetag>/', methods=['GET', 'POST'])
def tag_update(updatetag):
    return tag.tags_db_update(app.config['dsn'],updatetag)

@app.route('/tags/update/<updatetag>/apply', methods=['GET', 'POST'])
def tags_apply(updatetag):
    return tag.tags_db_update_apply(app.config['dsn'],updatetag)

@app.route('/savettag', methods=['POST'])
def savetag():
    tag.savetag(app.config['dsn'])
    return 'Your tag has been successfully posted'
    
@app.route('/universities')
def universities():
    return university.universities_page(app.config['dsn'])

@app.route('/universities/delete/<deleteuniversities>', methods=['GET', 'POST'])
def universities_delete(deleteuniversities):
    return university.universities_page_delete(app.config['dsn'])

@app.route('/universities/update/<updateuniversities>', methods=['GET', 'POST'])
def universities_update(updateuniversities):
    return university.universities_page_update(app.config['dsn'], updateuniversities)

@app.route('/universities/update/<updateuniversities>/apply', methods=['GET', 'POST'])
def universities_update_apply(updateuniversities):
    return university.universities_page_update_apply(app.config['dsn'], updateuniversities)

@app.route('/adduniversity')
def adduniversity():
    return render_template('universities_add.html')

@app.route('/universities_edit')
def universities_edit():
    return render_template('universities_edit.html')

@app.route('/academics')
def academics():
    return academics.academics_page(app.config['dsn'])

@app.route('/academics/delete/<deleteacademicinfo>', methods=['GET', 'POST'])
def academics_delete(deleteacademicinfo):
    return academics.academics_page_delete(app.config['dsn'], deleteacademicinfo)

@app.route('/academics/update/<updateacademicinfo>', methods=['GET', 'POST'])
def academics_update(updateacademicinfo):
    return academics.academics_page_update(app.config['dsn'], updateacademicinfo)

@app.route('/academics/update/<updateacademicinfo>/apply', methods=['GET', 'POST'])
def academics_update_apply(updateacademicinfo):
    return academics.academics_page_update_apply(app.config['dsn'], updateacademicinfo)

@app.route('/addacademics')
def addacademics():
    return render_template('academics_add.html')

@app.route('/academics_edit')
def academics_edit():
    return render_template('academics_edit.html')

@app.route('/unisports')
def unisports():
    return unisports.unisports_page(app.config['dsn'])

@app.route('/unisports/delete/<deleteuniteam>'), methods=['GET', 'POST'])
def unisports_delete(deleteuniteam):
    return unisports.unisports_page_delete(app.config['dsn'], deleteuniteam)

@app.route('/unisports/update/<updateuniteam>', methods=['GET', 'POST'])
def unisports_update(updateuniteam):
    return unisports.unisports_page_update(app.config['dsn'], updateuniteam)

@app.route('/unisports/update/<updateuniteam>/apply', methods=['GET', 'POST'])
def unisports_update_apply(updateuniteam):
    return unisports.unisports_page_update_apply(app.config['dsn'], updateuniteam)

@app.route('/addunisports')
def addunisports():
    return render_template('unisports_add.html')

@app.route('/unisports_edit')
def unisports_edit():
    return render_template('unsports_edit.html')

@app.route('/tweets')
def tweets():
    return tweet.tweets_db(app.config['dsn'])

@app.route('/tweets/delete/<deleteTweet>', methods=['GET', 'POST'])
def tweet_delete(deleteTweet):
    return tweet.tweets_db_delete(app.config['dsn'],deleteTweet)

@app.route('/tweets/initialize_tweets', methods=['GET', 'POST'])
def initialize_tweets():
        return tweet.initialize_tweets(app.config['dsn'])

@app.route('/tweets/update/<updateTweet>/', methods=['GET', 'POST'])
def tweet_update(updateTweet):
    return tweet.tweets_db_update(app.config['dsn'],updateTweet)

@app.route('/tweets/update/<updateTweet>/apply', methods=['GET', 'POST'])
def tweets_apply(updateTweet):
    return tweet.tweets_db_update_apply(app.config['dsn'],updateTweet)

@app.route('/tweet_edit')
def tweet_edit():
    return render_template('tweet_edit.html')

@app.route('/savetweet', methods=['POST'])
def savetw():
    tweet.savetweet(app.config['dsn'])
    return 'Your tweet has been successfully posted'

@app.route('/favorites')
def favorites():
    return favorite.favorites_db(app.config['dsn'])

@app.route('/saveFavoriteUser', methods=['POST'])
def savefavorites():
	favorite.saveFavoriteUser(app.config['dsn'])
	return 'Favorite user information is inserted'

@app.route('/favorites/delete/<deletefavorites>', methods=['GET', 'POST'])
def favorites_delete(deletefavorites):
    return favorite.favorites_db_delete(app.config['dsn'],deletefavorites)

@app.route('/favorites/initialize_favorites', methods=['GET', 'POST'])
def initialize_favorites():
        return favorite.initialize_favorites(app.config['dsn'])

@app.route('/favorites/update/<updatefavorites>/', methods=['GET', 'POST'])
def favorites_update(updatefavorites):
    return favorite.favorites_db_update(app.config['dsn'],updatefavorites)

@app.route('/favorites/update/<updatefavorites>/apply', methods=['GET', 'POST'])
def favorites_apply(updatefavorites):
    return favorite.favorites_db_update_apply(app.config['dsn'],updatefavorites)

@app.route('/favorites_edit')
def favorites_edit():
    return render_template('favorites_edit.html')

@app.route('/favorites_tweet')
def favorites_tweet():
    return favtweet.favoritestweet_db(app.config['dsn'])

@app.route('/saveFavoriteTweet', methods=['POST'])
def savefavoritestweet():
    favtweet.saveFavoriteTweet(app.config['dsn'])
    return 'Favorite tweet information is inserted'

@app.route('/favorites_tweet/delete/<deletefavoritestweet>', methods=['GET', 'POST'])
def favorites_tweet_delete(deletefavoritestweet):
    return favtweet.favoritestweet_db_delete(app.config['dsn'],deletefavoritestweet)

@app.route('/favorites_tweet/update/<updatefavoritestweet>/', methods=['GET', 'POST'])
def favorites_tweet_update(updatefavoritestweet):
    return favtweet.favoritestweet_db_update(app.config['dsn'],updatefavoritestweet)

@app.route('/favorites_tweet/update/<updatefavoritestweet>/apply', methods=['GET', 'POST'])
def favoritestweet_apply(updatefavoritestweet):
    return favtweet.favoritestweet_db_update_apply(app.config['dsn'],updatefavoritestweet)

@app.route('/favorites_tweet_edit')
def favorites_tweet_edit():
    return render_template('favorites_tweet_edit.html')

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
