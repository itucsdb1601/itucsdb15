import json
import os
import psycopg2 as dbapi2
import re
from flask import Flask, request, render_template, redirect
from flask.helpers import url_for

app = Flask(__name__)

class favorites:


    def initialize_favorites(config):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """DROP TABLE IF EXISTS FAVORITES CASCADE;"""
            cursor.execute(query)
            query = """CREATE TABLE IF NOT EXISTS FAVORITES (favorite_id serial primary key, user_name VARCHAR(20) NOT NULL, user_surname VARCHAR(20) NOT NULL,user_loginname VARCHAR(30) UNIQUE NOT NULL, user_email VARCHAR(30) NOT NULL)"""
            cursor.execute(query)
            query = """INSERT INTO FAVORITES (user_loginname, user_name, user_surname, user_email) VALUES ('melis', 'songul', 'sarac' , 'skdj')"""
            cursor.execute(query)

            query = """DROP TABLE IF EXISTS FAVORITESTWEET CASCADE;"""
            cursor.execute(query)
            query = """CREATE TABLE IF NOT EXISTS FAVORITESTWEET (
            favoritetweet_id serial,
            user_loginname VARCHAR(20) NOT NULL UNIQUE,
            tweet_input VARCHAR(200) NOT NULL,
            tweet_category VARCHAR(100),
            PRIMARY KEY(favoritetweet_id),
            FOREIGN KEY(user_loginname) REFERENCES FAVORITES(user_loginname))"""
            cursor.execute(query)
            query = """INSERT INTO FAVORITESTWEET (user_loginname, tweet_input, tweet_category) VALUES ('melis', 'have a nice day', 'daily')"""
            cursor.execute(query)

            connection.commit();
            return 'Tables are Inserted'


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
                return render_template('favorites_edit.html')




    def favorites_db(config):
        with dbapi2.connect(config) as connection:
            if request.method == 'GET':
                cursor = connection.cursor()
                query="SELECT user_loginname,user_name,user_surname,user_email from favorites"
                cursor.execute(query)
                print(cursor)
                return render_template('favorites.html', favorites_list=cursor)

    def favorites_db_delete(config,deletefavorites):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query="DELETE FROM favorites where user_loginname = %s"
            cursor.execute(query, (deletefavorites,))
            connection.commit()
            return redirect(url_for('favorites'))

    def favorites_db_update(config,updatefavorites):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query="""SELECT user_loginname from favorites where user_loginname = '%s'""" % (updatefavorites)
            cursor.execute(query)
            connection.commit()
            return render_template('favorites_update.html',favorites_updates=cursor)

    def favorites_db_update_apply(config,updatefavorites):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            new_name = request.form['favorites']
            print(new_name)
            query="""UPDATE favorites set user_loginname ='%s' where user_loginname = '%s'""" % (new_name,updatefavorites)
            cursor.execute(query)
            connection.commit()
            return redirect(url_for('favorites'))






