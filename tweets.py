import json
import os
import psycopg2 as dbapi2
import re
from flask import Flask, request, render_template, redirect
from flask.helpers import url_for

app = Flask(__name__)

class tweets:


    def initialize_tweets(config):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """DROP TABLE IF EXISTS TWEETS CASCADE;"""
            cursor.execute(query)
            query = """DROP TABLE IF EXISTS TAGS CASCADE;"""
            cursor.execute(query)
            query = """CREATE TABLE IF NOT EXISTS TWEETS
             (tweet_id SERIAL,
             user_logName VARCHAR(60) UNIQUE NOT NULL ,
             tweet_input VARCHAR(200) UNIQUE NOT NULL,
             tweet_category VARCHAR(100) NOT NULL,
             PRIMARY KEY(tweet_id , user_logName)) """
            cursor.execute(query)
            query = """INSERT INTO TWEETS (user_logName, tweet_input, tweet_category) VALUES ('songul', 'first tweet! #first', 'daily')"""
            cursor.execute(query)
            query = """CREATE TABLE IF NOT EXISTS TAGS
             (user_logname VARCHAR(20) UNIQUE PRIMARY KEY,
             tweet_input VARCHAR(200) NOT NULL,
             tag_id serial,
             tag_input VARCHAR(50) NOT NULL,
             tag_category VARCHAR(100) NOT NULL,
             FOREIGN KEY(user_logname) REFERENCES TWEETS(user_logName))"""
            cursor.execute(query)
            query = """INSERT INTO TAGS (user_logname, tweet_input, tag_input, tag_category) VALUES ('songul','first tweet! #first' , 'first' , 'daily')"""
            cursor.execute(query)
            connection.commit();
            return 'Tables inserted'


    def savetweet(config):
        new_tweet = None
        user_login = None
        new_category = None
        if request.method == 'POST':
            new_tweet = request.form['tweet_text']
            print(new_tweet)
            user_login = request.form['username_text']
            print(user_login)
            new_category = request.form['category_text']
            print(new_category)
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                query = """INSERT INTO TWEETS (user_logName, tweet_input, tweet_category) VALUES (%s, %s, %s)"""
                cursor.execute(query, (user_login, new_tweet, new_category))
                connection.commit();
                return redirect(url_for('tweet_edit'))


    def tweets_db(config):
        with dbapi2.connect(config) as connection:
            if request.method == 'GET':
                cursor = connection.cursor()
                query = "SELECT user_logName,tweet_input,tweet_category from tweets"
                cursor.execute(query)
                connection.commit();
                return render_template('tweets.html', tweets_list=cursor)


    def tweets_db_delete(config, deleteTweet):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM tweets where user_logName = %s"
            cursor.execute(query, (deleteTweet,))
            connection.commit();
            return redirect(url_for('tweets'))

    def tweets_db_update(config, updateTweet):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """SELECT tweet_input from tweets where user_logName = '%s'""" % (updateTweet)
            cursor.execute(query)
            connection.commit();
            return render_template('tweet_update.html', tweet_updates=cursor)


    def tweets_db_update_apply(config, updateTweet):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            new_tweet = request.form['tweet']
            query = """UPDATE tweets set tweet_input ='%s' where user_logName = '%s'""" % (new_tweet, updateTweet)
            cursor.execute(query)
            connection.commit();
            return redirect(url_for('tweets'))






