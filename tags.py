import json
import os
import psycopg2 as dbapi2
import re
from flask import Flask, request, render_template, redirect
from flask.helpers import url_for

app = Flask(__name__)

class tags:





    def savetag(config):
        new_tweet = None
        user_login = None
        new_category = None
        new_tag = None
        if request.method == 'POST':
            new_tweet = request.form['tweet_text']
            print(new_tweet)
            user_login = request.form['username_text']
            print(user_login)
            new_category = request.form['category_text']
            print(new_category)          
            new_tag = request.form['tag_text']
            print(new_tag)  
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                query = """INSERT INTO TAGS (user_logname, tweet_input,tag_input ,tag_category) VALUES (%s, %s, %s, %s)"""
                cursor.execute(query, (user_login, new_tweet,new_tag, new_category))
                connection.commit();
                return redirect(url_for('tags_edit'))


    def tags_db(config):
        with dbapi2.connect(config) as connection:
            if request.method == 'GET':
                cursor = connection.cursor()
                query = "SELECT user_logname, tweet_input,tag_input ,tag_category from tags"
                cursor.execute(query)
                connection.commit();
                return render_template('tags.html', tag_list=cursor)


    def tags_db_delete(config, deletetag):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM tags where user_logname = %s"
            cursor.execute(query, (deletetag,))
            connection.commit();
            return redirect(url_for('tags'))

    def tags_db_update(config, updatetag):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """SELECT tag_input from tags where user_logname = '%s'""" % (updatetag)
            cursor.execute(query)
            connection.commit();
            return render_template('tags_update.html', tag_updates=cursor)


    def tags_db_update_apply(config, updatetag):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            new_tag = request.form['tag']
            query = """UPDATE tags set tag_input ='%s' where user_logname = '%s'""" % (new_tag, updatetag)
            cursor.execute(query)
            connection.commit();
            return redirect(url_for('tags'))






