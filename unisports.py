import json
import os
import psycopg2 as dbapi2
import re
from flask import Flask, request, render_template, redirect
from flask.helpers import url_for

app = Flask(__name__)

#OZAN ÖZCAN 040100106
class unisports:

    def initialize_unisports(config):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """DROP TABLE IF EXISTS UNITEAMS CASCADE;"""
            cursor.execute(query)
            query = """DROP TABLE IF EXISTS UNILEAGUES CASCADE;"""
            cursor.execute(query)
            query = """DROP TABLE IF EXISTS COMPETITION CASCADE;"""
            cursor.execute(query)
            query = """CREATE TABLE IF NOT EXISTS UNITEAMS (team_id serial primary key, uni_name VARCHAR(80) UNIQUE NOT NULL, team_name VARCHAR(50) NOT NULL);"""
            cursor.execute(query)
            query = """INSERT INTO UNITEAMS (uni_name, team_name) VALUES ('Istanbul Technical University','Hornets'), ('Harvard University', 'Crimson'), ('Mersin University','Mustangs'), ('SUNY Buffalo', 'Bulls'), ('Bogazici University', 'Sultans');"""
            cursor.execute(query)
            query = """CREATE TABLE IF NOT EXISTS UNILEAGUES (league_id serial primary key, league_name VARCHAR(80) UNIQUE NOT NULL, country_id INTEGER    NOT NULL);"""
            cursor.execute(query)
            query = """INSERT INTO UNILEAGUES (league_name, country_id) VALUES ('NCAA Football Bowl Subdivision', 5), ('Istanbul Basketbol Ligi', 90), ('Universiteler Spor Ligi', 90), ('IFAF Europe Champions League', 5);"""
            cursor.execute(query)
            query = """CREATE TABLE IF NOT EXISTS COMPETITION (id serial primary key, country_id INTEGER NOT NULL, competition_type VARCHAR(80) NOT NULL);"""
            cursor.execute(query)
            query = """INSERT INTO COMPETITION (country_id, competition_type) VALUES (90, 'Domestic Intercollegiate'), (5, 'Foreign Tournament');"""
            connection.commit()
            return 'University Sport Tables Created <a href="http://localhost:5000">Home</a>'


    def unisports_page(config):
        with dbapi2.connect(config) as connection:
            if request.method == 'GET':
                cursor = connection.cursor()
                query = "SELECT team_id, uni_name from UNITEAMS"
                cursor.execute(query)
                return render_template('unisports.html', unis=cursor)

    def saveuniteam(config):
        uni_name = None
        team_name = None
        if request.method == 'POST':
            uni_name = request.form['uniname_text']
            team_name = request.form['teamname_text']
            with dbapi2.connection(config) as connection:
                cursor = connection.cursor()
                return redirect(url_for('unisports_add'))


    def unisports_page_delete(config, deleteuniteam):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """DELETE FROM UNITEAMS WHERE uni_name=%s"""
            cursor.execute(query, (deleteuniteam,))
            connection.commit();
            return redirect(url_for('unisports'))

    def unisports_page_update(config, updateuniteam):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """SELECT uni_name from UNITEAMS WHERE uni_name = %s""" % (updateuniteam)
            cursor.execute(query)
            connection.commit();
            return render_template('unisports_edit.html', unispo=cursor)

    def unisports_page_update_apply(config,updateuniteam):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            new_uniteam = request.form['name']
            print(new_uniteam)
            query="""UPDATE UNITEAMS set uni_name =%s where uni_name= %s""" % (new_uniteam,updateuniteam)
            cursor.execute(query)
            connection.commit()
            return redirect(url_for('unisports'))







