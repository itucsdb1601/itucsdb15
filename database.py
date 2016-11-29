import json
import os
import psycopg2 as dbapi2
import re
from flask import Flask, request, render_template, redirect
from flask.helpers import url_for
from flask import Flask, request, render_template
from Profile import Profile as profile
from tweets import tweets as tweet
from favorites import favorites as favorite

app = Flask(__name__)


def initialize_database(config):
    with dbapi2.connect(config) as connection:
        cursor = connection.cursor()
        profile.initialize_profiles(config)
        initialize_followers(config)
		tweet.initialize_tweets(config)
		favorite.initialize_favorites(config)
        connection.commit();
        return 'tables are created <a href="http://localhost:5000">Home</a>'



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


