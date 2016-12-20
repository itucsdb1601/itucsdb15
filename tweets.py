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
            query = """CREATE TABLE IF NOT EXISTS TWEETS (
            tweet_id serial unique,
            user_logname VARCHAR(60) not null,
            tweet_input VARCHAR(200) unique not null,
            date date default current_date,
            tweet_category VARCHAR(100) not null,
            primary key(tweet_id, user_logname),
            foreign key(user_logname) references user_login(user_loginname) on delete cascade on update cascade            )
            """
            cursor.execute(query)

            query = """DROP TABLE IF EXISTS TAGS CASCADE;"""
            cursor.execute(query)

            query = """CREATE TABLE IF NOT EXISTS TAGS (
            tag_id serial unique,
            tweet_input VARCHAR(200) not null,
            tag_input VARCHAR(200) unique not null,
            tag_category VARCHAR(100) not null,
            date date default current_date ,
            primary key(tag_id),
            foreign key(tweet_input) references TWEETS(tweet_input) on delete cascade on update cascade
            )
            """

            cursor.execute(query)

            query = """DROP TABLE IF EXISTS COMMENTS CASCADE;"""
            cursor.execute(query)


            query = """CREATE TABLE IF NOT EXISTS COMMENTS (
            tweet_input VARCHAR(200) not null,
            comment_id serial unique not null,
            comment VARCHAR(200) not null,
            user_logname VARCHAR(60) not null,
            date date default current_date,
            primary key(comment_id),
            foreign key(user_logname) references user_login(user_loginname) on delete cascade on update cascade,
            foreign key(tweet_input) references TWEETS(tweet_input) on delete cascade on update cascade)
            """

            cursor.execute(query)

            query = """DROP TABLE IF EXISTS DIRECTMESSAGES CASCADE;"""
            cursor.execute(query)

            query = """CREATE TABLE IF NOT EXISTS DIRECTMESSAGES(
            dm_id serial unique,
            user_logname1 VARCHAR(60) not null,
            user_logname2 VARCHAR(60) not null,
            message VARCHAR(200) not null,
            subject VARCHAR(100) not null,
            date date default current_date,
            primary key(dm_id),
            foreign key(user_logname1) references user_login(user_loginname) on delete cascade on update cascade,
            foreign key(user_logname2) references user_login(user_loginname) on delete cascade on update cascade
            )
            """

            cursor.execute(query)

            query = """DROP TABLE IF EXISTS ACTIVITIES CASCADE;"""
            cursor.execute(query)


            query = """CREATE TABLE IF NOT EXISTS ACTIVITIES(
            event_id serial unique not null,
            event_name VARCHAR(200) unique not null,
            event_location VARCHAR(200) not null,
            event_date VARCHAR(200) not null,
            event_category VARCHAR(200) not null,
            primary key(event_id, event_name))
            """

            cursor.execute(query)

            connection.commit();
            return 'Tables inserted <a href="http://localhost:5000">Home</a>'


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
                try:
                    query = """INSERT INTO TWEETS (user_logName, tweet_input, tweet_category) VALUES (%s, %s, %s)"""
                    cursor.execute(query, (user_login, new_tweet, new_category))
                    connection.commit();
                    return 'Your tweet has been successfully posted<a href="http://localhost:5000">Home</a>'
                except:
                    return 'Your tweet cannot be posted due to foreign key constraints! <a href="http://localhost:5000">Home</a>'

    def tweets_db(config):
        with dbapi2.connect(config) as connection:
            if request.method == 'GET':
                cursor = connection.cursor()
                query = "SELECT user_logname,tweet_id,tweet_input,tweet_category, date from tweets"
                cursor.execute(query)
                connection.commit();
                return render_template('tweets.html', tweets_list=cursor)


    def tweets_db_delete(config, deleteTweet):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM tweets where user_logname = %s"
            cursor.execute(query, (deleteTweet,))
            connection.commit();
            return redirect(url_for('tweets'))

    def tweets_db_update(config, updateTweet):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """SELECT tweet_input from tweets where user_logname = '%s'""" % (updateTweet)
            cursor.execute(query)
            connection.commit();
            return render_template('tweet_update.html', tweet_updates=cursor)


    def tweets_db_update_apply(config, updateTweet):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            try:
                new_tweet = request.form['tweet']
                query = """UPDATE tweets set tweet_input ='%s' where user_logName = '%s'""" % (new_tweet, updateTweet)
                cursor.execute(query)
                connection.commit();
                return redirect(url_for('tweets'))
            except:
                return 'Value cannot be NULL! <a href="http://localhost:5000">Home</a>'







