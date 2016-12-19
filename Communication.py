import json
import os
import psycopg2 as dbapi2
import re
from flask import Flask, request, render_template, redirect
from flask.helpers import url_for

app = Flask(__name__)
## CEYDA ALADAÐ - 150130283
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

    #Delete user's communication information from USER_COMMUNICATION
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

    #Show user's communication informations inside html table, join with countries table to geet country code
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




