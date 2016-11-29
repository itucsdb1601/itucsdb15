import json
import os
import psycopg2 as dbapi2
import re
from flask import Flask, request, render_template, redirect
from flask.helpers import url_for

## CEYDA ALADAÐ - 150130283
class Profile:

    #Initialize database tables from beginning, insert some example values
    #Coutnries and Hobbiesa are static tables that are related to user_hobbies and user_communication
    def initialize_profiles(config):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """DROP TABLE IF EXISTS USER_HOBBIES CASCADE"""
            cursor.execute(query)
            connection.commit();
            query = """DROP TABLE IF EXISTS USER_LOGIN CASCADE"""
            cursor.execute(query)
            connection.commit();
            query = """DROP TABLE IF EXISTS USER_COMMUNICATION CASCADE"""
            cursor.execute(query)
            connection.commit();
            query = """DROP TABLE IF EXISTS COUNTRY CASCADE"""
            cursor.execute(query)
            connection.commit();
            query = """DROP TABLE IF EXISTS HOBBIES CASCADE"""
            cursor.execute(query)
            connection.commit();
            query = """CREATE TABLE IF NOT EXISTS USER_LOGIN (user_id serial primary key, user_loginname VARCHAR(60) UNIQUE NOT NULL, user_password VARCHAR(20) NOT NULL , user_name VARCHAR(30) NOT NULL, user_surname VARCHAR(30) NOT NULL , user_email VARCHAR(120) NOT NULL, user_gender VARCHAR(3) NOT NULL)"""
            cursor.execute(query)
            connection.commit();
            query = """INSERT INTO USER_LOGIN(user_loginname,user_password,user_name,user_surname,user_email,user_gender) VALUES ('hayra1907','gfb123','oguz','ozcan','asd@gmail.com', 'm'),('ceyda123','ceydaa','ceyda','aladag','ceydag@gmail.com', 'f'),('abv','abv34','anil','berkay','abv@gmail.com', 'm')"""
            cursor.execute(query)
            connection.commit();
            query = """CREATE TABLE IF NOT EXISTS HOBBIES (hobby_name VARCHAR(60) UNIQUE NOT NULL, hobby_type VARCHAR(200) NOT NULL)"""
            cursor.execute(query)
            connection.commit();
            query = """INSERT INTO HOBBIES VALUES ('Reading','Indoor casual hobbies') ,('Watching TV','Indoor casual hobbies') ,('Family Time','Indoor casual hobbies') ,('Going to Movies','Indoor casual hobbies') ,('Fishing','Indoor casual hobbies') ,('Computer','Indoor casual hobbies') ,('Gardening','Indoor casual hobbies') ,('Renting Movies','Indoor casual hobbies') ,('Walking','Outdoors') ,('Exercise','Outdoors') ,('Listening to Music','Outdoors') ,('Entertaining','Outdoors') ,('Hunting','Outdoors') ,('Team Sports','Outdoors') ,('Shopping','Outdoors') ,('Traveling','Outdoors') ,('Sleeping','Indoor casual hobbies') ,('Socializing','Outdoors') ,('Sewing','Outdoors') ,('Golf','Competition hobbies') ,('Church Activities','Competition hobbies') ,('Relaxing','Indoor casual hobbies') ,('Playing Music','Indoor casual hobbies') ,('Housework','Indoor casual hobbies') ,('Crafts','Indoor casual hobbies') ,('Watching Sports','Competition hobbies') ,('Bicycling','Competition hobbies') ,('Playing Cards','Competition hobbies') ,('Hiking','Competition hobbies') ,('Cooking','Observation hobbies') ,('Eating Out','Observation hobbies') ,('Dating Online','Observation hobbies') ,('Swimming','Observation hobbies') ,('Camping','Observation hobbies') ,('Skiing','Observation hobbies') ,('Working on Cars','Observation hobbies') ,('Writing','Observation hobbies') ,('Boating','Observation hobbies') ,('Motorcycling','Observation hobbies') ,('Animal Care','Observation hobbies') ,('Bowling','Competition hobbies') ,('Painting','Competition hobbies') ,('Running','Competition hobbies') ,('Dancing','Competition hobbies') ,('Horseback Riding','Competition hobbies') ,('Tennis','Competition hobbies') ,('Theater','Competition hobbies') ,('Billiards','Competition hobbies') ,('Beach','Competition hobbies') ,('Volunteer Work','Competition hobbies');"""
            cursor.execute(query)
            connection.commit();
            query = """CREATE TABLE IF NOT EXISTS COUNTRY (country_code VARCHAR(60) UNIQUE NOT NULL, country_name VARCHAR(200) NOT NULL)"""
            cursor.execute(query)
            connection.commit();
            query = """INSERT INTO COUNTRY VALUES
            ('AF','Afghanistan') ,('AX','Aland Islands') ,('AL','Albania') ,('DZ','Algeria') ,('AS','American Samoa') ,('AD','Andorra') ,('AO','Angola') ,('AI','Anguilla') ,('AQ','Antarctica') ,('AG','Antigua and Barbuda') ,('AR','Argentina') ,('AM','Armenia') ,('AW','Aruba') ,('AU','Australia') ,('AT','Austria') ,('AZ','Azerbaijan') ,('BS','Bahamas') ,('BH','Bahrain') ,('BD','Bangladesh') ,('BB','Barbados') ,('BY','Belarus') ,('BE','Belgium') ,('BZ','Belize') ,('BJ','Benin') ,('BM','Bermuda') ,('BT','Bhutan') ,('BO','Bolivia, Plurinational State of') ,('BQ','Bonaire, Sint Eustatius and Saba') ,('BA','Bosnia and Herzegovina') ,('BW','Botswana') ,('BV','Bouvet Island') ,('BR','Brazil') ,('IO','British Indian Ocean Territory') ,('BN','Brunei Darussalam') ,('BG','Bulgaria') ,('BF','Burkina Faso') ,('BI','Burundi') ,('KH','Cambodia') ,('CM','Cameroon') ,('CA','Canada') ,('CV','Cape Verde') ,('KY','Cayman Islands') ,('CF','Central African Republic') ,('TD','Chad') ,('CL','Chile') ,('CN','China') ,('CX','Christmas Island') ,('CC','Cocos (Keeling) Islands') ,('CO','Colombia') ,('KM','Comoros') ,('CG','Congo') ,('CD','Congo, the Democratic Republic of the') ,('CK','Cook Islands') ,('CR','Costa Rica') ,('CI','Cote dIvoire') ,('HR','Croatia') ,('CU','Cuba') ,('CW','Curacao') ,('CY','Cyprus') ,('CZ','Czech Republic') ,('DK','Denmark') ,('DJ','Djibouti') ,('DM','Dominica') ,('DO','Dominican Republic') ,('EC','Ecuador') ,('EG','Egypt') ,('SV','El Salvador') ,('GQ','Equatorial Guinea') ,('ER','Eritrea') ,('EE','Estonia') ,('ET','Ethiopia') ,('FK','Falkland Islands (Malvinas)') ,('FO','Faroe Islands') ,('FJ','Fiji') ,('FI','Finland') ,('FR','France') ,('GF','French Guiana') ,('PF','French Polynesia') ,('TF','French Southern Territories') ,('GA','Gabon') ,('GM','Gambia') ,('GE','Georgia') ,('DE','Germany') ,('GH','Ghana') ,('GI','Gibraltar') ,('GR','Greece') ,('GL','Greenland') ,('GD','Grenada') ,('GP','Guadeloupe') ,('GU','Guam') ,('GT','Guatemala') ,('GG','Guernsey') ,('GN','Guinea') ,('GW','Guinea-Bissau') ,('GY','Guyana') ,('HT','Haiti') ,('HM','Heard Island and McDonald Islands') ,('VA','Holy See (Vatican City State)') ,('HN','Honduras') ,('HK','Hong Kong') ,('HU','Hungary') ,('IS','Iceland') ,('IN','India') ,('ID','Indonesia') ,('IR','Iran, Islamic Republic of') ,('IQ','Iraq') ,('IE','Ireland') ,('IM','Isle of Man') ,('IL','Israel') ,('IT','Italy') ,('JM','Jamaica') ,('JP','Japan') ,('JE','Jersey') ,('JO','Jordan') ,('KZ','Kazakhstan') ,('KE','Kenya') ,('KI','Kiribati') ,('KP','Korea Democratic Peoples Republic of') ,('KR','Korea Republic of') ,('KW','Kuwait') ,('KG','Kyrgyzstan') ,('LA','Lao Peoples Democratic Republic') ,('LV','Latvia') ,('LB','Lebanon') ,('LS','Lesotho') ,('LR','Liberia') ,('LY','Libya') ,('LI','Liechtenstein') ,('LT','Lithuania') ,('LU','Luxembourg') ,('MO','Macao') ,('MK','Macedonia, the former Yugoslav Republic of') ,('MG','Madagascar') ,('MW','Malawi') ,('MY','Malaysia') ,('MV','Maldives') ,('ML','Mali') ,('MT','Malta') ,('MH','Marshall Islands') ,('MQ','Martinique') ,('MR','Mauritania') ,('MU','Mauritius') ,('YT','Mayotte') ,('MX','Mexico') ,('FM','Micronesia, Federated States of') ,('MD','Moldova, Republic of') ,('MC','Monaco') ,('MN','Mongolia') ,('ME','Montenegro') ,('MS','Montserrat') ,('MA','Morocco') ,('MZ','Mozambique') ,('MM','Myanmar') ,('NA','Namibia') ,('NR','Nauru') ,('NP','Nepal') ,('NL','Netherlands') ,('NC','New Caledonia') ,('NZ','New Zealand') ,('NI','Nicaragua') ,('NE','Niger') ,('NG','Nigeria') ,('NU','Niue') ,('NF','Norfolk Island') ,('MP','Northern Mariana Islands') ,('NO','Norway') ,('OM','Oman') ,('PK','Pakistan') ,('PW','Palau') ,('PS','Palestinian Territory, Occupied') ,('PA','Panama') ,('PG','Papua New Guinea') ,('PY','Paraguay') ,('PE','Peru') ,('PH','Philippines') ,('PN','Pitcairn') ,('PL','Poland') ,('PT','Portugal') ,('PR','Puerto Rico') ,('QA','Qatar') ,('RE','Reunion') ,('RO','Romania') ,('RU','Russian Federation') ,('RW','Rwanda') ,('BL','Saint Barthelemy') ,('SH','Saint Helena, Ascension and Tristan da Cunha') ,('KN','Saint Kitts and Nevis') ,('LC','Saint Lucia') ,('MF','Saint Martin (French part)') ,('PM','Saint Pierre and Miquelon') ,('VC','Saint Vincent and the Grenadines') ,('WS','Samoa') ,('SM','San Marino') ,('ST','Sao Tome and Principe') ,('SA','Saudi Arabia') ,('SN','Senegal') ,('RS','Serbia') ,('SC','Seychelles') ,('SL','Sierra Leone') ,('SG','Singapore') ,('SX','Sint Maarten (Dutch part)') ,('SK','Slovakia') ,('SI','Slovenia') ,('SB','Solomon Islands') ,('SO','Somalia') ,('ZA','South Africa') ,('GS','South Georgia and the South Sandwich Islands') ,('SS','South Sudan') ,('ES','Spain') ,('LK','Sri Lanka') ,('SD','Sudan') ,('SR','Suriname') ,('SJ','Svalbard and Jan Mayen') ,('SZ','Swaziland') ,('SE','Sweden') ,('CH','Switzerland') ,('SY','Syrian Arab Republic') ,('TW','Taiwan, Province of China') ,('TJ','Tajikistan') ,('TZ','Tanzania, United Republic of') ,('TH','Thailand') ,('TL','Timor-Leste') ,('TG','Togo') ,('TK','Tokelau') ,('TO','Tonga') ,('TT','Trinidad and Tobago') ,('TN','Tunisia') ,('TR','Turkey') ,('TM','Turkmenistan') ,('TC','Turks and Caicos Islands') ,('TV','Tuvalu') ,('UG','Uganda') ,('UA','Ukraine') ,('AE','United Arab Emirates') ,('GB','United Kingdom') ,('US','United States') ,('UM','United States Minor Outlying Islands') ,('UY','Uruguay') ,('UZ','Uzbekistan') ,('VU','Vanuatu') ,('VE','Venezuela, Bolivarian Republic of') ,('VN','Viet Nam') ,('VG','Virgin Islands, British') ,('VI','Virgin Islands, U.S.') ,('WF','Wallis and Futuna') ,('EH','Western Sahara') ,('YE','Yemen') ,('ZM','Zambia') ,('ZW','Zimbabwe');"""
            cursor.execute(query)
            connection.commit();
            query = """CREATE TABLE IF NOT EXISTS USER_COMMUNICATION (user_loginname VARCHAR(60) REFERENCES USER_LOGIN(user_loginname) UNIQUE NOT NULL, user_nationality VARCHAR(60) NOT NULL , user_living_country VARCHAR(60) REFERENCES COUNTRY(country_code) NOT NULL, user_living_city VARCHAR(60) NOT NULL, user_telephonenumber VARCHAR(60) NOT NULL, user_birthday VARCHAR(60) NOT NULL)"""
            cursor.execute(query)
            connection.commit();
            query = """CREATE TABLE IF NOT EXISTS USER_HOBBIES (user_loginname VARCHAR(60) REFERENCES USER_LOGIN(user_loginname) NOT NULL, user_hobby VARCHAR(60) REFERENCES HOBBIES(hobby_name) NOT NULL, PRIMARY KEY(user_loginname,user_hobby) )"""
            cursor.execute(query)
            connection.commit();

    #Save user to user_login table
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


    #Show user from database user_login
    def users_page_db(config):
        with dbapi2.connect(config) as connection:
            if request.method == 'GET':
                cursor = connection.cursor()
                query = "SELECT user_loginname,user_name,user_surname,user_email,user_gender from user_login"
                cursor.execute(query)
                return render_template('profiles.html', users=cursor)

    #Delete user from user_login also delete reference values on other tables
    def users_page_db_delete(config, deleteuserlogin):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM user_hobbies where user_loginname = %s"
            cursor.execute(query, (deleteuserlogin,))
            query = "DELETE FROM user_communication where user_loginname = %s"
            cursor.execute(query, (deleteuserlogin,))
            query = "DELETE FROM user_login where user_loginname = %s"
            cursor.execute(query, (deleteuserlogin,))
            connection.commit()
            return redirect(url_for('profiles'))

    #Update user name open profile edit page
    def users_page_db_update(config, updateuserlogin):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """SELECT user_loginname from user_login where user_loginname = '%s'""" % (updateuserlogin)
            cursor.execute(query)
            connection.commit()
            return render_template('profiles_edit.html', logins=cursor)

    #Update user name and all related reference tables
    def users_page_db_update_apply(config, updateuserlogin):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            new_name = request.form['name']
            query = """ALTER TABLE user_communication DROP CONSTRAINT user_communication_user_loginname_fkey"""
            cursor.execute(query)
            connection.commit()
            query = """ALTER TABLE user_hobbies DROP CONSTRAINT user_hobbies_user_loginname_fkey"""
            cursor.execute(query)
            connection.commit()
            query = """UPDATE user_hobbies set user_loginname ='%s' where user_loginname = '%s'""" % (new_name, updateuserlogin)
            cursor.execute(query)
            connection.commit()
            query = """UPDATE user_communication set user_loginname ='%s' where user_loginname = '%s'""" % (new_name, updateuserlogin)
            cursor.execute(query)
            connection.commit()
            query = """UPDATE user_login set user_loginname ='%s' where user_loginname = '%s'""" % (new_name, updateuserlogin)
            cursor.execute(query)
            connection.commit()
            query = """ALTER TABLE user_hobbies ADD CONSTRAINT user_hobbies_user_loginname_fkey FOREIGN KEY(user_loginname) REFERENCES user_login(user_loginname);"""
            cursor.execute(query)
            connection.commit()
            query = """ALTER TABLE user_communication ADD CONSTRAINT user_communication_user_loginname_fkey FOREIGN KEY(user_loginname) REFERENCES user_login(user_loginname);"""
            cursor.execute(query)
            connection.commit()
            return redirect(url_for('profiles'))



