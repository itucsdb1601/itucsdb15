import json
import os
import psycopg2 as dbapi2
import re
from flask import Flask, request, render_template, redirect
from flask.helpers import url_for

app = Flask(__name__)

class activities:

    def saveevent(config):
        event_name = None
        event_location = None
        event_date = None
        event_category = None
        if request.method == 'POST':
            event_name = request.form['eventname_text']
            print(event_name)
            event_location = request.form['eventloc_text']
            print(event_location)
            event_date = request.form['eventdate_text']
            print(event_date)
            event_category = request.form['eventcat_text']
            print(event_category)
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    query = """INSERT INTO activities(event_name, event_location, event_date, event_category) VALUES (%s, %s, %s, %s)"""
                    cursor.execute(query, (event_name, event_location, event_date, event_category))
                    connection.commit();
                    return 'Your activity has been successfully posted <a href="http://localhost:5000">Home</a>'
                except:
                    return 'Your activity cannot be added due to foreign key constraints! <a href="http://localhost:5000">Home</a>'


    def events_db(config):
        with dbapi2.connect(config) as connection:
            if request.method == 'GET':
                cursor = connection.cursor()
                query = "SELECT DISTINCT event_name, event_location, event_date, event_category  from ACTIVITIES"
                cursor.execute(query)
                connection.commit();
                return render_template('events.html', events_list=cursor)


    def events_db_delete(config, deleteevent):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM ACTIVITIES where event_name = %s"
            cursor.execute(query, (deleteevent,))
            connection.commit();
            return redirect(url_for('events'))

    def events_db_update(config, updateevent):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """SELECT event_name from activities where event_name = '%s'""" % (updateevent)
            cursor.execute(query)
            connection.commit();
            return render_template('events_update.html', events_updates=cursor)


    def events_db_update_apply(config, updateevent):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            try:
                comment = request.form['event_name']
                query = """UPDATE activities set event_name ='%s' where event_name = '%s'""" % (comment, updateevent)
                cursor.execute(query)
                connection.commit();
                return redirect(url_for('events'))
            except:
                return 'Value cannot be NULL! <a href="http://localhost:5000">Home</a>'






