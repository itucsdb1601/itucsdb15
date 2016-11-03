import json
import os
import psycopg2 as dbapi2
import re
<<<<<<< HEAD
from flask import Flask, request, render_template, redirect
from flask.helpers import url_for
=======
from flask import Flask, request, render_template


app = Flask(__name__)
>>>>>>> 72451323770cee9de3c5a2d8fc3a1441ffa8b894


def initialize_database(config):
    with dbapi2.connect(config) as connection:
        cursor = connection.cursor()

<<<<<<< HEAD
        query = """CREATE TABLE IF NOT EXISTS USER_LOGIN (user_id serial primary key, user_loginname NOT NULL VARCHAR(60), user_password VARCHAR(20) NOT NULL,user_name VARCHAR(30) NOT NULL, user_surname VARCHAR(30) NOT NULL, user_email UNIQUE NOT NULL VARCHAR(120), user_gender integer"""
        cursor.execute(query)
        try:
            cursor.execute(query)
        except:
            print("Oops!  That user name exists.  Try again...")
        connection.commit();
        #initialize_tweets(config)
        #initialize_followers(config)
        #initialize_favoritestable(config)
        #initialize_universities(config)
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
        
        query = """CREATE TABLE IF NOT EXISTS FOLLOWERS (following_id serial primary key,follower_name VARCHAR(200) ,follower_email VARCHAR(200))"""
        cursor.execute(query)
        
        query = """insert into FOLLOWERS(follower_name,follower_email) values('c','d')"""
=======
        query = """CREATE TABLE IF NOT EXISTS USER_LOGIN (user_id serial primary key, user_loginname VARCHAR(60) NOT NULL, user_password VARCHAR(20) NOT NULL , user_name VARCHAR(30) NOT NULL, user_surname VARCHAR(30) NOT NULL , user_email VARCHAR(120) NOT NULL , user_gender VARCHAR(10))"""
        cursor.execute(query)
        connection.commit();
        query = """CREATE TABLE IF NOT EXISTS TWEETS (tweet_id serial primary key, user_logName VARCHAR(60) NOT NULL , tweet_input VARCHAR(200) NOT NULL)"""
        cursor.execute(query)
        connection.commit();
        query = """CREATE TABLE IF NOT EXISTS FAVORITES (favorite_id serial primary key, user_name VARCHAR(20) NOT NULL, user_surname VARCHAR(20) NOT NULL,user_loginname VARCHAR(30) UNIQUE NOT NULL, user_email VARCHAR(30) NOT NULL)"""
>>>>>>> 72451323770cee9de3c5a2d8fc3a1441ffa8b894
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




<<<<<<< HEAD
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
        

def saveuser(config):
    user_name = None
    user_surname = None
    user_loginname = None
    user_password = None
    user_email = None
    user_gender = None
    if request.method == 'POST':
        user_name= request.form['name_text']
        user_surname = request.form['surname_text']
        print(user_surname)
        user_loginname = request.form['username_text']
        print(user_loginname)
        user_password = request.form['password_text']
        user_email = request.form['email_text']
        print(user_email)
        if request.form['gender'] == 'Male':
            user_gender = 'm'
        else:
            user_gender = 'f'
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO USER_LOGIN(user_loginname,user_password,user_name,user_surname,user_email,user_gender) VALUES (%s,%s,%s,%s,%s,%s);"""
            cursor.execute(query,(user_loginname,user_password,user_name,user_surname,user_email,user_gender))
            connection.commit();
            return redirect(url_for('login'))

def users_page_db(config):
    with dbapi2.connect(config) as connection:
        if request.method == 'GET':
            cursor = connection.cursor()
            query="SELECT user_loginname,user_name,user_surname,user_email,user_gender from user_login"
            cursor.execute(query)
            print(cursor)
            return render_template('profiles.html',users=cursor)
def users_page_db_delete(config,deleteuserlogin):
    with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query="DELETE FROM user_login where user_loginname = %s"
            cursor.execute(query, (deleteuserlogin,))
            connection.commit()
            return redirect(url_for('profiles'))
def users_page_db_update(config,updateuserlogin):
     with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query="""SELECT user_loginname from user_login where user_loginname = '%s'""" % (updateuserlogin)
            cursor.execute(query)
            connection.commit()
            return render_template('profiles_edit.html',logins=cursor)
def users_page_db_update_apply(config,updateuserlogin):
    with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            new_name = request.form['name']
            print(new_name)
            query="""UPDATE user_login set user_loginname ='%s' where user_loginname = '%s'""" % (new_name,updateuserlogin)
            cursor.execute(query)
            connection.commit()
            return redirect(url_for('profiles'))



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
    
    if request.method == 'POST':
        follower_name= request.form['name_text']
        print(user_name)
        follower_email = request.form['email_text']
        print(user_surname)
        
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO FOLLOWERS(follower_name,follower_email) VALUES (%s,%s);"""
            cursor.execute(query,(follower_name,follower_email))
            connection.commit();
            return redirect(url_for('followers'))



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




=======
>>>>>>> 72451323770cee9de3c5a2d8fc3a1441ffa8b894
