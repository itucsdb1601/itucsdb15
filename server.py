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
from university import university as university
from directmessages import directmessages as directmessage
from comments import comments as comment
from events import activities as event
from favoriteevents import favoriteevents as favoriteevent
from favoriteTags import favoriteTags as favoritetag
from favoriteUni import favoriteUnis as favoriteuni


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

@app.route('/inituniversities')
def init_university():
    return university.initialize_universities(app.config['dsn'])


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
    return tag.savetag(app.config['dsn'])


@app.route('/directmessages_edit')
def directmessages_edit():
    return render_template('directmessages_edit.html')

@app.route('/directmessages')
def directmessages():
    return directmessage.directmessages_db(app.config['dsn'])

@app.route('/directmessages/delete/<deletedm>', methods=['GET', 'POST'])
def directmessages_delete(deletedm):
    return directmessage.directmessages_db_delete(app.config['dsn'],deletedm)


@app.route('/directmessages/update/<updatedm>/', methods=['GET', 'POST'])
def directmessages_update(updatedm):
    return directmessage.directmessages_db_update(app.config['dsn'],updatedm)

@app.route('/directmessages/update/<updatedm>/apply', methods=['GET', 'POST'])
def directmessage_apply(updatedm):
    return directmessage.directmessages_db_update_apply(app.config['dsn'],updatedm)

@app.route('/savedirectmessage', methods=['POST'])
def savedirectmessage():
    return directmessage.savedirectmessage(app.config['dsn'])


@app.route('/comments_edit')
def comments_edit():
    return render_template('comments_edit.html')

@app.route('/comments')
def comments():
    return comment.comments_db(app.config['dsn'])

@app.route('/comments/delete/<deletecomment>', methods=['GET', 'POST'])
def comments_delete(deletecomment):
    return comment.comments_db_delete(app.config['dsn'],deletecomment)


@app.route('/comments/update/<updatecomment>/', methods=['GET', 'POST'])
def comments_update(updatecomment):
    return comment.comments_db_update(app.config['dsn'],updatecomment)

@app.route('/comments/update/<updatecomment>/apply', methods=['GET', 'POST'])
def comments_apply(updatecomment):
    return comment.comments_db_update_apply(app.config['dsn'],updatecomment)

@app.route('/savecomment', methods=['POST'])
def savecomment():
    return comment.savecomment(app.config['dsn'])


@app.route('/events_edit')
def events_edit():
    return render_template('events_edit.html')

@app.route('/events')
def events():
    return event.events_db(app.config['dsn'])

@app.route('/events/delete/<deleteevent>', methods=['GET', 'POST'])
def events_delete(deleteevent):
    return event.events_db_delete(app.config['dsn'],deleteevent)


@app.route('/events/update/<updateevent>/', methods=['GET', 'POST'])
def events_update(updateevent):
    return event.events_db_update(app.config['dsn'],updateevent)

@app.route('/events/update/<updateevent>/apply', methods=['GET', 'POST'])
def events_apply(updateevent):
    return event.events_db_update_apply(app.config['dsn'],updateevent)

@app.route('/saveevent', methods=['POST'])
def saveevent():
    return event.saveevent(app.config['dsn'])

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
    return tweet.savetweet(app.config['dsn'])


@app.route('/activities_panel')
def activities_panel():
    return render_template('activities_panel.html')


@app.route('/favoritesPanel')
def favoritesPanel():
    return render_template('favoritesPanel.html')

@app.route('/favorites/initialize_favorites', methods=['GET', 'POST'])
def initialize_favorites():
        return favorite.initialize_favorites(app.config['dsn'])

@app.route('/favoritesPanel/favorites')
def favorites():
    return favorite.favorites_db(app.config['dsn'])


@app.route('/saveFavoriteUser', methods=['POST'])
def savefavorites():
    return favorite.saveFavoriteUser(app.config['dsn'])


@app.route('/favorites/delete/<deletefavorites>', methods=['GET', 'POST'])
def favorites_delete(deletefavorites):
    return favorite.favorites_db_delete(app.config['dsn'],deletefavorites)

@app.route('/favorites/update/<updatefavorites>/', methods=['GET', 'POST'])
def favorites_update(updatefavorites):
    return favorite.favorites_db_update(app.config['dsn'],updatefavorites)

@app.route('/favorites/update/<updatefavorites>/apply', methods=['GET', 'POST'])
def favorites_apply(updatefavorites):
    return favorite.favorites_db_update_apply(app.config['dsn'],updatefavorites)

@app.route('/favorites_edit')
def favorites_edit():
    return render_template('favorites_edit.html')


@app.route('/favoritesPanel/favoriteUnis')
def favoriteUnis():
    return favoriteuni.favoriteUnis_db(app.config['dsn'])

@app.route('/savefavoriteUnis', methods=['POST'])
def savefavoriteUni():
    return favoriteuni.savefavoriteUni(app.config['dsn'])


@app.route('/favoriteUnis/delete/<deletefavoriteUni>', methods=['GET', 'POST'])
def favoriteUni_delete(deletefavoriteUni):
    return favoriteuni.favoriteUnis_db_delete(app.config['dsn'],deletefavoriteUni)

@app.route('/favoriteUnis/update/<updatefavoriteUni>/', methods=['GET', 'POST'])
def favoriteUni_update(updatefavoriteUni):
    return favoriteuni.favoriteUnis_db_update(app.config['dsn'],updatefavoriteUni)

@app.route('/favoriteUnis/update/<updatefavoriteUni>/apply', methods=['GET', 'POST'])
def favoriteUnis_apply(updatefavoriteUni):
    return favoriteuni.favoriteUnis_db_update_apply(app.config['dsn'],updatefavoriteUni)

@app.route('/favoriteUnis_edit')
def favoriteUnis_edit():
    return render_template('favoriteUnis_edit.html')

@app.route('/favorites_tweet_edit')
def favorites_tweet_edit():
    return render_template('favorites_tweet_edit.html')

@app.route('/favoritesPanel/favoriteTags')
def favoriteTags():
    return favoritetag.favoriteTags_db(app.config['dsn'])

@app.route('/savefavoriteTags', methods=['POST'])
def savefavoriteTags():
    return favoritetag.savefavoriteTags(app.config['dsn'])


@app.route('/favoriteTags/delete/<deletefavoriteTag>', methods=['GET', 'POST'])
def favoriteTag_delete(deletefavoriteTag):
    return favoritetag.favoriteTags_db_delete(app.config['dsn'],deletefavoriteTag)

@app.route('/favoriteTags/update/<updatefavoriteTag>/', methods=['GET', 'POST'])
def favoriteTag_update(updatefavoriteTag):
    return favoritetag.favoriteTags_db_update(app.config['dsn'],updatefavoriteTag)

@app.route('/favoriteTags/update/<updatefavoriteTag>/apply', methods=['GET', 'POST'])
def favoriteTag_apply(updatefavoriteTag):
    return favoritetag.favoriteTags_db_update_apply(app.config['dsn'],updatefavoriteTag)
@app.route('/favoriteTags_edit')
def favoriteTags_edit():
    return render_template('favoriteTags_edit.html')


@app.route('/favoritesPanel/favoriteEvents')
def favoriteEvents():
    return favoriteevent.favoriteevents_db(app.config['dsn'])

@app.route('/savefavoriteEvents', methods=['POST'])
def savefavoriteEvents():
    return favoriteevent.savefavoriteEvents(app.config['dsn'])


@app.route('/favoriteEvents/delete/<deletefavoriteEvent>', methods=['GET', 'POST'])
def favoriteEvent_delete(deletefavoriteEvent):
    return favoriteevent.favoriteevents_db_delete(app.config['dsn'],deletefavoriteEvent)

@app.route('/favoriteEvents/update/<updatefavoriteEvent>/', methods=['GET', 'POST'])
def favoriteEvent_update(updatefavoriteEvent):
    return favoriteevent.favoriteevents_db_update(app.config['dsn'],updatefavoriteEvent)

@app.route('/favoriteEvents/update/<updatefavoriteEvent>/apply', methods=['GET', 'POST'])
def favoriteEvent_apply(updatefavoriteEvent):
    return favoriteevent.favoriteevents_db_update_apply(app.config['dsn'],updatefavoriteEvent)

@app.route('/favoriteEvents_edit')
def favoriteEvents_edit():
    return render_template('favoriteEvents_edit.html')


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
