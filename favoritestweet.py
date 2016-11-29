import json
import os
import psycopg2 as dbapi2
import re
from flask import Flask, request, render_template, redirect
from flask.helpers import url_for

app = Flask(__name__)

class favoritestweet:



    def saveFavoriteTweet(config):
        user_loginname = None
        tweet_input = None
        tweet_category = None
        if request.method == 'POST':
            user_loginname= request.form['fname_text']
            print(user_loginname)
            tweet_input = request.form['ftweet_text']
            print(tweet_input)
            tweet_category = request.form['fcategory_text']
            print(tweet_category)
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                query = """INSERT INTO FAVORITESTWEET (user_loginname, tweet_input, tweet_category) VALUES (%s, %s, %s)"""
                cursor.execute(query,(user_loginname,tweet_input,tweet_category))
                connection.commit();
                return render_template('favorites_tweet_edit.html')




    def favoritestweet_db(config):
        with dbapi2.connect(config) as connection:
            if request.method == 'GET':
                cursor = connection.cursor()
                query="SELECT user_loginname,tweet_input,tweet_category from favoritestweet"
                cursor.execute(query)
                print(cursor)
                return render_template('favorites_tweet.html', favoritestweet_list=cursor)

    def favoritestweet_db_delete(config,deletefavoritestweet):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query="DELETE FROM favoritestweet where user_loginname = %s"
            cursor.execute(query, (deletefavoritestweet,))
            connection.commit()
            return redirect(url_for('favorites_tweet'))

    def favoritestweet_db_update(config,updatefavoritestweet):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query="""SELECT tweet_category from favoritestweet where user_loginname = '%s'""" % (updatefavoritestweet)
            cursor.execute(query)
            connection.commit()
            return render_template('favorites_tweet_update.html',favoritestweet_updates=cursor)

    def favoritestweet_db_update_apply(config,updatefavoritestweet):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            new_tweet = request.form['favoritestweet']
            print(new_tweet)
            query="""UPDATE favoritestweet set tweet_category ='%s' where user_loginname = '%s'""" % (new_tweet,updatefavoritestweet)
            cursor.execute(query)
            connection.commit()
            return redirect(url_for('favorites_tweet'))






