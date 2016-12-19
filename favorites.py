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
            query = """DROP TABLE IF EXISTS FAVORITESUSERS CASCADE;"""
            cursor.execute(query)
            query = """CREATE TABLE IF NOT EXISTS FAVORITEUSERS(
            favorite_id serial,
            user_logname1 VARCHAR(60) not null,
            user_logname2 VARCHAR(60) not null,
            date date DEFAULT current_date,
            relation VARCHAR(100) not null,
            primary key(favorite_id, user_logname1),
            foreign key(user_logname1) references user_login(user_loginname) on delete cascade on update cascade,
            foreign key(user_logname2) references user_login(user_loginname) on delete cascade on update cascade
            )
            """
            cursor.execute(query)
            query = """DROP TABLE IF EXISTS FAVORITESTWEETS CASCADE;"""
            cursor.execute(query)
            query = """CREATE TABLE IF NOT EXISTS FAVORITETWEETS(
            favoritetweet_id serial unique,
            tweet_id integer not null,
            user_logname VARCHAR(200) not null,
            pop_keyword VARCHAR(100) not null,
            primary key(favoritetweet_id, user_logname),
            foreign key(user_logname) references user_login(user_loginname) on delete cascade on update cascade,
            foreign key(tweet_id) references TWEETS(tweet_id) on delete cascade on update cascade
            )
            """
            cursor.execute(query)

            query = """DROP TABLE IF EXISTS FAVORITESTAGS CASCADE;"""
            cursor.execute(query)

            query = """CREATE TABLE IF NOT EXISTS FAVORITETAGS (
            favoritetag_id serial unique,
            tag_id integer not null,
            user_logname VARCHAR(60) not null,
            pop_tag VARCHAR(100) not null,
            date date DEFAULT current_date,
            primary key(favoritetag_id, tag_id),
            foreign key(tag_id) references tags(tag_id) on delete cascade on update cascade
            )
            """
            cursor.execute(query)


            query = """DROP TABLE IF EXISTS FAVORITESEVENTS CASCADE;"""
            cursor.execute(query)


            query = """CREATE TABLE IF NOT EXISTS FAVORITEEVENTS (
            favoriteevent_id serial unique not null,
            event_name VARCHAR(200) not null,
            user_logname VARCHAR(60) not null,
            join_status VARCHAR(150) not null,
            primary key(favoriteevent_id),
            foreign key(event_name) references events(event_name) on delete cascade on update cascade)
            """
            cursor.execute(query)


            query = """DROP TABLE IF EXISTS FAVORITESUNIS CASCADE;"""
            cursor.execute(query)

            query = """CREATE TABLE IF NOT EXISTS FAVORITEUNIS (
            uni_name VARCHAR(80)  NOT NULL,
            favoriteuni_id serial unique,
            fav_department VARCHAR(100) not null,
            user_logname VARCHAR(60) not null,
            primary key(favoriteuni_id),
            foreign key(user_logname) references user_login(user_loginname) on delete cascade on update cascade,
            foreign key(uni_name) references UNIVERSITYLIST(uni_name) on delete cascade on update cascade)
            """
            cursor.execute(query)

            connection.commit();
            return 'Tables are inserted <a href="http://localhost:5000">Home</a>'



    def saveFavoriteUser(config):
        user_logname1 = None
        user_logname2 = None
        relation = None
        if request.method == 'POST':
            user_logname1= request.form['fname_text']
            print(user_logname1)
            user_logname2 = request.form['fsurname_text']
            print(user_logname2)
            relation = request.form['floginname_text']
            print(relation)
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    query = """INSERT INTO FAVORITEUSERS(user_logname1,user_logname2,relation) VALUES (%s,%s,%s);"""
                    cursor.execute(query,(user_logname1,user_logname2,relation))
                    connection.commit();
                    return 'Favorite user information is inserted <a href="http://localhost:5000">Home</a>'
                except:
                    return  'The users do not exist in User_Login Table or values cannot be NULL! <a href="http://localhost:5000">Home</a> '

    def favorites_db(config):
        with dbapi2.connect(config) as connection:
            if request.method == 'GET':
                cursor = connection.cursor()
                query="SELECT user_logname1,user_logname2,date, relation from favoriteusers"
                cursor.execute(query)
                print(cursor)
                return render_template('favorites.html', favorites_list=cursor)

    def favorites_db_delete(config,deletefavorites):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query="DELETE FROM favoriteusers where user_logname1 = %s"
            cursor.execute(query, (deletefavorites,))
            connection.commit()
            return redirect(url_for('favorites'))

    def favorites_db_update(config,updatefavorites):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query="""SELECT relation from favoriteusers where user_logname1 = '%s'""" % (updatefavorites)
            cursor.execute(query)
            connection.commit()
            return render_template('favorites_update.html',favorites_updates=cursor)

    def favorites_db_update_apply(config,updatefavorites):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            try:
                new_name = request.form['favorites']
                print(new_name)
                query="""UPDATE favoriteusers set relation ='%s' where user_logname1 = '%s'""" % (new_name,updatefavorites)
                cursor.execute(query)
                connection.commit()
                return redirect(url_for('favorites'))
            except:
                return 'Value cannot be NULL! <a href="http://localhost:5000">Home</a>'







