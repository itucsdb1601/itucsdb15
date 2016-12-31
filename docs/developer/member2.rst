Parts Implemented by Ozan Ozcan
================================
The classes created by Ozan Özcan are universities, academics and unisports. All of the classes have the same header in order to import and implement the functionality of json, psycopg2 and flask. url_for will be used to redirect pages.

.. code-block:: python
   import json
  import os
  import psycopg2 as dbapi2
  import re
  from flask import Flask, request, render_template, redirect
  from flask.helpers import url_for

  app = Flask(__name__)
  
The tables will be dropped and re-created every time the database is initialized. Dropping operation is done to prevent any errors in table creation.

.. code-block:: python

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
   
      
      
With the following query and subsequent cursor.execute(query) command, the first table of the class, which is university list, is created. This table has 5 attributes.

.. code-block:: python

  query = """CREATE TABLE IF NOT EXISTS UNIVERSITYLIST (uni_id serial primary key, unicity_id VARCHAR(60) NOT NULL, uni_name  VARCHAR(80)   NOT NULL, unitype_id VARCHAR(80) NOT NULL, startdate VARCHAR(80) NOT NULL);"""
			cursor.execute(query)

- uni_id serial primary key: This is the primary key of the table. Each time a tuple is created in this table, uni_id will be incremented. For example, if the last element of the table has an id of 4, the subsequent entry to this table will have an uni_id of 5.

- unicity_id VARCHAR(60) NOT NULL: This value was initially an integer. But we have encountered some problems while trying to fetch data from user in html page as an integer. For our project to run in Bluemix without any issues, this value was switched to VARCHAR and takes a string as input. Originally, it would take an integer and then this integer would be used in another table. It is not null so there will be an error if this id is left blank in initial elements or when a user is trying to enter a new tuple to this list.

- uni_name VARCHAR(80) NOT NULL: This is the most important attribute of the table. This table is connected to other tables via uni_name. uni_name will hold the name of the university and obviously shouldn't be left blank.

- unitype_id VARCHAR(80) NOT NULL: Like city id number, this was also an integer converted to string to not break the website. The database will take the id and use it to elaborate on which category this particular university is considered in.

- startdate VARCHAR(80) NOT NULL: Another integer converted to string. The date the university is founded is stored in this attribute.

.. code-block:: python

  query = """INSERT INTO UNIVERSITYLIST(uni_name, unitype_id, unicity_id, startdate) VALUES ('Istanbul Technical University','1','34',      '1773'), ('Harvard University', '5', '999', '1850'), ('Mersin University','2','33', '1933'), ('Mimar Sinan Fine Arts University', '3',    '34', '1802'), ('SUNY Buffalo', '5', '999', '1898');"""
			cursor.execute(query)
			connection.commit();

To make sure the insert operations were done, all of the tables which will be created will have a few tuples inserted in them. Each time the database is initialized, these values are restored and presented in the html file.

.. code-block:: python

			query = """CREATE TABLE IF NOT EXISTS UNIVERSITYTYPE (type_id serial primary key, unitype VARCHAR(80) NOT NULL);"""
			cursor.execute(query)

Universitytype table consists of two attributes. It was planned to take the unitype_id from the Universitylist table and give the necessary information about the type of the university in this table

- type_id serial primary key

- unitype: This attribute contains the explanation of the type.

.. code-block:: python 

			query = """INSERT INTO UNIVERSITYTYPE (unitype) VALUES ('Public Technical University'), ('Public University'), ('Sports and Arts University'), ('Private University'), ('Foreign University');"""
			cursor.execute(query)
      
.. code-block:: python 

			query = """CREATE TABLE IF NOT EXISTS UNICITY (city_id INTEGER, city_name VARCHAR(80) NOT NULL);"""
			cursor.execute(query)

Unicity table also has two attributes and will list the cities in which the universities are located. If it is a unversity based in Turkey, it's city licence plate number will be its unicity id, if it is a foreign university it's default value is 999.

.. code-block:: python 

  query = """INSERT INTO UNICITY VALUES (34,'Istanbul'), (35,'Izmir'), (999,'Foreign'), (33, 'Mersin'),(6,'Ankara'), (1,'Adana'), (7,'Antalya');"""
			cursor.execute(query)

If a university with a different city code is added to the Universitylist table, the code and the city name should be added to this table.

.. code-block:: python

			query = """CREATE TABLE IF NOT EXISTS UNIPOPULARITY (popularity_id INTEGER  primary key, uni_name VARCHAR(80) NOT NULL, totalscore INTEGER, totalusers INTEGER NOT NULL);"""
			cursor.execute(query)

  
Unipopularity table has four attributes.
  
- popularity_id integer primary key

- uni_name VARCHAR(80) NOT NULL

- totalscore INTEGER

- totalusers INTEGER NOT NULL

	Popularity of a university will be evaluated in this table. The total users enrolled in a certain university will be held. The total score is an algorithm calculated by the votes users will give to a certain university, and their academic and athletic accomplishments.
  

.. code-block:: python

			query = """INSERT INTO UNIPOPULARITY VALUES	(15, 'Gazi University', 10954, 322), (22, 'Izmir University', 2559, 210);"""
			cursor.execute(query)
			connection.commit();
			return 'University Tables Created <a href="http://localhost:5000">Home</a>'
      
      
      
After the last commit, a blank page will open in the browser saying that the tables are created for this class.

.. code-block:: python

	def universities_page(config):
		with dbapi2.connect(config) as connection:
			if request.method == 'GET':
				cursor = connection.cursor()
				query = "SELECT uni_name, startdate from UNIVERSITYLIST"
				cursor.execute(query)
				return render_template('universities.html', unis=cursor)
        

After the table creation operation is processed, certain methods for this class is written. The first method universities_page is used to get data from Universitylist table to be used in universities main html page. 

.. code-block:: python 

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
        
 
The method shown above will be used to get necessary information to add a new university to the database. This method will be used in university_add.html page.

.. code-block:: python
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
				return 'update is done'
        
        
Delete and update methods are implemented in the universities main page. There are links for delete and update in table where universities are listed. When delete is pressed, the delete method will delete the selected university. When update is pressed, universities_edit.html page will open and the user will update the selected university. The apply method is used to save the changes made.


UNISPORTS:

.. code-block:: python

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
            
The unisports class is initialized in this method. The tables are dropped to be created in initialization.

.. code-block:: python

            query = """CREATE TABLE IF NOT EXISTS UNITEAMS (team_id serial primary key, uni_name VARCHAR(80) UNIQUE NOT NULL, team_name VARCHAR(50) NOT NULL);"""
            cursor.execute(query)
 
 
The first table of this class is Uniteams. This table has 3 attributes.

- team_id serial primary key

- uni_name VARCHAR(80) UNIQUE NOT NULL

- team_name VARCHAR(50) UNIQUE NOT NULL

	This table will list the team names of the affiliated university.
  
.. code-block:: python

            query = """INSERT INTO UNITEAMS (uni_name, team_name) VALUES ('Istanbul Technical University','Hornets'), ('Harvard University', 'Crimson'), ('Mersin University','Mustangs'), ('SUNY Buffalo', 'Bulls'), ('Bogazici University', 'Sultans');"""
            cursor.execute(query)
            
.. code-block:: python
            query = """CREATE TABLE IF NOT EXISTS UNILEAGUES (league_id serial primary key, league_name VARCHAR(80) UNIQUE NOT NULL, country_id INTEGER    NOT NULL);"""
            cursor.execute(query)
            
The unileagues table will be used to list the different teams that belongs to this university. This table has 3 attributes.

- league_id serial primary key

- league_name VARHCAR(80) UNIQUE NOT NULL: the team must be playing in a unique league. 2 teams from same university cannot play in the same league. 

- country_id INTEGER NOT NULL: used to determine if the team is playing in a domestic or international competition.

.. code-block:: python
            query = """INSERT INTO UNILEAGUES (league_name, country_id) VALUES ('NCAA Football Bowl Subdivision', 5), ('Istanbul Basketbol Ligi', 90), ('Universiteler Spor Ligi', 90), ('IFAF Europe Champions League', 5);"""
            cursor.execute(query)
            
As it can be seen from this example, different leagues with respective country codes are listed.

.. code-block:: python
            query = """CREATE TABLE IF NOT EXISTS COMPETITION (id serial primary key, country_id INTEGER NOT NULL, competition_type VARCHAR(80) NOT NULL);"""
            cursor.execute(query)
This table has 3 attributes; id, country_id and competition_type. 

.. code-block:: python

            query = """INSERT INTO COMPETITION (country_id, competition_type) VALUES (90, 'Domestic Intercollegiate'), (5, 'Foreign Tournament');"""
            connection.commit()
            return 'University Sport Tables Created <a href="http://localhost:5000">Home</a>'
            
After the last table of this class is created, the app will post a message informing the successful table creations.



.. code-block:: python 

    def unisports_page(config):
        with dbapi2.connect(config) as connection:
            if request.method == 'GET':
                cursor = connection.cursor()
                query = "SELECT uni_name, team_name from UNITEAMS"
                cursor.execute(query)
                return render_template('unisports.html', unispo=cursor)
                
 
 
This method is used to initialize the unisports main page and present the uniteams table in unisports.html page.

.. code-block:: python

    def saveuniteam(config):
        uni_name = None
        team_name = None
        if request.method == 'POST':
            uni_name = request.form['uniname_text']
            team_name = request.form['teamname_text']
            with dbapi2.connection(config) as connection:
                cursor = connection.cursor()
                return redirect(url_for('unisports_add'))

This method is used to add a new uniteam to the uniteams table when unisports_add.html page is opened.

.. code-block:: python

    def unisports_page_delete(config, deleteuniteam):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """DELETE FROM UNITEAMS WHERE uni_name=%s"""
            cursor.execute(query, (deleteuniteam,))
            connection.commit();
            return redirect(url_for('unisports'))
            
This method is embedded in the University Sports Database page. When user clicks on the delete link, this method will run and delete the selected tuple.

.. code-block:: python

    def unisports_page_update(config, updateuniteam):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """SELECT uni_name from UNITEAMS WHERE uni_name = '%s'""" % (updateuniteam)
            cursor.execute(query)
            connection.commit();
            return render_template('unisports_edit.html', unispo=cursor)
            
This method will run in the unisports_edit.html page. When necessary changes are made, this method ensures that these changes are saved.

.. code-block:: python

    def unisports_page_update_apply(config,updateuniteam):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            new_uniteam = request.form['name']
            print(new_uniteam)
            query="""UPDATE UNITEAMS set uni_name =%s where uni_name= '%s'""" % (new_uniteam,updateuniteam)
            cursor.execute(query)
            connection.commit()
            return redirect(url_for('unisports'))
   
This method will run in unisports_edit page.


ACADEMICS:

.. code-block:: python

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



The final class is academics and it is initialized. The tables desired to be created are dropped first.


.. code-block:: python

			query = """CREATE TABLE IF NOT EXISTS ACADEMICINFO (id serial primary key, uni_name VARCHAR(80) UNIQUE NOT NULL, level VARCHAR(50) NOT NULL, scholarship VARCHAR(3) NOT NULL , mainresearch VARCHAR(100) NOT NULL, researchbudget VARCHAR(50) NOT NULL);"""
			cursor.execute(query)

The first table of this class is academicinfo. It has 6 attributes.

- id serial primary key

- uni_name VARCHAR(80) NOT NULL

- level VARCHAR(50) NOT NULL: the level of the university is determined by an algorithm

- scholarship VARCHAR(3) NOT NULL: this will indicate if the university has scholarship opportunities or not.

- mainresearch VARCHAR(100) NOT NULL: this will explain the main research area of the university for the students who plan to specialize on this.

- researchbudget: this attribute gives an estimate on how much the budget is for this university

.. code-block:: python

			query = """INSERT INTO ACADEMICINFO (uni_name, level, scholarship, mainresearch, researchbudget) VALUES ('Istanbul Technical University', 3, 'y', 'Daylight Saving Time', 50000000), ('Harvard University', '1', 'y', 'Nobel Research', '100'), ('Mersin University','5', 'n', 'Agricultural Developments', '3000000');"""
			cursor.execute(query)
            
This table will be presented in the academics.html page.  

.. code-block:: python

			query = """CREATE TABLE IF NOT EXISTS SCHOLARSHIPS (scholarship_id serial primary key, scholarshiptype VARCHAR(50) NOT NULL, scholarshipname VARCHAR (100) UNIQUE NOT NULL, scholars INTEGER, money_amount VARCHAR(50) NOT NULL);"""
			cursor.execute(query)
            
            
This table will provide information about the scholarship opportunities for a selected.

university. It has 5 attributes.

- scholarship_id serial primary key

- scholarshiptype VARCHAR(50) NOT NULL: this will indicate the type of the scholarship a student can apply to.

- scholarshipname VARCHAR (100) UNIQUE NOT NULL

- scholars INTEGER: the amount of people who can get this scholarship

- money_amount VARHCAR (50) NOT NULL: the value of this scholarship


.. code-block:: python

			query = """INSERT INTO SCHOLARSHIPS (scholarshiptype, scholarshipname, scholars, money_amount) VALUES ('Tuition', 'KYK', 300, 5000), ('Academic Excellence', 'Fulbright', 10, 300000), ('Athletic Excellence', 'NCAA Scholarship', 500, '40000');"""
			cursor.execute(query)
      
.. code-block:: python
 
			query = """CREATE TABLE IF NOT EXISTS RESDEV (rdtype_id serial primary key, researchtype VARCHAR(50) NOT NULL, researchname VARCHAR(100) NOT NULL);"""
			cursor.execute(query)
      
This table will detail the research and development areas of the selected university. It has 3 attributes.
- rdtype_id serial primary key
- researchtype VARCHAR (50) NOT NULL
- researchname VARCHAR(100) NOT NULL

.. code-block:: python


			query = """INSERT INTO RESDEV (researchtype, researchname) VALUES ('Academic', 'Machine Learning'),('Athletic','Kinesiology in Contact Sports');"""
			cursor.execute(query)
      
.. code-block:: python
 
			query = """CREATE TABLE IF NOT EXISTS LEVELS (id serial primary key, unilevel VARCHAR(50) NOT NULL, leveltype VARCHAR(80) UNIQUE NOT NULL);"""
			cursor.execute(query)
      
This table uses the algorithm created to calculate the level of the university to give a general idea for the students where the university's standing is in a ranking.

.. code-block:: python

			query = """INSERT INTO LEVELS (unilevel, leveltype) VALUES ('1', 'Worldwide Known Top Class University'), ('2', 'Time Magazine top 40 University'), ('3', 'Top Tier Turkish University'), ('4', 'Average Turkish University'), ('5', 'Below Average Turkish University), ('6', 'Non-top tier foreign based University');"""
			connection.commit()
			return 'Academic Tables Created <a href="http://localhost:5000">Home</a>'
      
 
After the last table is created, the app will indicate if the tables are created successfully or not.

.. code-block:: python

	def academics_page(config):
		with dbapi2.connect(config) as connection:
			if request.method == 'GET':
				cursor = connection.cursor()
				query = "SELECT uni_name, level, scholarship , mainresearch , researchbudget from ACADEMICINFO"
				cursor.execute(query)
				return render_template('academics.html', aca=cursor)
     
This method will initialize the academic informations and present it in academics.html.     

.. code-block:: python

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
        
        
This method is executed in academics_add.html page. This is used to ensure the academic information is added to the database if all the values are entered within the constraints

.. code-block:: python

	def academics_page_delete(config, deleteacademicinfo):
		with dbapi2.connect(config) as connection:
			cursor = connection.cursor()
			query = """DELETE FROM ACADEMICINFO WHERE uni_name=%s"""
			cursor.execute(query, (deleteacademicinfo,))
			connection.commit();
			return redirect(url_for('academics'))

This method will run in the academics main page and when delete link is created, this method is executed to delete the selected academic information.

.. code-block:: python

	def academics_page_update(config, updateacademicinfo):
		with dbapi2.connect(config) as connection:
			cursor = connection.cursor()
			query = """SELECT uni_name from ACADEMICINFO WHERE uni_name = %s""" % (updateacademicinfo)
			cursor.execute(query)
			connection.commit();
			return render_template('academics_edit.html', unispo=cursor)


This method will run in the academics_edit.html page. This is used to present the user with a page where he or she can update the necessary information.






.. code-block:: python

	def academics_page_update_apply(config,updateacademicinfo):
		with dbapi2.connect(config) as connection:
			cursor = connection.cursor()
			new_aca = request.form['name']
			print(new_aca)
			query="""UPDATE ACADEMICINFO set uni_name =%s where uni_name= %s""" % (new_aca,updateacademicinfo)
			cursor.execute(query)
			connection.commit()
			return redirect(url_for('academics'))

This method runs in academics_edit.html page and ensure the changes made in this page is saved. The user will return to academics main html page after pressing the save button in the html page.





















































  
  
  




