Parts Implemented by Ceyda Aladağ
================================
I implemeted the USER_LOGIN, USER_COMMUNICATION and USER_HOBBIES entities for this project. These entities provide the database for the Profile page. 
All of the operations implemented are listed in below.
OPERATIONS
•	Initialize Tables Method
In this part, database of profile page is begun by using \initdb command and tables of profile page is created. 

•	Add Methods 
This method provide the inserting the new users information to UNICORN website and our database.
•	Delete Methods
This method is used for the deleting user information from the database and website page. 
•	Update Methods
Update methods are used for updateing the information of users with the new information. 
•	Search Methods
Search method selects the required or desired information from the database tables and shows them on the selection list tables. 


PROFILE IMPLEMENTATION
           I designed profile, communication and hobbies classes for the profile page implementation. Profile is the core entity of our database system and is used as a foreign key in other entities and tables. 
PYTHON/SQL CODE 
All of the tables creation are done in this initilalize_profiles() function. And this function is called in the initialize_database() function which in the database.py class. 
 
.. code-block::python

   class Profile:

    #Initialize database tables from beginning, insert some example values
    #Coutnries and Hobbiesa are static tables that are related to user_hobbies and user_communication
    def initialize_profiles(config):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """DROP TABLE IF EXISTS USER_HOBBIES CASCADE;"""
            cursor.execute(query)
            query = """DROP TABLE IF EXISTS USER_LOGIN CASCADE;"""
            cursor.execute(query)
            query = """DROP TABLE IF EXISTS USER_COMMUNICATION CASCADE;"""
            cursor.execute(query)
            query = """DROP TABLE IF EXISTS COUNTRY CASCADE;"""
            cursor.execute(query)
            query = """DROP TABLE IF EXISTS HOBBIES CASCADE;"""
            cursor.execute(query)
            query = """CREATE TABLE IF NOT EXISTS USER_LOGIN (user_id serial primary key, user_loginname VARCHAR(60) UNIQUE NOT NULL, user_password VARCHAR(20) NOT NULL , user_name VARCHAR(30) NOT NULL, user_surname VARCHAR(30) NOT NULL , user_email VARCHAR(120) NOT NULL, user_gender VARCHAR(3) NOT NULL);"""
            cursor.execute(query)
            query = """INSERT INTO USER_LOGIN(user_loginname,user_password,user_name,user_surname,user_email,user_gender) VALUES ('hayra1907','gfb123','oguz','ozcan','asd@gmail.com', 'm'),('ceyda123','ceydaa','ceyda','aladag','ceydag@gmail.com', 'f'),('abv','abv34','anil','berkay','abv@gmail.com', 'm');"""
            cursor.execute(query)
            query = """CREATE TABLE IF NOT EXISTS HOBBIES (hobby_name VARCHAR(60) UNIQUE NOT NULL, hobby_type VARCHAR(200) NOT NULL);"""
            cursor.execute(query)
            query = """INSERT INTO HOBBIES VALUES ('Reading','Indoor casual hobbies') ,('Watching TV','Indoor casual hobbies') ,('Family Time','Indoor casual hobbies') ,('Going to Movies','Indoor casual hobbies') ,('Fishing','Indoor casual hobbies') ,('Computer','Indoor casual hobbies') ,('Gardening','Indoor casual hobbies') ,('Renting Movies','Indoor casual hobbies') ,('Walking','Outdoors') ,('Exercise','Outdoors') ,('Listening to Music','Outdoors') ,('Entertaining','Outdoors') ,('Hunting','Outdoors') ,('Team Sports','Outdoors') ,('Shopping','Outdoors') ,('Traveling','Outdoors') ,('Sleeping','Indoor casual hobbies') ,('Socializing','Outdoors') ,('Sewing','Outdoors') ,('Golf','Competition hobbies') ,('Church Activities','Competition hobbies') ,('Relaxing','Indoor casual hobbies') ,('Playing Music','Indoor casual hobbies') ,('Housework','Indoor casual hobbies') ,('Crafts','Indoor casual hobbies') ,('Watching Sports','Competition hobbies') ,('Bicycling','Competition hobbies') ,('Playing Cards','Competition hobbies') ,('Hiking','Competition hobbies') ,('Cooking','Observation hobbies') ,('Eating Out','Observation hobbies') ,('Dating Online','Observation hobbies') ,('Swimming','Observation hobbies') ,('Camping','Observation hobbies') ,('Skiing','Observation hobbies') ,('Working on Cars','Observation hobbies') ,('Writing','Observation hobbies') ,('Boating','Observation hobbies') ,('Motorcycling','Observation hobbies') ,('Animal Care','Observation hobbies') ,('Bowling','Competition hobbies') ,('Painting','Competition hobbies') ,('Running','Competition hobbies') ,('Dancing','Competition hobbies') ,('Horseback Riding','Competition hobbies') ,('Tennis','Competition hobbies') ,('Theater','Competition hobbies') ,('Billiards','Competition hobbies') ,('Beach','Competition hobbies') ,('Volunteer Work','Competition hobbies');"""
            cursor.execute(query)
            query = """CREATE TABLE IF NOT EXISTS COUNTRY (country_code VARCHAR(60) UNIQUE NOT NULL, country_name VARCHAR(200) NOT NULL);"""
            cursor.execute(query)
            query = """INSERT INTO COUNTRY VALUES
            ('AF','Afghanistan') ,('AX','Aland Islands') ,('AL','Albania') ,('DZ','Algeria') ,('AS','American Samoa') ,('AD','Andorra') ,('AO','Angola') ,('AI','Anguilla') ,('AQ','Antarctica') ,('AG','Antigua and Barbuda') ,('AR','Argentina') ,('AM','Armenia') ,('AW','Aruba') ,('AU','Australia') ,('AT','Austria') ,('AZ','Azerbaijan') ,('BS','Bahamas') ,('BH','Bahrain') ,('BD','Bangladesh') ,('BB','Barbados') ,('BY','Belarus') ,('BE','Belgium') ,('BZ','Belize') ,('BJ','Benin') ,('BM','Bermuda') ,('BT','Bhutan') ,('BO','Bolivia, Plurinational State of') ,('BQ','Bonaire, Sint Eustatius and Saba') ,('BA','Bosnia and Herzegovina') ,('BW','Botswana') ,('BV','Bouvet Island') ,('BR','Brazil') ,('IO','British Indian Ocean Territory') ,('BN','Brunei Darussalam') ,('BG','Bulgaria') ,('BF','Burkina Faso') ,('BI','Burundi') ,('KH','Cambodia') ,('CM','Cameroon') ,('CA','Canada') ,('CV','Cape Verde') ,('KY','Cayman Islands') ,('CF','Central African Republic') ,('TD','Chad') ,('CL','Chile') ,('CN','China') ,('CX','Christmas Island') ,('CC','Cocos (Keeling) Islands') ,('CO','Colombia') ,('KM','Comoros') ,('CG','Congo') ,('CD','Congo, the Democratic Republic of the') ,('CK','Cook Islands') ,('CR','Costa Rica') ,('CI','Cote dIvoire') ,('HR','Croatia') ,('CU','Cuba') ,('CW','Curacao') ,('CY','Cyprus') ,('CZ','Czech Republic') ,('DK','Denmark') ,('DJ','Djibouti') ,('DM','Dominica') ,('DO','Dominican Republic') ,('EC','Ecuador') ,('EG','Egypt') ,('SV','El Salvador') ,('GQ','Equatorial Guinea') ,('ER','Eritrea') ,('EE','Estonia') ,('ET','Ethiopia') ,('FK','Falkland Islands (Malvinas)') ,('FO','Faroe Islands') ,('FJ','Fiji') ,('FI','Finland') ,('FR','France') ,('GF','French Guiana') ,('PF','French Polynesia') ,('TF','French Southern Territories') ,('GA','Gabon') ,('GM','Gambia') ,('GE','Georgia') ,('DE','Germany') ,('GH','Ghana') ,('GI','Gibraltar') ,('GR','Greece') ,('GL','Greenland') ,('GD','Grenada') ,('GP','Guadeloupe') ,('GU','Guam') ,('GT','Guatemala') ,('GG','Guernsey') ,('GN','Guinea') ,('GW','Guinea-Bissau') ,('GY','Guyana') ,('HT','Haiti') ,('HM','Heard Island and McDonald Islands') ,('VA','Holy See (Vatican City State)') ,('HN','Honduras') ,('HK','Hong Kong') ,('HU','Hungary') ,('IS','Iceland') ,('IN','India') ,('ID','Indonesia') ,('IR','Iran, Islamic Republic of') ,('IQ','Iraq') ,('IE','Ireland') ,('IM','Isle of Man') ,('IL','Israel') ,('IT','Italy') ,('JM','Jamaica') ,('JP','Japan') ,('JE','Jersey') ,('JO','Jordan') ,('KZ','Kazakhstan') ,('KE','Kenya') ,('KI','Kiribati') ,('KP','Korea Democratic Peoples Republic of') ,('KR','Korea Republic of') ,('KW','Kuwait') ,('KG','Kyrgyzstan') ,('LA','Lao Peoples Democratic Republic') ,('LV','Latvia') ,('LB','Lebanon') ,('LS','Lesotho') ,('LR','Liberia') ,('LY','Libya') ,('LI','Liechtenstein') ,('LT','Lithuania') ,('LU','Luxembourg') ,('MO','Macao') ,('MK','Macedonia, the former Yugoslav Republic of') ,('MG','Madagascar') ,('MW','Malawi') ,('MY','Malaysia') ,('MV','Maldives') ,('ML','Mali') ,('MT','Malta') ,('MH','Marshall Islands') ,('MQ','Martinique') ,('MR','Mauritania') ,('MU','Mauritius') ,('YT','Mayotte') ,('MX','Mexico') ,('FM','Micronesia, Federated States of') ,('MD','Moldova, Republic of') ,('MC','Monaco') ,('MN','Mongolia') ,('ME','Montenegro') ,('MS','Montserrat') ,('MA','Morocco') ,('MZ','Mozambique') ,('MM','Myanmar') ,('NA','Namibia') ,('NR','Nauru') ,('NP','Nepal') ,('NL','Netherlands') ,('NC','New Caledonia') ,('NZ','New Zealand') ,('NI','Nicaragua') ,('NE','Niger') ,('NG','Nigeria') ,('NU','Niue') ,('NF','Norfolk Island') ,('MP','Northern Mariana Islands') ,('NO','Norway') ,('OM','Oman') ,('PK','Pakistan') ,('PW','Palau') ,('PS','Palestinian Territory, Occupied') ,('PA','Panama') ,('PG','Papua New Guinea') ,('PY','Paraguay') ,('PE','Peru') ,('PH','Philippines') ,('PN','Pitcairn') ,('PL','Poland') ,('PT','Portugal') ,('PR','Puerto Rico') ,('QA','Qatar') ,('RE','Reunion') ,('RO','Romania') ,('RU','Russian Federation') ,('RW','Rwanda') ,('BL','Saint Barthelemy') ,('SH','Saint Helena, Ascension and Tristan da Cunha') ,('KN','Saint Kitts and Nevis') ,('LC','Saint Lucia') ,('MF','Saint Martin (French part)') ,('PM','Saint Pierre and Miquelon') ,('VC','Saint Vincent and the Grenadines') ,('WS','Samoa') ,('SM','San Marino') ,('ST','Sao Tome and Principe') ,('SA','Saudi Arabia') ,('SN','Senegal') ,('RS','Serbia') ,('SC','Seychelles') ,('SL','Sierra Leone') ,('SG','Singapore') ,('SX','Sint Maarten (Dutch part)') ,('SK','Slovakia') ,('SI','Slovenia') ,('SB','Solomon Islands') ,('SO','Somalia') ,('ZA','South Africa') ,('GS','South Georgia and the South Sandwich Islands') ,('SS','South Sudan') ,('ES','Spain') ,('LK','Sri Lanka') ,('SD','Sudan') ,('SR','Suriname') ,('SJ','Svalbard and Jan Mayen') ,('SZ','Swaziland') ,('SE','Sweden') ,('CH','Switzerland') ,('SY','Syrian Arab Republic') ,('TW','Taiwan, Province of China') ,('TJ','Tajikistan') ,('TZ','Tanzania, United Republic of') ,('TH','Thailand') ,('TL','Timor-Leste') ,('TG','Togo') ,('TK','Tokelau') ,('TO','Tonga') ,('TT','Trinidad and Tobago') ,('TN','Tunisia') ,('TR','Turkey') ,('TM','Turkmenistan') ,('TC','Turks and Caicos Islands') ,('TV','Tuvalu') ,('UG','Uganda') ,('UA','Ukraine') ,('AE','United Arab Emirates') ,('GB','United Kingdom') ,('US','United States') ,('UM','United States Minor Outlying Islands') ,('UY','Uruguay') ,('UZ','Uzbekistan') ,('VU','Vanuatu') ,('VE','Venezuela, Bolivarian Republic of') ,('VN','Viet Nam') ,('VG','Virgin Islands, British') ,('VI','Virgin Islands, U.S.') ,('WF','Wallis and Futuna') ,('EH','Western Sahara') ,('YE','Yemen') ,('ZM','Zambia') ,('ZW','Zimbabwe');"""
            cursor.execute(query)
            query = """CREATE TABLE IF NOT EXISTS USER_COMMUNICATION (user_loginname VARCHAR(60) REFERENCES USER_LOGIN(user_loginname) UNIQUE NOT NULL, user_nationality VARCHAR(60) NOT NULL , user_living_country VARCHAR(60) REFERENCES COUNTRY(country_code) NOT NULL, user_living_city VARCHAR(60) NOT NULL, user_telephonenumber VARCHAR(60) NOT NULL, user_birthday VARCHAR(60) NOT NULL);"""
            cursor.execute(query)
            query = """CREATE TABLE IF NOT EXISTS USER_HOBBIES (user_loginname VARCHAR(60) REFERENCES USER_LOGIN(user_loginname) NOT NULL, user_hobby VARCHAR(60) REFERENCES HOBBIES(hobby_name) NOT NULL, PRIMARY KEY(user_loginname,user_hobby) );"""
            cursor.execute(query)
            connection.commit();
            
            import json
            import os
            import psycopg2 as dbapi2
            import re
            from flask import Flask, request, render_template, redirect
            from flask.helpers import url_for
            from flask import Flask, request, render_template
            from Profile import Profile as profile
            from Interaction_c import Interaction_c
            from tweets import tweets as tweet
            from favorites import favorites as favorite
            from university import university as university


            app = Flask(__name__)


            def initialize_database(config):
                with dbapi2.connect(config) as connection:
                     cursor = connection.cursor()
                     profile.initialize_profiles(config)
                     Interaction_c.initialize_interaction(config)
                     connection.commit();
                     return 'tables are created <a href="http://itucsdb1601.mybluemix.net">Home</a>'
 

HTML 
This is the HTML code for home of profile page.

.. code-block:: python
   
    <body>
    <div class="container">
        <h2>Profile</h2>
      <div class="header clearfix">
        <nav>
          <ul class="nav nav-pills pull-right">
           <li role="presentation" class="active"><a href="{{ url_for('home_page') }}">Home</a></li>
           <li role="presentation" class="active"><a href="{{ url_for('login') }}">Sign Up</a></li>
           <li role="presentation" class="active"><a href="{{ url_for('communication_edit') }}">Edit Personal Information</a></li>
           <li role="presentation" class="active"><a href="{{ url_for('hobbies_edit') }}">Edit Hobbies</a></li>
          </ul>
        </nav>
      </div>

   <form action="{{ url_for('profiles') }}" method = "post">
  <table id="usersTable" class="table">
    <thead>
      <tr>
        <th>User Login</th>
        <th>Name</th>
        <th>Surname</th>
        <th>E-mail</th>
		<th>Gender</th>
      </tr>
    </thead>
	<tbody>
		{% for user_loginname, user_name, user_surname, user_email, user_gender in users %}
	    <tr>
		<td class="UsersTableItem">{{user_loginname}}</td>
		<td class="UsersTableItem">{{user_name}}</td>
		<td class="UsersTableItem">{{user_surname}}</td>
		<td class="UsersTableItem">{{user_email}}</td>
		{% if user_gender == 'm' %}
		<td class="UsersTableItem">Male</td>
		{% endif %}
		{% if user_gender == 'f' %}
		<td class="UsersTableItem">Female</td>
		{% endif %}
		<td class="UsersTableItem"><a href="{{ url_for('profile_delete', deleteuserlogin=user_loginname) }}">Delete</a>
		<td class="UsersTableItem"><a href="{{ url_for('profile_update', updateuserlogin=user_loginname) }}">Update</a>
	     </tr>
		{% endfor %}
	</tbody>
  </table>
 
USER_LOGIN TABLE
USER_LOGIN table includes the 7 columns with that names:
user_id: serial primary key, unique not null
user_loginname: varchar(60), unique not null
user_name: varchar(30), not null
user_surname: varchar(30), not null
user_password: varchar(20), not null
user_email: varchar(120), not null
user_gender: varchar(3), not null
user_loginname is reference for USER_COMMUNICTION and USER_HOBBIES tables. . User_id column is serial primary key and this id’s are unique. Also, user_loginname is the unique so there is no user name with the same the other one.

Add Method for USER_LOGIN
This method enaables the sign up to website for users. As a default, all columns values are None. Then with ‘POST’ method, values are taken from users and inserted the USER_LOGIN table by using insert into command. 

.. code-block:: python
   
    def saveuser(config):
        user_name = None
        user_surname = None
        user_loginname = None
        user_password = None
        user_email = None
        user_gender = None
        if request.method == 'POST':
            user_name = request.form['name_text']
            print(user_name)
            user_surname = request.form['surname_text']
            print(user_surname)
            user_loginname = request.form['loginname_text']
            print(user_loginname)
            user_password = request.form['password_text']
            print(user_password)
            user_email = request.form['email_text']
            print(user_email)
            user_gender = request.form['gender']
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                if(user_gender == 'Male'):
                    query = """INSERT INTO USER_LOGIN(user_loginname,user_password,user_name,user_surname,user_email,user_gender) VALUES (%s,%s,%s,%s,%s,%s);"""
                    cursor.execute(query, (user_loginname, user_password, user_name, user_surname, user_email,'m'))
                else:
                    query = """INSERT INTO USER_LOGIN(user_loginname,user_password,user_name,user_surname,user_email,user_gender) VALUES (%s,%s,%s,%s,%s,%s);"""
                    cursor.execute(query, (user_loginname, user_password, user_name, user_surname, user_email,'f'))
                connection.commit();
                return redirect(url_for('login'))


Delete Method for USER_LOGIN
User name which desired to be deleted is taken from by using deleteuserlogin and matched user names are deleted from 3 tables which in the profile database because the user_loginname is reference and delete from the references values on other tables. 

.. code-block:: python
   
    def users_page_db_delete(config, deleteuserlogin):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM user_hobbies where user_loginname = %s"
            cursor.execute(query, (deleteuserlogin,))
            query = "DELETE FROM user_communication where user_loginname = %s"
            cursor.execute(query, (deleteuserlogin,))
            query = "DELETE FROM user_login where user_loginname = %s"
            cursor.execute(query, (deleteuserlogin,))
            connection.commit();
            return redirect(url_for('profiles'))


Update Method for USER_LOGIN
User_loginname is updated with the using updateuserlogin. If the entered user names are equals then new name is entered by the admin and user name is changed with the new name. 
Because the being foreign key of user_loginname, user names of all tables are changed with the this update operation. Besides, add and drop constraints are set for the USER_COMMUNICATION and USER_HOBBIES tables with the user_loginname foreign keys.

.. code-block:: python
   
    def users_page_db_update(config, updateuserlogin):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """SELECT user_loginname from user_login where user_loginname = '%s'""" % (updateuserlogin)
            cursor.execute(query)
            connection.commit();
            return render_template('profiles_edit.html', logins=cursor)
            
    def users_page_db_update_apply(config, updateuserlogin):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            new_name = request.form['name']
            query = """ALTER TABLE user_communication DROP CONSTRAINT user_communication_user_loginname_fkey"""
            cursor.execute(query)
            query = """ALTER TABLE user_hobbies DROP CONSTRAINT user_hobbies_user_loginname_fkey"""
            cursor.execute(query)
            query = """UPDATE user_hobbies set user_loginname ='%s' where user_loginname = '%s'""" % (new_name, updateuserlogin)
            cursor.execute(query)
            query = """UPDATE user_communication set user_loginname ='%s' where user_loginname = '%s'""" % (new_name, updateuserlogin)
            cursor.execute(query)
            query = """UPDATE user_login set user_loginname ='%s' where user_loginname = '%s'""" % (new_name, updateuserlogin)
            cursor.execute(query)
            query = """ALTER TABLE user_hobbies ADD CONSTRAINT user_hobbies_user_loginname_fkey FOREIGN KEY(user_loginname) REFERENCES user_login(user_loginname);"""
            cursor.execute(query)
            query = """ALTER TABLE user_communication ADD CONSTRAINT user_communication_user_loginname_fkey FOREIGN KEY(user_loginname) REFERENCES user_login(user_loginname);"""
            cursor.execute(query)
            connection.commit();
            return redirect(url_for('profiles'))
   
 

Select Method for USER_LOGIN
By using the ‘GET’ method, required columns are selected from the USER_LOGIN table and showed on the profile page with the selection table.
 
.. code-block:: python
   
   def users_page_db(config):
        with dbapi2.connect(config) as connection:
            if request.method == 'GET':
                cursor = connection.cursor()
                query = "SELECT user_loginname,user_name,user_surname,user_email,user_gender from user_login"
                cursor.execute(query)
                connection.commit();
                return render_template('profiles.html', users=cursor)


USER_COMMUNICATION TABLE 

This table keep the personal information values of registered people in our website database.
If the non existing user_loginname is entered for any operation such as insert, delete,update, these operation can not be made. This is the cascade situation with these restrictions. 

user_loginname: foreign key, unique not null
user_nationality: varchar(60), not null
user_living_country: foreign key, varchar(60), not null
user_living_city: varchar(60), not null
user_telephonenumber: varchar(60), not null
user_birthday: varchar(60), not null

COUNTRY TABLE
This table is the static table which came from the database when the database is started in every time.
country_code: unique, varchar(60),  not null
country_name: varchar(200),  not null

Add and Update Method for USER_COMMUNICATION
Required information are taken from the users and ıf the non existing personal information with this user name, these personal information are added to an USER_COMMUNICATION table. If the existing personal information with this user name, then personal information of this person are updated. This control is provided by the Select 1 command. This operation can be named as UPSERT operation.
 
.. code-block:: python

   class Communication:

   def users_page_db_communication_information_apply(config):
            username = request.form['user_name']
            nationality = request.form['nationality']
            print(nationality)
            country = request.form['country']
            livingcity = request.form['livingcity_text']
            telephone_number = request.form['telephonenumber_text']
            datepicker = request.form['datepicker']

            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    #Query works in the way that update if exists, if doesn't exist insert as new row.
                    query = """UPDATE USER_COMMUNICATION SET user_loginname='%s', user_nationality = '%s',
                user_living_country='%s',user_living_city='%s',user_telephonenumber='%s',user_birthday='%s' WHERE
                user_loginname='%s'""" % (username, nationality, country, livingcity, telephone_number, datepicker,username)
                    cursor.execute(query)
                    query= """INSERT INTO USER_COMMUNICATION
                       (user_loginname, user_nationality, user_living_country ,user_living_city,user_telephonenumber,user_birthday)
                        SELECT '%s','%s','%s','%s','%s','%s' WHERE NOT EXISTS (SELECT 1 FROM USER_COMMUNICATION WHERE user_loginname='%s')"""% (username, nationality, country, livingcity, telephone_number,datepicker,username)
                    cursor.execute(query)
                    connection.commit();
                except Exception as e:
                    return "There is no user with that name <a href='http://itucsdb1601.mybluemix.net/profiles'>Profiles</a>"
                else:
                    return redirect(url_for('communication_edit'))


Delete Method for USER_COMMUNICATION
User name which entered the text box in delete operation on page is taken and if the matching is provided between user names is deleted. If there is no matching with two user names function returns the warning message. 

.. code-block:: python

    def users_page_db_communication_information_delete(config):
        username = request.form['user_name_del']
        with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                query="DELETE FROM user_communication where user_loginname = %s"
                cursor.execute(query, (username,))
                connection.commit();
                if cursor.rowcount == 0:
                    return "There is no personal info for this user <a href='http://itucsdb1601.mybluemix.net/profiles'>Profiles</a>"
                else:
                    return redirect(url_for('communication_edit'))

Search Method for USER_COMMUNICATION
Join operation is done between the USER_COMMUNICATION and COUNTRY tables. After that, desired colums are selected from the join table and showed the personal info list selection table. 

.. code-block:: python
 
   def users_page_db_communication_information_select(config):
         with dbapi2.connect(config) as connection:
            if request.method == 'GET':
                cursor = connection.cursor()
                query = "SELECT d.user_loginname,d.user_nationality,c.country_code,d.user_living_city,d.user_telephonenumber,d.user_birthday FROM user_communication d, country c where d.user_living_country = c.country_code"
                cursor.execute(query)
                comm_list = cursor.fetchall()
                query = "SELECT country_code,country_name from COUNTRY"
                cursor.execute(query)
                country_list = cursor.fetchall()
                connection.commit();
                return render_template('communication_edit.html', countries = country_list, communications=comm_list)

USER_HOBBIES TABLE
This table includes the hobbies and hobby types of users with their user_loginname. 
user_loginname: primary key, foreign key, not null
user_hobby: primary key, foreign key, not null

HOBBIES TABLE
This table is the static table which came from the database when the database is started in every time.
hobby_name: unique, varchar(60), not null
hobby_type: varchar(60), not null

Add and Update Method for USER_HOBBIES
Desired user name which is also exist in USER_LOGIN table is taken as a request. Hobby_name is selected from dropdown bar. If the non existing hobby name with this user name, these hobbies are added to an USER_HOBBIES table. If the existing hobbies with this user name, then hobbies of this person are updated. This control is provided by the Select 1 command. One person have an one or more than hobbies for herself/itself thanks to the primary key pairs of the user_loginname and user_hobby.
 
.. code-block:: python
   
   def users_page_db_hobby_information_apply(config):
        username = request.form['user_name']
        hobby = request.form['hobby']

        with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    query = """UPDATE USER_HOBBIES SET user_loginname='%s', user_hobby = '%s' WHERE
                    user_loginname='%s' AND user_hobby='%s' """ % (username, hobby,username,hobby)
                    cursor.execute(query)
                    query= """INSERT INTO USER_HOBBIES
                       (user_loginname, user_hobby)
                        SELECT '%s','%s' WHERE NOT EXISTS (SELECT 1 FROM USER_HOBBIES WHERE user_loginname='%s' AND user_hobby='%s')"""% (username, hobby, username, hobby)
                    cursor.execute(query)
                    connection.commit();
                except Exception as e:
                    return "There is no user with that name <a href='http://itucsdb1601.mybluemix.net/profiles'>Profiles</a>"
                else:
                    return redirect(url_for('hobbies_edit'))

Delete Method for USER_HOBBIES 
User name which entered the text box in delete operation on page is taken and hobby is selected from the dropdown. If the matching is provided between user names and hobby, this person is deleted by the admin. If there is no matching with two user names function returns the warning message. 

.. code-block:: python

   def users_page_db_hobby_information_delete(config):
        username = request.form['user_name_del']
        hobby_name = request.form['hobby_sel']
        with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                query="DELETE FROM user_hobbies where user_loginname = %s AND user_hobby=%s"
                cursor.execute(query, (username,hobby_name))
                connection.commit();
                if cursor.rowcount == 0:
                    return "There is no user and hobby with that user hobby pair <a href='http://itucsdb1601.mybluemix.net/profiles'>Profiles</a>"
                else:
                    return redirect(url_for('hobbies_edit'))


Search Method for USER_HOBBIES 

Join operation is done between the USER_HOBBIES and HOBBIES tables. After that, desired colums are selected from the join table and showed the hobby list selection table. Hobby type of hobbies is also shown in the hobby list because of the join operation.

.. code-block:: python

   class Hobby:

   
    def users_page_db_hobby_information_select(config):
         with dbapi2.connect(config) as connection:
            if request.method == 'GET':
                cursor = connection.cursor()
                query = "SELECT hobby_name, hobby_type from HOBBIES"
                cursor.execute(query)
                hobby_list = cursor.fetchall()
                query = "SELECT b.user_loginname,a.hobby_name, a.hobby_type from HOBBIES a, USER_HOBBIES b where a.hobby_name = b.user_hobby"
                cursor.execute(query)
                user_hobby_list = cursor.fetchall()
                connection.commit();
                return render_template('hobbies_edit.html',hobbies = hobby_list, user_hobbies = user_hobby_list)


