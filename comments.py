import json
import os
import psycopg2 as dbapi2
import re
from flask import Flask, request, render_template, redirect
from flask.helpers import url_for

app = Flask(__name__)

class comments:

    def savecomment(config):
        tweet_id = None
        user_logname = None
        comment = None
        if request.method == 'POST':
            tweet_id = request.form['tweetid_text']
            print(tweet_id)
            user_logname = request.form['userlogname_text']
            print(user_logname)
            comment = request.form['comment_text']
            print(comment)
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    query = """INSERT INTO comments (tweet_id, comment, user_logname) VALUES (%d, %s, %s)"""
                    cursor.execute(query, (tweet_id, user_logname, comment))
                    connection.commit();
                    return 'Your comment has been successfully posted <a href="http://localhost:5000">Home</a>'
                except:
                    return 'Your comment cannot be added due to foreign key constraints! <a href="http://localhost:5000">Home</a>'


    def comments_db(config):
        with dbapi2.connect(config) as connection:
            if request.method == 'GET':
                cursor = connection.cursor()
                query = "SELECT DISTINCT comments.user_logname, tweet_input, comment  from COMMENTS, TWEETS where comments.tweet_id=tweets.tweet_id"
                cursor.execute(query)
                connection.commit();
                return render_template('comments.html', comments_list=cursor)


    def comments_db_delete(config, deletecomment):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM COMMENTS where user_logname = %s"
            cursor.execute(query, (deletecomment,))
            connection.commit();
            return redirect(url_for('comments'))

    def comments_db_update(config, updatecomment):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """SELECT comment from comments where user_logname = '%s'""" % (updatecomment)
            cursor.execute(query)
            connection.commit();
            return render_template('comments_update.html', comment_updates=cursor)


    def comments_db_update_apply(config, updatecomment):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            try:
                comment = request.form['comment_txt']
                query = """UPDATE comments set comment ='%s' where user_logname = '%s'""" % (comment, updatecomment)
                cursor.execute(query)
                connection.commit();
                return redirect(url_for('comments'))
            except:
                return 'Value cannot be NULL! <a href="http://localhost:5000">Home</a>'






