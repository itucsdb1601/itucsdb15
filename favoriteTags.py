import json
import os
import psycopg2 as dbapi2
import re
from flask import Flask, request, render_template, redirect
from flask.helpers import url_for

app = Flask(__name__)

class favoriteTags:

    def savefavoriteTags(config):
        tag_id = None
        user_logname = None
        pop_tag = None
        if request.method == 'POST':
            tag_id = request.form['tag_id_text']
            print(tag_id)
            user_logname = request.form['flogin_name_text']
            print(user_logname)
            pop_tag = request.form['pop_tag_text']
            print(pop_tag)
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    query = """INSERT INTO favoritetags(tag_id, user_logname, pop_tag) VALUES (%d, %s, %s)"""
                    cursor.execute(query, (tag_id, user_logname, pop_tag))
                    connection.commit();
                    return 'Your favorite tag has been successfully posted <a href="http://localhost:5000">Home</a>'
                except:
                    return 'Your favorite tag cannot be added due to foreign key constraints! <a href="http://localhost:5000">Home</a>'


    def favoriteTags_db(config):
        with dbapi2.connect(config) as connection:
            if request.method == 'GET':
                cursor = connection.cursor()
                query = "SELECT DISTINCT favoritetags.user_logname, tag_input, pop_tag from favoritetags, tags where tags.tag_id=favoritetags.tag_id"
                cursor.execute(query)
                connection.commit();
                return render_template('favoriteTags.html', favoriteTags_list=cursor)


    def favoriteTags_db_delete(config, deletefavoriteTag):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM favoritetags where user_logname = %s"
            cursor.execute(query, (deletefavoriteTag,))
            connection.commit();
            return redirect(url_for('favoriteTags'))

    def favoriteTags_db_update(config, updatefavoriteTag):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """SELECT pop_tag from favoritetags where user_logname = '%s'""" % (updatefavoriteTag)
            cursor.execute(query)
            connection.commit();
            return render_template('favoriteTags_update.html', favoriteTags_updates=cursor)


    def favoriteTags_db_update_apply(config, updatefavoriteEvent):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            try:
                pop_tag = request.form['pop_tag']
                query = """UPDATE favoritetags set pop_tag ='%s' where user_logname = '%s'""" % (pop_tag, updatefavoriteEvent)
                cursor.execute(query)
                connection.commit();
                return redirect(url_for('favoriteTags'))
            except:
                return 'Value cannot be NULL! <a href="http://localhost:5000">Home</a>'






