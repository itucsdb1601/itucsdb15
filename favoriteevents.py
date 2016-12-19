import json
import os
import psycopg2 as dbapi2
import re
from flask import Flask, request, render_template, redirect
from flask.helpers import url_for

app = Flask(__name__)

class favoriteevents:

    def savefavoriteEvents(config):
        event_name = None
        user_logname = None
        join_status = None
        if request.method == 'POST':
            event_name = request.form['event_name_text']
            print(event_name)
            user_logname = request.form['floginname_text']
            print(user_logname)
            join_status = request.form['status_text']
            print(join_status)
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    query = """INSERT INTO favoriteevents(event_name, user_logname, join_status) VALUES (%s, %s, %s)"""
                    cursor.execute(query, (event_name, user_logname, join_status))
                    connection.commit();
                    return 'Your favorite event has been successfully posted <a href="http://localhost:5000">Home</a>'
                except:
                    return 'Your favorite event cannot be added due to foreign key constraints! <a href="http://localhost:5000">Home</a>'


    def favoriteevents_db(config):
        with dbapi2.connect(config) as connection:
            if request.method == 'GET':
                cursor = connection.cursor()
                query = "SELECT user_logname, event_name, join_status from favoriteevents"
                cursor.execute(query)
                connection.commit();
                return render_template('favoriteEvents.html', favoriteEvents_list=cursor)


    def favoriteevents_db_delete(config, deletefavoriteEvent):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM favoriteevents where user_logname = %s"
            cursor.execute(query, (deletefavoriteEvent,))
            connection.commit();
            return redirect(url_for('favoriteEvents'))

    def favoriteevents_db_update(config, updatefavoriteEvent):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """SELECT join_status from favoriteevents where user_logname = '%s'""" % (updatefavoriteEvent)
            cursor.execute(query)
            connection.commit();
            return render_template('favoriteEvents_update.html', favoriteEvents_updates=cursor)


    def favoriteevents_db_update_apply(config, updatefavoriteEvent):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            try:
                join_status = request.form['favorites']
                query = """UPDATE favoriteevents set join_status ='%s' where user_logname = '%s'""" % (join_status, updatefavoriteEvent)
                cursor.execute(query)
                connection.commit();
                return redirect(url_for('favoriteEvents'))
            except:
                return 'Value cannot be NULL! <a href="http://localhost:5000">Home</a>'






