import json
import os
import psycopg2 as dbapi2
import re
from flask import Flask


app = Flask(__name__)


def initialize_database(config):
    with dbapi2.connect(config) as connection:
        cursor = connection.cursor()

        query = """CREATE TABLE IF NOT EXISTS USER_LOGIN (user_id serial primary key,user_name VARCHAR (60) UNIQUE NOT NULL,user_password VARCHAR(20))"""
        cursor.execute(query)

        try:
            query = """insert into USER_LOGIN(user_name,user_password) values('saracso','1234567890')"""
            cursor.execute(query)
        except:
            print("Oops!  That user name exists.  Try again...")

        try:
            query = """insert into USER_LOGIN(user_name,user_password) values('aladagce','123456')"""
            cursor.execute(query)
        except:
            print("Oops!  That user name exists.  Try again...")

        connection.commit();
        initialize_tweets(config)
        initialize_followers(config)
	initialize_favoritestable(config)
	initialize_universities(config)
        return 'Value is inserted'

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

        query = """CREATE TABLE IF NOT EXISTS FOLLOWERS (following_event_id serial primary key,follower_id INTEGER NOT NULL ,user_id INTEGER NOT NULL)"""
        cursor.execute(query)

        query = """insert into FOLLOWERS(follower_id,user_id) values(2,1)"""
        cursor.execute(query)
        connection.commit();
        return 'A new follower is added to the follower list.'
		
		
		
def initialize_favoritestable(config):
    with dbapi2.connect(config) as connection:
        cursor = connection.cursor()

        query = """CREATE TABLE IF NOT EXISTS FAVORITES (fav_id serial primary key, user_id INTEGER NOT NULL,university_name VARCHAR(100))"""
        cursor.execute(query)
        try:
            query = """insert into FAVORITES(user_id,university_name) values('1','Istanbul Technical University')"""
            cursor.execute(query)
        except:
            print("Oops!  That favorite id already exists.  Try again...")
        connection.commit();
        return 'Favorite user  is inserted'

def initialize_universities(config):
    with dbapi2.connection(config) as connection:
        cursor = connection.cursor()
    
        query = """CREATE TABLE IF NOT EXISTS UNIVERSITY_USERS (
                    uni_id serial primary key,
                    user_id INTEGER NOT NULL,
                    uni_name VARCHAR(50) NOT NULL,
                    )"""
        cursor.execute(query)
        query = """INSERT INTO USER_LOGIN (user_id,uni_name) VALUES ('1','Istanbul Technical University')"""
        cursor.execute(query)
        connection.commit();
        return 'niversities table is inserted to store user-university data'


