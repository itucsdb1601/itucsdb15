import json
import os
import psycopg2 as dbapi2
import re
from flask import Flask, request, render_template, redirect
from flask.helpers import url_for

app = Flask(__name__)

class directmessages:

    def savedirectmessage(config):
        user_logname1 = None
        user_logname2 = None
        message = None
        subject = None
        if request.method == 'POST':
            user_logname1 = request.form['senderlogname_text']
            print(user_logname1)
            user_logname2 = request.form['receiverlogname_text']
            print(user_logname2)
            message = request.form['message_text']
            print(message)
            subject = request.form['subject_text']
            print(subject)
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    query = """INSERT INTO DIRECTMESSAGES (user_logname1, user_logname2, message, subject) VALUES (%s, %s, %s, %s)"""
                    cursor.execute(query, (user_logname1, user_logname2, message, subject))
                    connection.commit();
                    return 'Your message has been successfully posted <a href="http://localhost:5000">Home</a>'
                except:
                    return 'Your message cannot be added due to foreign key constraints! <a href="http://localhost:5000">Home</a>'


    def directmessages_db(config):
        with dbapi2.connect(config) as connection:
            if request.method == 'GET':
                cursor = connection.cursor()
                query = "SELECT DISTINCT user_logname1, user_logname2,message ,subject, date from DIRECTMESSAGES"
                cursor.execute(query)
                connection.commit();
                return render_template('directmessages.html', directmessages_list=cursor)


    def directmessages_db_delete(config, deletedm):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM DIRECTMESSAGES where user_logname1 = %s"
            cursor.execute(query, (deletedm,))
            connection.commit();
            return redirect(url_for('directmessages'))

    def directmessages_db_update(config, updatetag):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """SELECT message from directmessages where user_logname1 = '%s'""" % (updatetag)
            cursor.execute(query)
            connection.commit();
            return render_template('directmessages_update.html', directmessage_updates=cursor)


    def directmessages_db_update_apply(config, updatedm):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            try:
                message = request.form['directmessage']
                query = """UPDATE directmessages set message ='%s' where user_logname1 = '%s'""" % (message, updatedm)
                cursor.execute(query)
                connection.commit();
                return redirect(url_for('directmessages'))
            except:
                return 'Value cannot be NULL! <a href="http://localhost:5000">Home</a>'






