import json
import os
import psycopg2 as dbapi2
import re
from flask import Flask, request, render_template, redirect
from flask.helpers import url_for

app = Flask(__name__)

class tags:





    def savetag(config):
        tweet_input = None
        new_category = None
        new_tag = None
        if request.method == 'POST':
            tweet_input = request.form['tweetinput_text']
            print(tweet_input)
            new_category = request.form['category_text']
            print(new_category)
            new_tag = request.form['tag_text']
            print(new_tag)
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    query = """INSERT INTO TAGS(tweet_input, tag_input ,tag_category) VALUES (%s, %s, %s)"""
                    cursor.execute(query, (tweet_input, new_tag, new_category))
                    connection.commit();
                    return 'Your tag has been successfully posted <a href="http://localhost:5000">Home</a>'
                except:
                    return 'Your tag cannot be added due to foreign key constraints! <a href="http://localhost:5000">Home</a>'


    def tags_db(config):
        with dbapi2.connect(config) as connection:
            if request.method == 'GET':
                cursor = connection.cursor()
                query = "SELECT DISTINCT user_logname, tags.tweet_input,tag_input ,tag_category, tags.date from TAGS , TWEETS where tags.tweet_input = tweets.tweet_input"
                cursor.execute(query)
                connection.commit();
                return render_template('tags.html', tag_list=cursor)


    def tags_db_delete(config, deletetag):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM tags where tag_input = %s"
            cursor.execute(query, (deletetag,))
            connection.commit();
            return redirect(url_for('tags'))

    def tags_db_update(config, updatetag):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """SELECT tag_input from tags where tag_input='%s'""" % (updatetag)
            cursor.execute(query)
            connection.commit();
            return render_template('tags_update.html', tag_updates=cursor)


    def tags_db_update_apply(config, updatetag):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            try:
                new_tag = request.form['tag']
                query = """UPDATE tags set tag_input ='%s' where tag_input = '%s'""" % (new_tag, updatetag)
                cursor.execute(query)
                connection.commit();
                return redirect(url_for('tags'))
            except:
                return 'Value cannot be NULL! <a href="http://localhost:5000">Home</a>'






