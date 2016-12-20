import json
import os
import psycopg2 as dbapi2
import re
from flask import Flask, request, render_template, redirect
from flask.helpers import url_for

app = Flask(__name__)


class academics:

	def initialize_academics(config):
		with dbapi2.connect(config) as connection:
			cursor = connection.cursor()
			query = """DROP TABLE IF EXISTS ACADEMICINFO CASCADE;"""
			cursor.execute(query)
			query = """DROP TABLE IF EXISTS SCHOLARSHIPS CASCADE;"""
			cursor.execute(query)
			query = """DROP TABLE IF EXISTS RESDEV CASCADE;"""
			cursor.execute(query)
			query = """DROP TABLE IF EXISTS LEVELS CASCADE;"""
			cursor.execute(query)
			query = """CREATE TABLE IF NOT EXISTS ACADEMICINFO (id serial primary key, uni_name VARCHAR(80) UNIQUE NOT NULL, level VARCHAR(50) NOT NULL, scholarship VARCHAR(3) NOT NULL , mainresearch VARCHAR(100) NOT NULL, researchbudget VARCHAR(50) NOT NULL);"""
			cursor.execute(query)
			query = """INSERT INTO ACADEMICINFO (uni_name, level, scholarship, mainresearch, researchbudget) VALUES ('Istanbul Technical University', 3, 'y', 'Daylight Saving Time', 50000000), ('Harvard University', '1', 'y', 'Nobel Research', '100'), ('Mersin University','5', 'n', 'Agricultural Developments', '3000000');"""
			cursor.execute(query)
			query = """CREATE TABLE IF NOT EXISTS SCHOLARSHIPS (scholarship_id serial primary key, scholarshiptype VARCHAR(50) NOT NULL, scholarshipname VARCHAR (100) UNIQUE NOT NULL, scholars INTEGER, money_amount VARCHAR(50) NOT NULL);"""
			cursor.execute(query)
			query = """INSERT INTO SCHOLARSHIPS (scholarshiptype, scholarshipname, scholars, money_amount) VALUES ('Tuition', 'KYK', 300, 5000), ('Academic Excellence', 'Fulbright', 10, 300000), ('Athletic Excellence', 'NCAA Scholarship', 500, '40000');"""
			cursor.execute(query)
			query = """CREATE TABLE IF NOT EXISTS RESDEV (rdtype_id serial primary key, researchtype VARCHAR(50) NOT NULL, researchname VARCHAR(100) NOT NULL);"""
			cursor.execute(query)
			query = """INSERT INTO RESDEV (researchtype, researchname) VALUES ('Academic', 'Machine Learning'),('Athletic','Kinesiology in Contact Sports');"""
			cursor.execute(query)
			query = """CREATE TABLE IF NOT EXISTS LEVELS (id serial primary key, unilevel VARCHAR(50) NOT NULL, leveltype VARCHAR(80) UNIQUE NOT NULL);"""
			cursor.execute(query)
			query = """INSERT INTO LEVELS (unilevel, leveltype) VALUES ('1', 'Worldwide Known Top Class University'), ('2', 'Time Magazine top 40 University'), ('3', 'Top Tier Turkish University'), ('4', 'Average Turkish University'), ('5', 'Below Average Turkish University), ('6', 'Non-top tier foreign based University');"""
			connection.commit()
			return 'Academic Tables Created <a href="http://localhost:5000">Home</a>'



	def academics_page(config):
		with dbapi2.connect(config) as connection:
			if request.method == 'GET':
				cursor = connection.cursor()
				query = "SELECT uni_name, level, scholarship , mainresearch , researchbudget from ACADEMICINFO"
				cursor.execute(query)
				return render_template('academics.html', aca=cursor)

	def saveacademics(config):
		uni_name = None
		level = None
		scholarship = None
		mainresearch = None
		researchbudget = None

		if request.method == 'POST':
			uni_name = request.form['uniname_text']
			level = request.form['level_text']
			scholarship = request.form['scholarship_yn']
			mainresearch = request.form['research_text']
			researchbugdet = request.form['budget_text']
			with dbapi2.connection(config) as connection:
				cursor = connection.cursor()
				return redirect(url_for('academics_add'))


	def academics_page_delete(config, deleteacademicinfo):
		with dbapi2.connect(config) as connection:
			cursor = connection.cursor()
			query = """DELETE FROM ACADEMICINFO WHERE uni_name=%s"""
			cursor.execute(query, (deleteacademicinfo,))
			connection.commit();
			return redirect(url_for('academics'))

	def academics_page_update(config, updateacademicinfo):
		with dbapi2.connect(config) as connection:
			cursor = connection.cursor()
			query = """SELECT uni_name from ACADEMICINFO WHERE uni_name = %s""" % (updateacademicinfo)
			cursor.execute(query)
			connection.commit();
			return render_template('academics_edit.html', unispo=cursor)

	def academics_page_update_apply(config,updateacademicinfo):
		with dbapi2.connect(config) as connection:
			cursor = connection.cursor()
			new_aca = request.form['name']
			print(new_aca)
			query="""UPDATE ACADEMICINFO set uni_name =%s where uni_name= %s""" % (new_aca,updateacademicinfo)
			cursor.execute(query)
			connection.commit()
			return redirect(url_for('academics'))







