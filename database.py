import json
import os
import psycopg2 as dbapi2
import re
from flask import Flask, request, render_template, redirect
from flask.helpers import url_for
from flask import Flask, request, render_template
from Profile import Profile as profile

app = Flask(__name__)


def initialize_database(config):
    with dbapi2.connect(config) as connection:
        cursor = connection.cursor()
        profile.initialize_profiles(config)
        initialize_followers(config)
        query = """DROP TABLE IF EXISTS TWEETS"""
        cursor.execute(query)
        query = """DROP TABLE IF EXISTS FAVORITES"""
        cursor.execute(query)
        query = """CREATE TABLE IF NOT EXISTS TWEETS (tweet_id serial primary key, user_logName VARCHAR(60) NOT NULL , tweet_input VARCHAR(200) NOT NULL)"""
        cursor.execute(query)
        query = """CREATE TABLE IF NOT EXISTS FAVORITES (favorite_id serial primary key, user_name VARCHAR(20) NOT NULL, user_surname VARCHAR(20) NOT NULL,user_loginname VARCHAR(30) UNIQUE NOT NULL, user_email VARCHAR(30) NOT NULL)"""
        cursor.execute(query)
        connection.commit();
        return 'tables are created <a href="http://localhost:5000">Home</a>'

def initialize_tweets(config):
    with dbapi2.connect(config) as connection:
        cursor = connection.cursor()

        query = """CREATE TABLE IF NOT EXISTS TWEETS (tweet_id serial primary key,user_id INTEGER NOT NULL, user_tweet VARCHAR(200))"""
        cursor.execute(query)

        query = """insert into TWEETS(user_id, user_tweet) values(1,'first tweet for user 1 was added')"""
        cursor.execute(query)
        connection.commit();
        return 'Tweet was inserted'


def initialize_followers(config):
    with dbapi2.connect(config) as connection:
        cursor = connection.cursor()

        query = """DROP TABLE IF EXISTS FOLLOWERS"""
        cursor.execute(query)
        connection.commit();

        query = """DROP TABLE IF EXISTS FOLLOWING"""
        cursor.execute(query)
        connection.commit();

        query = """DROP TABLE IF EXISTS BLOCKED"""
        cursor.execute(query)
        connection.commit();


        query = """DROP TABLE IF EXISTS DATE"""
        cursor.execute(query)
        connection.commit();

        query = """DROP TABLE IF EXISTS BLOCKED_TYPE"""
        cursor.execute(query)
        connection.commit();


        query = """ CREATE TABLE IF NOT EXISTS FOLLOWERS (follower_id serial primary key,follower_name VARCHAR(200)  ,follower_email VARCHAR(200),follower_username VARCHAR(200),follower_date VARCHAR(200))"""
        cursor.execute(query)
        connection.commit();

        query = """ CREATE TABLE IF NOT EXISTS FOLLOWING (following_id serial primary key,following_name VARCHAR(200) ,following_email VARCHAR(200),following_username VARCHAR(200),following_date VARCHAR(200))"""
        cursor.execute(query)
        connection.commit();

        query = """ CREATE TABLE IF NOT EXISTS BLOCKED (blocked_id serial primary key,blocked_name VARCHAR(200) ,blocked_email VARCHAR(200),blocked_username VARCHAR(200),blocked_date VARCHAR(200),blocked_type VARCHAR(200))"""
        cursor.execute(query)
        connection.commit();

        query = """ CREATE TABLE IF NOT EXISTS DATE (date_id serial primary key, date_loginname VARCHAR(200), date_ VARCHAR(200))"""
        cursor.execute(query)
        connection.commit();

        query = """ CREATE TABLE IF NOT EXISTS BLOCKED_TYPE (type_id serial primary key, type VARCHAR(200))"""
        cursor.execute(query)
        connection.commit();


        query = """ insert into BLOCKED_TYPE(type) values('inappropriate content')"""
        cursor.execute(query)
        connection.commit();

        query = """ insert into BLOCKED_TYPE(type) values('fake profile')"""
        cursor.execute(query)
        connection.commit();

        query = """ insert into BLOCKED_TYPE(type) values('distracting message content')"""
        cursor.execute(query)
        connection.commit();

        query = """ insert into BLOCKED_TYPE(type) values('violent profile')"""
        cursor.execute(query)
        connection.commit();

        #print(rows)
        #for row in rows:
        #    now = datetime.datetime.now()
        #    query = """insert into DATE(user_name,date) values(%s,%s)"""
        #    cursor.execute(query,(row[0],now.year))
        #    connection.commit();
        return 'sdfjlksfjlsk'



def check(config):
    user_loginname = None
    if request.method == 'POST':
        user_loginname = request.form['user_name_text']
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            try:
                query = """INSERT INTO FOLLOWERS(follower_name,follower_email,follower_username)
                        SELECT user_name,user_email,user_loginname FROM USER_LOGIN where user_loginname = '%s'""" %(user_loginname)
                cursor.execute(query)
                connection.commit();
                return render_template('followers.html')
            except:
                return "there is no such entry in the user table"

def check3(config):
    user_loginname = None
    if request.method == 'POST':
        user_loginname = request.form['user_name_text3']
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            try:
                query = """INSERT INTO BLOCKED(blocked_name,blocked_email,blocked_username)
                        SELECT user_name,user_email,user_loginname FROM USER_LOGIN where user_loginname = '%s'""" %(user_loginname)
                cursor.execute(query)
                connection.commit();
                print(query)
                return render_template('blocked.html')
            except:
                return "there is no such entry in the user table"

def search(config):
    follower_name = None
    follower_email = None
    if request.method == 'POST':
        follower_name = request.form['follower_name_text']
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """SELECT follower_name,follower_email,follower_username,follower_date FROM FOLLOWERS where follower_username = %s;"""
            try:
                cursor.execute(query,follower_name)
                return render_template('search_display.html',followers=cursor)
            except:
                return "there is no such entry in the table"

def search_following(config):
    following_name = None
    following_email = None
    if request.method == 'POST':
        following_name = request.form['follower_name_text']
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """SELECT following_name,following_email,following_username,following_date FROM FOLLOWING where following_username = %s ;"""
            try:
                cursor.execute(query,following_name)
                return render_template('search_display.html',following=cursor)
            except:
                return "there is no such entry in the table"

def search_blocked(config):
    blocked_name = None
    blocked_email = None
    if request.method == 'POST':
        blocked_name = request.form['follower_name_text']
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """SELECT blocked_name,blocked_email,blocked_username,blocked_date FROM BLOCKED where blocked_username = %s ;"""
            try:
                cursor.execute(query,blocked_name)
                return render_template('search_display.html',blocked=cursor)
            except:
                return "there is no such entry in the table"
def check2(config):
    user_loginname = None
    if request.method == 'POST':
        user_loginname = request.form['user_name_text2']
        with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    query = """INSERT INTO FOLLOWING(following_name,following_email,following_username)
                        SELECT user_name,user_email,user_loginname FROM USER_LOGIN where user_loginname = '%s'""" %(user_loginname)
                    cursor.execute(query)
                    connection.commit();
                    print(query)
                    return render_template('following.html')
                except:
                    return "there is no such entry in the user table"

def unfollow(config):

    if request.method == 'POST':
        follower_username = request.form['follower_name_text']
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM FOLLOWERS WHERE follower_username = %s"
            try:
                cursor.execute(query,follower_username)
                connection.commit();
                # return redirect(url_for('followers'))
                return redirect(url_for('followers'))
            except:
                return "There is no such entry"

def unfollow_following(config):


    if request.method == 'POST':
        following_username = request.form['follower_name_text']
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM FOLLOWING WHERE following_username = %s"
            try:
                cursor.execute(query,follower_username)
                connection.commit();
                # return redirect(url_for('followers'))
                return redirect(url_for('following'))
            except:
                return "There is no such entry"

def unfollow_blocked(config):

    if request.method == 'POST':
        following_username = request.form['follower_name_text']
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM BLOCKED WHERE blocked_username = %s"
            try:
                cursor.execute(query,follower_username)
                connection.commit();
                # return redirect(url_for('followers'))
                return redirect(url_for('blocked'))
            except:
                return "There is no such entry"

def follow(config):
    if request.method == 'POST':
        user_loginname = request.form['follower_name_text']
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()

            try:
                query = """INSERT INTO FOLLOWERS(follower_name,follower_email,follower_username)
                    SELECT user_name,user_email,user_loginname FROM USER_LOGIN where user_loginname = '%s'""" %(user_loginname)
                cursor.execute(query)
                connection.commit();

                    #query = """INSERT INTO FOLLOWERS(follower_date)
                    #SELECT date_ from DATE where date_loginname =' %s'""" %(user_loginname)
                    #cursor.execute(query)
                    #connection.commit();
                return render_template('followers.html')
            except:
                return "there is no such entry in the user table"


def follow_following(config):
    following_name = None
    following_email = None
    if request.method == 'POST':
        user_loginname = request.form['follower_name_text']
        print(follower_email)
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            #query = """insert into FOLLOWING(following_name,following_email,following_username,following_date) (SELECT user_name,user_email,user_loginname FROM USER_LOGIN where user_name = %s AND user_email = %s,select date_ from DATE where date_loginname = following_name)"""

            query = """INSERT INTO FOLLOWING(following_name,following_email,following_username)
                SELECT user_name,user_email,user_loginname FROM USER_LOGIN where user_loginname = '%s'""" %(user_loginname)
            cursor.execute(query)
            connection.commit();
            # return redirect(url_for('followers'))
            return 'Following is inserted'


def follow_blocked(config):
    blocked_name = None
    blocked_email = None
    if request.method == 'POST':
        user_loginname = request.form['follower_name_text']
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            #query = """insert into BLOCKED(blocked_name,blocked_email,blocked_username,blocked_date) (SELECT user_name,user_email,user_loginname FROM USER_LOGIN where user_name = %s AND user_email = %s,select date_ from DATE where date_loginname = blocked_name)"""
            query = """INSERT INTO BLOCKED(blocked_name,blocked_email,blocked_username)
                SELECT user_name,user_email,user_loginname FROM USER_LOGIN where user_loginname = '%s'""" %(user_loginname)
            cursor.execute(query)
            connection.commit();
            # return redirect(url_for('followers'))
            return 'blocked is inserted'

def update(config):
    follower_name = None
    follower_email = None

    if request.method == 'POST':
        follower_name = request.form['follower_name_text']
        follower_name_new = request.form['follower_name_text_new']
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """UPDATE FOLLOWERS SET follower_name= %s  where follower_name = %s ;"""
            cursor.execute(query,(follower_name_new,follower_name))
            connection.commit();
            return redirect(url_for('followers'))


def update_following(config):
    following_name = None
    following_email = None

    if request.method == 'POST':
        following_name = request.form['follower_email_text']
        following_name_new = request.form['follower_name_text_new']
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """UPDATE FOLLOWING SET following_name_new= %s  where follower_name = %s ;"""
            cursor.execute(query,(following_name_new,following_name))
            connection.commit();
            return redirect(url_for('following'))


def update_blocked(config):
    blocked_name = None
    blocked_email = None

    if request.method == 'POST':
        blocked_name = request.form['follower_email_text']
        blocked_name_new = request.form['follower_name_text_new']
        blocked_type = request.form['blocked_type']
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """UPDATE BLOCKED SET blocked_name_new= %s, blocked_type = %s where blocked_name = %s ;"""
            cursor.execute(query,(blocked_name_new,blocked_name,blocked_type))
            connection.commit();
            return redirect(url_for('blocked'))
def savetweet(config):
    new_tweet = None
    user_login = None
    if request.method == 'POST':
        new_tweet = request.form['tweet_text']
        print(new_tweet)
        user_login = request.form['username_text']
        print(user_login)
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO TWEETS (user_logName, tweet_input) VALUES (%s, %s)"""
            cursor.execute(query, (user_login, new_tweet))
            connection.commit();
            return 'Your tweet has been successfully posted'


def saveFavoriteUser(config):
    user_name = None
    user_surname = None
    user_loginname = None
    user_email = None
    if request.method == 'POST':
        user_name= request.form['fname_text']
        print(user_name)
        user_surname = request.form['fsurname_text']
        print(user_surname)
        user_loginname = request.form['floginname_text']
        print(user_loginname)
        user_email = request.form['femail_text']
        print(user_email)
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO FAVORITES(user_loginname,user_name,user_surname,user_email) VALUES (%s,%s,%s,%s);"""
            cursor.execute(query,(user_loginname,user_name,user_surname,user_email))
            connection.commit();
            return 'Favorite user information is inserted'





        query = """CREATE TABLE IF NOT EXISTS UNIVERSITY_USERS (
                    uni_id serial primary key,
                    user_id INTEGER NOT NULL,
                    uni_name VARCHAR(50) NOT NULL
                    )"""
        cursor.execute(query)
        query = """INSERT INTO UNIVERSITY_USERS (user_id,uni_name) VALUES ('1','Istanbul Technical University')"""
        cursor.execute(query)
        connection.commit();
        return 'universities table is inserted to store user-university data'


def tweets_db(config):
    with dbapi2.connect(config) as connection:
        if request.method == 'GET':
            cursor = connection.cursor()
            query="SELECT user_loginname,tweet from tweets"
            cursor.execute(query)
            print(cursor)
            return render_template('tweets.html',thistweet=cursor)
def tweets_db_delete(config,deleteUserTweet):
    with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query="DELETE FROM tweets where user_loginname = %s"
            cursor.execute(query, (deleteUserTweet,))
            connection.commit()
            return redirect(url_for('tweets'))
def tweets_db_update(config,updateUserTweet):
     with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query="""SELECT user_loginname from tweets where user_loginname = '%s'""" % (updateUserTweet)
            cursor.execute(query)
            connection.commit()
            return render_template('tweet_update.html',logins=cursor)  #bunun için bir tweet_update html i gerekecek
def tweet_page_db_update_apply(config,updateUserTweet):
    with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            new_tweet = request.form['tweet_text']
            print(new_tweet)
            query="""UPDATE tweets set tweet ='%s' where user_loginname = '%s'""" % (new_ntweet,updateUserTweet)
            cursor.execute(query)
            connection.commit()
            return redirect(url_for('tweets'))



def universities_page_db_delete(config,deleteuni_name):
    with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query="DELETE FROM UNIVERITY_USERS where uni_name = %s"
            cursor.execute(query, (deleteuni_name))
            connection.commit()
            return redirect(url_for('universities'))

def universities_page_db_update(config,updateuni_name):
     with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query="""SELECT uni_name from UNIVERSITIY_USERS where uni_name = '%s'""" % (updateuni_name)
            cursor.execute(query)
            connection.commit()
            return render_template('universities_edit.html',universities=cursor)
def universities_page_db_update_apply(config,updateuni_name):
    with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            new_uni = request.form['name']
            print(new_uni)
            query="""UPDATE university_users set uni_name ='%s' where uni_name= '%s'""" % (new_name,updateuni_name)
            cursor.execute(query)
            connection.commit()
            return redirect(url_for('universities'))


def saveFavoriteUser(config):
    user_name = None
    user_surname = None
    user_loginname = None
    user_email = None
    if request.method == 'POST':
        user_name= request.form['fname_text']
        print(user_name)
        user_surname = request.form['fsurname_text']
        print(user_surname)
        user_loginname = request.form['floginname_text']
        print(user_loginname)
        user_email = request.form['femail_text']
        print(user_email)
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO FAVORITES(user_loginname,user_name,user_surname,user_email) VALUES (%s,%s,%s,%s)"""
            cursor.execute(query,(user_loginname,user_name,user_surname,user_email))
            connection.commit();
            return 'Favorite user information is inserted'

def favorites_db(config):
    with dbapi2.connect(config) as connection:
        if request.method == 'GET':
            cursor = connection.cursor()
            query="SELECT user_loginname,user_name,user_surname,user_email from favorites"
            cursor.execute(query)
            print(cursor)
            return render_template('favorites.html',favorites=cursor)
def favorites_db_delete(config,deleteufavorites):
    with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query="DELETE FROM favorites where user_loginname = %s"
            cursor.execute(query, (deletefavorites,))
            connection.commit()
            return redirect(url_for('favorites'))
def favorites_db_update(config,updateuserlogin):
     with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query="""SELECT user_loginname from favorites where user_loginname = '%s'""" % (updatefavorites)
            cursor.execute(query)
            connection.commit()
            return render_template('favorites_edit.html',logins=cursor)
def favorites_db_update_apply(config,updateuserlogin):
    with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            new_name = request.form['name']
            print(new_name)
            query="""UPDATE favorites set user_loginname ='%s' where user_loginname = '%s'""" % (new_name,updatefavorites)
            cursor.execute(query)
            connection.commit()
            return redirect(url_for('favorites'))

