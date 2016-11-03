import json
import os
import psycopg2 as dbapi2
import re
from flask import Flask, request, render_template


app = Flask(__name__)


def initialize_database(config):
    with dbapi2.connect(config) as connection:
        cursor = connection.cursor()

        query = """CREATE TABLE IF NOT EXISTS USER_LOGIN (user_id serial primary key, user_loginname VARCHAR(60) NOT NULL, user_password VARCHAR(20) NOT NULL , user_name VARCHAR(30) NOT NULL, user_surname VARCHAR(30) NOT NULL , user_email VARCHAR(120) NOT NULL , user_gender VARCHAR(10))"""
        cursor.execute(query)
        connection.commit();
        query = """CREATE TABLE IF NOT EXISTS TWEETS (tweet_id serial primary key, user_logName VARCHAR(60) NOT NULL , tweet_input VARCHAR(200) NOT NULL)"""
        cursor.execute(query)
        connection.commit();
        query = """CREATE TABLE IF NOT EXISTS FAVORITES (favorite_id serial primary key, user_name VARCHAR(20) NOT NULL, user_surname VARCHAR(20) NOT NULL,user_loginname VARCHAR(30) UNIQUE NOT NULL, user_email VARCHAR(30) NOT NULL)"""
        cursor.execute(query)
        connection.commit();
        return 'Value is inserted'


def saveuser(config):
    user_name = None
    user_surname = None
    user_loginname = None
    user_password = None
    user_email = None
    user_gender = None
    if request.method == 'POST':
        user_name= request.form['name_text']
        print(user_name)
        user_surname = request.form['surname_text']
        print(user_surname)
        user_loginname = request.form['loginname_text']
        print(user_loginname)
        user_password = request.form['password_text']
        print(user_password)
        user_email = request.form['email_text']
        print(user_email)
        if request.form['gender'] == 'Male':
            user_gender = 'm'
        else:
            user_gender = 'f'
        print(user_gender)
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO USER_LOGIN(user_loginname,user_password,user_name,user_surname,user_email,user_gender) VALUES (%s,%s,%s,%s,%s,%s);"""
            cursor.execute(query,(user_loginname,user_password,user_name,user_surname,user_email,user_gender))
            connection.commit();
            return 'User is inserted'

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




