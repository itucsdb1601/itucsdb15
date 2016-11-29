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
        query = """CREATE TABLE IF NOT EXISTS FOLLOWERS (following_id serial primary key,follower_name VARCHAR(200) ,follower_email VARCHAR(200))"""
        cursor.execute(query)
        query = """insert into FOLLOWERS(follower_name,follower_email) values('c','d')"""
        cursor.execute(query)
        connection.commit();
        return 'Value is inserted'

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


def follow(config,insertfollower):
    follower_name = None
    follower_email = None

    if request.method == 'GET':
        follower_name= request.form['name_text']
        print(user_name)
        follower_email = request.form['email_text']
        print(user_surname)

        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO FOLLOWERS(follower_name,follower_email) VALUES (%s,%s);"""
            cursor.execute(query,(follower_name,follower_email))
            connection.commit();
            return redirect(url_for('follower'))



def unfollow(config,deletefollower):
    follower_name = None
    follower_email = None

    if request.method == 'POST':
        follower_name2= request.form['name_text']
        print(user_name)
        follower_email2 = request.form['email_text']
        print(user_surname)

        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """DELETE FROM FOLLOWERS WHERE follower_name = follower_name2 AND follower_email = follower_email2;"""
            cursor.execute(query,(follower_name,follower_email))
            connection.commit();
            return redirect(url_for('followers'))


def search(config,searchfollower):
    follower_name = None
    follower_email = None

    if request.method == 'POST':
        follower_name= request.form['name_text']
        print(user_name)
        follower_email = request.form['email_text']
        print(user_surname)

        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """SELECT follower_name,follower_email FROM FOLLOWERS;"""
            cursor.execute(query,(follower_name,follower_email))
            connection.commit();
            return redirect(url_for('followers'))

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

def update(config,updatefollower):
    follower_name = None
    follower_email = None

    if request.method == 'POST':
        follower_name2= request.form['name_text']
        print(user_name)
        follower_email2 = request.form['email_text']
        print(user_surname)

        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """UPDATE FOLLOWERS SET follower_name='DFDSF',follower_email='DFDF' WHERE follower_name = follower_name2 ,follower_email = follower_email2;"""
            cursor.execute(query,(follower_name,follower_email))
            connection.commit();
            return redirect(url_for('followers'))

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

