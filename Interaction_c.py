'''
Created on Dec 17, 2016

@author: Zeynep
'''
import json
import os
import psycopg2 as dbapi2
import re
from flask import Flask, request, render_template, redirect
from flask.helpers import url_for

app = Flask(__name__)
# # ZEYNEP ONER � - 150150706
class Interaction_c:

    # Initialize database tables from beginning, insert some example values
    # Coutnries and Hobbiesa are static tables that are related to user_hobbies and user_communication
    def initialize_interaction(config):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
        
        query = """DROP TABLE IF EXISTS FOLLOWERS"""
        cursor.execute(query)
        connection.commit();
        
        query = """DROP TABLE IF EXISTS EVENTS"""
        cursor.execute(query)
        connection.commit();
        
        query = """DROP TABLE IF EXISTS LOCATION"""
        cursor.execute(query)
        connection.commit();
        
        query = """ CREATE TABLE IF NOT EXISTS LOCATION (location_id serial primary key,location_name VARCHAR(200))"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('ADANA')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('ADIYAMAN')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('AFYONKARAHISAR')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('AKSARAY')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('AMASYA')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('ANKARA')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('ANTALYA')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('ARDAHAN')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('ARTVIN')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('AYDIN')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('BALIKESIR')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('BARTIN')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('BATMAN')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('BAYBURT')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('BINGOL')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('BOLU')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('BURDUR')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('BURSA')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('DENIZLI')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('DIYARBAKIR')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('DUZCE')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('EDIRNE')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('ELAZIG')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('ERZINCAN')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('ERZURUM')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('ESKISEHIR')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('GAZIANTEP')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('GIRESUN')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('GUMUSHANE')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('HAKKARI')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('HATAY')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('ISPARTA')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('IGDIR')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('KARABUK')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('KARAMAN')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('KARS')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('KASTAMONU')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('KAYSERI')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('KILIS')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('KIRIKKALE')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('KIRKLARELI')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('KIRSEHIR')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('KOCAELI')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('KONYA')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('KUTAHYA')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('MALATYA')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('MANISA')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('MARDIN')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('MERSIN')"""
        cursor.execute(query)
        connection.commit();
        
        
        query = """ insert into LOCATION(location_name) values('MUGLA')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('MUS')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('NEVSEHIR')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('NIGDE')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('NEVSEHIR')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('NIGDE')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('ORDU')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('OSMANIYE')"""
        cursor.execute(query)
        connection.commit();
        
        
        query = """ insert into LOCATION(location_name) values('RIZE')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('SAKARYA')"""
        cursor.execute(query)
        connection.commit();
        
        
        query = """ insert into LOCATION(location_name) values('SAMSUN')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('SIIRT')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('SINOP')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('SIVAS')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('TEKIRDAG')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('TOKAT')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('TRABZON')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('TUNCELI')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('USAK')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('VAN')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('YALOVA')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('YOZGAT')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('ZONGULDAK')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('CANAKKALE')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('CANKIRI')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('CORUM')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('ISTANBUL')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('IZMIR')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('SANLIURFA')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into LOCATION(location_name) values('SIRNAK')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ CREATE TABLE IF NOT EXISTS EVENTS (event_id serial primary key,event_name VARCHAR(200), event_time VARCHAR(200), event_price VARCHAR(200))"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into EVENTS(event_name,event_time,event_price) values('Kalben',' 10 October','50 TL')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into EVENTS(event_name,event_time,event_price) values('Mabel Matiz',' 17 November','37 TL')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into EVENTS(event_name,event_time,event_price) values('Athena',' 8 October','47 TL')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into EVENTS(event_name,event_time,event_price) values('Cem Adrian',' 10 October','50 TL')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into EVENTS(event_name,event_time,event_price) values('Yasar',' 10 October','50 TL')"""
        cursor.execute(query)
        connection.commit();
        
        query = """DROP TABLE IF EXISTS FOLLOWING"""
        cursor.execute(query)
        connection.commit();
        
        query = """DROP TABLE IF EXISTS BLOCKED"""
        cursor.execute(query)
        connection.commit();
        
        query = """DROP TABLE IF EXISTS BLOCKED_TYPE"""
        cursor.execute(query)
        connection.commit();
        
        query = """DROP TABLE IF EXISTS PLAYLIST"""
        cursor.execute(query)
        connection.commit();
        
        query = """DROP TABLE IF EXISTS SM"""
        cursor.execute(query)
        connection.commit();
        
        query = """ CREATE TABLE IF NOT EXISTS SM (social_media_id serial primary key,social_media_name VARCHAR(200))"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into SM(social_media_name) values('Instagram')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into SM(social_media_name) values('Facebook')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into SM(social_media_name) values('Pinterest')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into SM(social_media_name) values('Tinder')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into SM(social_media_name) values('Spotify')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ CREATE TABLE IF NOT EXISTS PLAYLIST (playlist_id serial primary key,singer_name VARCHAR(200)  ,song_name VARCHAR(200), minute VARCHAR(200))"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into PLAYLIST(singer_name,song_name,minute) values('Drake','Feel No Ways','3:55')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into PLAYLIST(singer_name,song_name,minute) values('G-Eazy','Drifting','3:54')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into PLAYLIST(singer_name,song_name,minute) values('Wiz Khalifa','Material','4:37')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into PLAYLIST(singer_name,song_name,minute) values('Tyga','Diced Pineapples','3:23')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into PLAYLIST(singer_name,song_name,minute) values('Usher','Lemme See','4:05')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into PLAYLIST(singer_name,song_name,minute) values('The Weeknd','House of Balloons','3:37')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into PLAYLIST(singer_name,song_name,minute) values('Snoop Dogg','Kush','4:00')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into PLAYLIST(singer_name,song_name,minute) values('Murat Boz','Direniyorsun','4:05')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into PLAYLIST(singer_name,song_name,minute) values('Cem Belevi','Alisamiyorum','3:37')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into PLAYLIST(singer_name,song_name,minute) values('Emir','Bir Agla','4:00')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into PLAYLIST(singer_name,song_name,minute) values('Aydin Kurtoglu','Yak','4:05')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into PLAYLIST(singer_name,song_name,minute) values('Mustafa Ceceli','Husran','3:37')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into PLAYLIST(singer_name,song_name,minute) values('Aleyna Tilki','Cevapsiz Cinlama','4:00')"""
        cursor.execute(query)
        connection.commit();
        
        
        query = """ CREATE TABLE IF NOT EXISTS FOLLOWERS (follower_id serial primary key,follower_name VARCHAR(200)  ,follower_email VARCHAR(200),follower_username VARCHAR(200),follower_date VARCHAR(200), playlist_id integer,social_media_id integer)"""
        cursor.execute(query)
        connection.commit();
        
        query = """ CREATE TABLE IF NOT EXISTS FOLLOWING (following_id serial primary key,following_name VARCHAR(200) ,following_email VARCHAR(200),following_username VARCHAR(200),following_date VARCHAR(200),event_id integer,location_id integer)"""
        cursor.execute(query)
        connection.commit();
        
        query = """ CREATE TABLE IF NOT EXISTS BLOCKED (blocked_id serial primary key,blocked_name VARCHAR(200) ,blocked_email VARCHAR(200),blocked_username VARCHAR(200),blocked_date VARCHAR(200),blocked_type VARCHAR(200),blocking_time VARCHAR(200))"""
        cursor.execute(query)
        connection.commit();
        
        
        query = """ CREATE TABLE IF NOT EXISTS BLOCKED_TYPE (type_id serial primary key, type VARCHAR(200))"""
        cursor.execute(query)
        connection.commit();
        
        
        query = """ insert into BLOCKED_TYPE(type) values('inappropriate content')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into BLOCKED_TYPE(type) values('fake profile')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into BLOCKED_TYPE(type) values('distracting message content')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into BLOCKED_TYPE(type) values('violent profile')"""
        cursor.execute(query)
        connection.commit();
        
        return 'sdfjlksfjlsk'

    def check(config):
        user_loginname = None
        if request.method == 'POST':
            user_loginname = request.form['user_name_text']
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                
                    query = "SELECT * FROM FOLLOWERS where follower_username = '%s'" % (user_loginname)
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount != 0:
                        return "this entry already exists in followers table"
                
                    query = """SELECT user_name,user_email,user_loginname FROM USER_LOGIN where user_loginname = '%s'""" % (user_loginname)
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount == 0:
                        return "there is no such entry in the user table"
                    rows = cursor.fetchall()
                    for row in rows:
                        query = "INSERT INTO FOLLOWERS(follower_name,follower_email,follower_username) VALUES(%s,%s,%s)"
                        cursor.execute(query, (row[0], row[1], row[2]))
                        connection.commit();
                        return render_template('followers.html')
                except:
                    return "exception occurs"

    def check3(config):
        user_loginname = None
        if request.method == 'POST':
            user_loginname = request.form['user_name_text3']
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                
                    query = "SELECT * FROM BLOCKED where blocked_username = '%s'" % (user_loginname)
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount != 0:
                        return "this entry already exists in blocked table"
                
                    query = """SELECT user_name,user_email,user_loginname FROM USER_LOGIN where user_loginname = '%s'""" % (user_loginname)
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount == 0:
                        return "there is no such entry in the user table"
                    rows = cursor.fetchall()
                    for row in rows:
                        query = "INSERT INTO BLOCKED(blocked_name,blocked_email,blocked_username) VALUES(%s,%s,%s)"
                        cursor.execute(query, (row[0], row[1], row[2]))
                        connection.commit();
                        return render_template('blocked.html')
                except:
                    return "exception occurs"


    def search(config):
        follower_name = None
        follower_email = None
        if request.method == 'POST':
            follower_name = request.form['follower_name_text']
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    query = "SELECT follower_name,follower_email,follower_username,follower_date FROM FOLLOWERS where follower_username = '%s';" % (follower_name)
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount == 0:
                        return "there is no such entry in the followers table"
                    return render_template('search_display.html', followers=cursor)
                except:
                    return "there is no such entry in the table"

    def search_blocked(config):
        blocked_name = None
        blocked_email = None
        if request.method == 'POST':
            blocked_name = request.form['follower_name_text']
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    query = "SELECT blocked_name,blocked_email,blocked_username,blocked_date,blocked_type FROM BLOCKED where blocked_username = '%s';" % (blocked_name)
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount == 0:
                        return "there is no such entry in the blocked table"
                    rows = cursor.fetchall()
                    for row in rows:
                        print (row[0], row[1], row[2], row[3],row[4])
                        return "selected row is printed"
                except:
                    return "there is no such entry in the table"

    def find(config):
        if request.method == 'POST':
            location_name = request.form['find_text']
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    query = "SELECT location_id from LOCATION where location_name = '%s';" % (location_name)
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount == 0:
                        return "there is no such city in the location table"
                    rows = cursor.fetchall()
                    for row in rows:
                        query = "SELECT * FROM FOLLOWING where location_id = '%s';"
                        cursor.execute(query, (row[0],))
                        rowcount = cursor.rowcount
                        if rowcount == 0:
                            return "there is no such following person in this location"
                        rows2 = cursor.fetchall()
                        for row2 in rows2:
                            print (row2[1], row2[2], row2[3])
                            return "selected row is printed"
                except:
                    return "exception occurs"


    def check2(config):
        user_loginname = None
        if request.method == 'POST':
            user_loginname = request.form['user_name_text2']
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    query = "SELECT * FROM FOLLOWING where following_username = '%s'" % (user_loginname)
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount != 0:
                        return "this entry already exists in following table"
                    
                    query = "SELECT user_name,user_email,user_loginname FROM USER_LOGIN where user_loginname = '%s'" % (user_loginname)
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount == 0:
                        return "there is no such entry in the user table"
                    rows = cursor.fetchall()
                    for row in rows:
                        query = """INSERT INTO FOLLOWING(following_name,following_email,following_username) VALUES(%s,%s,%s)"""
                        cursor.execute(query, (row[0], row[1], row[2]))
                        connection.commit();
                        return render_template('following.html')      
                except:
                    return "exception occurs"


    def unfollow(config):
        if request.method == 'POST':
            follower_username = request.form['follower_name_text']
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    query = "SELECT follower_name,follower_email,follower_username FROM FOLLOWERS WHERE follower_username = '%s'" % (follower_username)
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount == 0:
                        return "there is no such entry in the followers table"
                    query = "DELETE FROM FOLLOWERS WHERE follower_username = '%s'" % (follower_username)
                    cursor.execute(query)
                    connection.commit();
                    return redirect(url_for('followers'))
                except:
                    return "exception occurs"

    def unfollow_following(config):
        if request.method == 'POST':
            following_username = request.form['follower_name_text']
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    query = "SELECT * FROM FOLLOWING WHERE following_username = '%s'" % (following_username)
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount == 0:
                        print ("there is no such entry in the followers table")
                        return " "
                    query = "DELETE FROM FOLLOWING WHERE following_username = '%s'" % (following_username)
                    cursor.execute(query)
                    connection.commit();
                    return redirect(url_for('following'))
                except:
                    return "exception occurs"

    def search_following(config):
        following_name = None
        following_email = None
        if request.method == 'POST':
            following_name = request.form['follower_name_text']
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    query = "SELECT following_name,following_email,following_username,following_date FROM FOLLOWING where following_username = '%s';" % (following_name)
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount == 0:
                        return "there is no such entry in the following table"
                    rows = cursor.fetchall()
                    for row in rows:
                        print (row[0], row[1], row[2], row[3])
                        return "selected row is printed"
            
                except:
                    return "there is no such entry in the table"




    def unfollow_blocked(config):
        if request.method == 'POST':
            blocked_username = request.form['follower_name_text']
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    query = "SELECT blocked_name,blocked_email,blocked_username FROM BLOCKED WHERE blocked_username = '%s'" % (blocked_username)
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount == 0:
                        return "there is no such entry in the followers table"
                    query = "DELETE FROM BLOCKED WHERE blocked_username = '%s'" % (blocked_username)
                    cursor.execute(query)
                    connection.commit();
                    return redirect(url_for('blocked'))
                except:
                    return "exception occurs"

    def follow(config):
        if request.method == 'POST':
            user_loginname = request.form['follower_name_text']
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                
                    query = "SELECT * FROM FOLLOWERS where follower_username = '%s'" % (user_loginname)
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount != 0:
                        return "this entry already exists in followers table"
                
                    query = "SELECT user_name,user_email,user_loginname FROM USER_LOGIN where user_loginname = '%s'" % (user_loginname)
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount == 0:
                        return "there is no such entry in the user table"
            
                    rows = cursor.fetchall()
                    for row in rows:
                        query = """INSERT INTO FOLLOWERS(follower_name,follower_email,follower_username) VALUES(%s,%s,%s)"""
                        cursor.execute(query, (row[0], row[1], row[2]))
                        connection.commit();
                        return render_template('followers.html')
                except:
                    return "exception occurs"

    def follow_following(config):
        following_name = None
        following_email = None
        if request.method == 'POST':
            user_loginname = request.form['follower_name_text']
            '''print(follower_email)'''
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    query = "SELECT * FROM FOLLOWING where following_username = '%s'" % (user_loginname)
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount != 0:
                        return "this entry already exists in following table"
                
                
                    query = "SELECT user_name,user_email,user_loginname FROM USER_LOGIN where user_loginname = '%s'" % (user_loginname)
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount == 0:
                        return "there is no such entry in the user table"
                    rows = cursor.fetchall()
                    for row in rows:
                        query = """INSERT INTO FOLLOWING(following_name,following_email,following_username) VALUES(%s,%s,%s)"""
                        cursor.execute(query, (row[0], row[1], row[2]))
                        connection.commit();
                        return render_template('following.html')
                except:
                    return "exception occurs"



    def follow_blocked(config):
        blocked_name = None
        blocked_email = None
        if request.method == 'POST':
            user_loginname = request.form['follower_name_text']
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                
                    query = "SELECT * FROM BLOCKED where blocked_username = '%s'" % (user_loginname)
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount != 0:
                        return "this entry already exists in blocked table"
                
                    query = "SELECT user_name,user_email,user_loginname FROM USER_LOGIN where user_loginname = '%s'" % (user_loginname)
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount == 0:
                        return "there is no such entry in the user table"
                    rows = cursor.fetchall()
                    for row in rows:
                        query = """INSERT INTO BLOCKED(blocked_name,blocked_email,blocked_username) VALUES(%s,%s,%s)"""
                        cursor.execute(query, (row[0], row[1], row[2]))
                        connection.commit();
                        return render_template('blocked.html')
                except:
                    return "exception occurs"

    def update_blocked(config):
        blocked_name = None
        blocked_email = None
        if request.method == 'POST':
            blocked_name = request.form['follower_name_text']
            blocked_type = request.form['block_type']
            blocking_time = request.form['blocking_time']
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    query = "SELECT * FROM BLOCKED where blocked_username = '%s'" % blocked_name
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount == 0:
                        return "there is no such entry in the following table"  
                    
                    if blocked_type == 'inappropriate content' :
                        query = """UPDATE BLOCKED SET blocked_type='inappropriate content' where blocked_username = '%s' ;""" %blocked_name
                        cursor.execute(query)
                    elif blocked_type == 'fake profile' :
                        query = """UPDATE BLOCKED SET blocked_type= 'fake profile' where blocked_username = '%s' ;"""%blocked_name
                        cursor.execute(query)
                    elif blocked_type == 'distracting message content' :
                        query = """UPDATE BLOCKED SET blocked_type= 'distracting message content' where blocked_username = '%s' ;"""%blocked_name
                        cursor.execute(query)
                    elif blocked_type == 'violent profile' :
                        query = """UPDATE BLOCKED SET blocked_type= 'violent profile' where blocked_username = '%s' ;"""%blocked_name
                        cursor.execute(query)    
                    connection.commit();
                    print(blocking_time)
                    print(blocked_name)
                    query = """UPDATE BLOCKED SET blocking_time=%s where blocked_username =%s ;"""
                    cursor.execute(query,(blocking_time,blocked_name))
                    connection.commit();
                    return render_template('blocked.html')
                except:
                    return "exception occurs"

    def update(config):
        follower_name = None
        follower_email = None
    
        if request.method == 'POST':
            follower_name = request.form['follower_name_text']
            song_name = request.form['song_name']
            social_media_name = request.form['social_media_name']
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    query = "SELECT * FROM FOLLOWERS where follower_username = '%s';" % (follower_name)
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount == 0:
                        return "there is no such entry in the followers table"
                
                    if song_name == 'Cem Belevi - Alisamiyorum':
                        query = "SELECT playlist_id FROM PLAYLIST where singer_name = 'Cem Belevi'"
                    elif song_name == 'Murat Boz - Direniyorsun':
                        query = "SELECT playlist_id FROM PLAYLIST where singer_name = 'Murat Boz'"
                    elif song_name == 'Emir - Bir Agla':
                        query = "SELECT playlist_id FROM PLAYLIST where singer_name = 'Emir'"
                    elif song_name == 'Aydin Kurtoglu - Yak':
                        query = "SELECT playlist_id FROM PLAYLIST where singer_name = 'Ayd�n Kurtoglu'"
                    elif song_name == 'Mustafa Ceceli - Husran':
                        query = "SELECT playlist_id FROM PLAYLIST where singer_name = 'Mustafa Ceceli'"
                    elif song_name == 'Aleyna Tilki - Cevapsiz Cinlama':
                        query = "SELECT playlist_id FROM PLAYLIST where singer_name = 'Aleyna Tilki'"
                    elif song_name == 'Drake - Feel No Ways':
                        query = "SELECT playlist_id FROM PLAYLIST where singer_name = 'Drake'"
                    elif song_name == 'G-Eazy - Drifting':
                        query = "SELECT playlist_id FROM PLAYLIST where singer_name = 'G-Eazy'"
                    elif song_name == 'Wiz Khalifa - Material':
                        query = "SELECT playlist_id FROM PLAYLIST where singer_name = 'Wiz Khalifa'"
                    elif song_name == 'Tyga - Diced Pineapples':
                        query = "SELECT playlist_id FROM PLAYLIST where singer_name = 'Tyga'"
                    elif song_name == 'Usher - Lemme See':
                        query = "SELECT playlist_id FROM PLAYLIST where singer_name = 'Usher'"
                    elif song_name == 'The Weeknd - House of Balloons':
                        query = "SELECT playlist_id FROM PLAYLIST where singer_name = 'The Weeknd'"
                    elif song_name == 'Snoop Dogg - Kush':
                        query = "SELECT playlist_id FROM PLAYLIST where singer_name = 'Snoop Dogg'"
                    cursor.execute(query)
                    rows = cursor.fetchall()
                    for row in rows:
                        query = """UPDATE FOLLOWERS SET playlist_id= %s  where follower_username = %s ;"""
                        cursor.execute(query, (row[0], follower_name))
        
                    if social_media_name == 'Instagram':
                        query = "SELECT social_media_id FROM SM where social_media_name = 'Instagram'"
                    elif social_media_name == 'Facebook':
                        query = "SELECT social_media_id FROM SM where social_media_name = 'Facebook'"
                    elif social_media_name == 'Pinterest':
                        query = "SELECT social_media_id FROM SM where social_media_name = 'Pinterest'"
                    elif social_media_name == 'Tinder':
                        query = "SELECT social_media_id FROM SM where social_media_name = 'Tinder'"
                    elif social_media_name == 'Spotify':
                        query = "SELECT social_media_id FROM SM where social_media_name = 'Spotify'"
                    cursor.execute(query)
                    rows = cursor.fetchall()
                    for row in rows:
                        query = """UPDATE FOLLOWERS SET social_media_id= %s  where follower_username = %s ;"""
                        cursor.execute(query, (row[0], follower_name))
                        return render_template('followers.html')
                except:
                    return "exception occurs"



    def update_following(config):
        following_name = None
        following_email = None
        if request.method == 'POST':
            following_name = request.form['follower_name_text']
            event_name = request.form['event_name']
            location_name = request.form['location_text']
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    query = "SELECT * FROM FOLLOWING where following_username = '%s'" % following_name
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount == 0:
                        return "there is no such entry in the following table"
                    if event_name == 'Kalben':
                        query = "SELECT event_id FROM EVENTS where event_name = 'Kalben'"
                    elif event_name == 'Mabel Matiz':
                        query = "SELECT event_id FROM EVENTS where event_name = 'Mabel Matiz'"
                    elif event_name == 'Cem Adrian':
                        query = "SELECT event_id FROM EVENTS where event_name = 'Cem Adrian'"
                    elif event_name == 'Athena':
                        query = "SELECT event_id FROM EVENTS where event_name = 'Athena'"
                    elif event_name == 'Yasar':
                        query = "SELECT event_id FROM EVENTS where event_name = 'Yasar'"
                    cursor.execute(query)
                    rows = cursor.fetchall()
                    for row in rows:
                        query = """UPDATE FOLLOWING SET event_id= %s  where following_username = %s ;"""
                        cursor.execute(query, (row[0], following_name))
                        query = "SELECT * FROM LOCATION where location_name = '%s'" % location_name
                        cursor.execute(query)
                        rowcount = cursor.rowcount;
                    if rowcount == 0:
                        return "there is no such city in the location table"
                    rows = cursor.fetchall()
                    for row in rows:
                        query = """UPDATE FOLLOWING SET location_id= %s  where following_username = %s ;"""
                        cursor.execute(query, (row[0], following_name))
                        return render_template('following.html')
                except:
                    return "exception occurs"

