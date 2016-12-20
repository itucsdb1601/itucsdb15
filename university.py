import json
import os
import psycopg2 as dbapi2
import re
from flask import Flask, request, render_template, redirect
from flask.helpers import url_for

app = Flask(__name__)
#OZAN ÖZCAN 040100106

class university:

	def initialize_universities(config):
		with dbapi2.connect(config) as connection:
			cursor = connection.cursor()
			query = """DROP TABLE IF EXISTS UNIVERSITYLIST CASCADE;"""
			cursor.execute(query)
			query = """DROP TABLE IF EXISTS UNIVERSITYTYPE CASCADE;"""
			cursor.execute(query)
			query = """DROP TABLE IF EXISTS UNICITY CASCADE;"""
			cursor.execute(query)
			query = """DROP TABLE IF EXISTS UNIPOPULARITY CASCADE;"""
			cursor.execute(query)
			query = """CREATE TABLE IF NOT EXISTS UNIVERSITYLIST (uni_id serial primary key, unicity_id VARCHAR(60) NOT NULL, uni_name  VARCHAR(80) NOT NULL, unitype_id VARCHAR(80) NOT NULL, startdate VARCHAR(80) NOT NULL);"""
			cursor.execute(query)
			query = """INSERT INTO UNIVERSITYLIST(uni_name, unitype_id, unicity_id, startdate) VALUES ('Istanbul Technical University','1','34', '1773'), ('Harvard University', '5', '999', '1850'), ('Mersin University','2','33', '1933'), ('Mimar Sinan Fine Arts University', '3', '34', '1802'), ('SUNY Buffalo', '5', '999', '1898');"""
			cursor.execute(query)
			connection.commit();
			query = """CREATE TABLE IF NOT EXISTS UNIVERSITYTYPE (type_id serial primary key, unitype VARCHAR(80) NOT NULL);"""
			cursor.execute(query)
			query = """INSERT INTO UNIVERSITYTYPE (unitype) VALUES ('Public Technical University'), ('Public University'), ('Sports and Arts University'), ('Private University'), ('Foreign University');"""
			cursor.execute(query)
			query = """CREATE TABLE IF NOT EXISTS UNICITY (city_id INTEGER, city_name VARCHAR(80) NOT NULL);"""
			cursor.execute(query)
			query = """INSERT INTO UNICITY VALUES (34,'Istanbul'), (35,'Izmir'), (999,'Foreign'), (33, 'Mersin'),(6,'Ankara'), (1,'Adana'), (7,'Antalya');"""
			cursor.execute(query)
			query = """CREATE TABLE IF NOT EXISTS UNIPOPULARITY (popularity_id INTEGER  primary key, uni_name VARCHAR(80) NOT NULL, totalscore INTEGER, totalusers INTEGER NOT NULL);"""
			cursor.execute(query)
			query = """INSERT INTO UNIPOPULARITY VALUES	(15, 'Gazi University', 10954, 322), (22, 'Izmir University', 2559, 210);"""
			cursor.execute(query)
			connection.commit();
			return 'University Tables Created <a href="http://localhost:5000">Home</a>'

	def universities_page(config):
		with dbapi2.connect(config) as connection:
			if request.method == 'GET':
				cursor = connection.cursor()
				query = "SELECT uni_name, startdate from UNIVERSITYLIST"
				cursor.execute(query)
				return render_template('universities.html', unis=cursor)

	def saveuniversity(config):
		uni_name = None
		unitype_id = None
		unicity_id = None
		startdate = None
		if request.method == 'POST':
			unitype_id = request.form['unitype_id']
			print(unitype_id)
			unicity_id = request.form['unicity_id']
			print(unicity_id)
			uni_name = request.form['uniname_text']
			print(uni_name)
			startdate = request.form['founded']
			print(startdate)
			with dbapi2.connect(config) as connection:
				cursor = connection.cursor()
				query = """INSERT INTO UNIVERSITYLIST(uni_name, unitype_id, unicity_id, startdate) VALUES (%s, %s, %s , %s)"""
				cursor.execute(query, (uni_name, unicity_id, unitype_id, startdate ))
				connection.commit();
				return redirect(url_for('universities'))


	def universities_page_delete(config, deleteuniversities):
		with dbapi2.connect(config) as connection:
			cursor = connection.cursor()
			query = """DELETE FROM UNIVERSITYLIST WHERE uni_name=%s"""
			cursor.execute(query, (deleteuniversities,))
			connection.commit();
			return redirect(url_for('universities'))

	def universities_page_update(config, updateuniversities):
		with dbapi2.connect(config) as connection:
			cursor = connection.cursor()
			query = """SELECT uni_name from UNIVERSITYLIST WHERE uni_name = '%s'""" % (updateuniversities)
			cursor.execute(query)
			connection.commit();
			return render_template('universities_edit.html', uni=cursor)

	def universities_page_update_apply(config,updateuniversities):
		with dbapi2.connect(config) as connection:
			cursor = connection.cursor()
			new_uni = request.form['uname']
			print(new_uni)
			try:
				query="""UPDATE UNIVERSITYLIST set uni_name = '%s' where uni_name = '%s'""" % (new_uni,updateuniversities)
				cursor.execute(query)
				connection.commit()
				return redirect(url_for('universities'))
			except:
				return 'slkjdls'







