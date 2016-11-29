import json
import os
import psycopg2 as dbapi2
import re
from flask import Flask, request, render_template, redirect
from flask.helpers import url_for

## CEYDA ALADAÐ - 150130283
class Hobby:

    #Show user's hobby information make join with Hobbies table to get hobby type
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

    #Update user's hobby information if exists
    #If it doesn't exist create and add as new row
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
                    return "There is no user with that name <a href='http://localhost:5000/profiles'>Profiles</a>"
                else:
                    return redirect(url_for('hobbies_edit'))

    #Delete user's hobby information from user_hobbies
    def users_page_db_hobby_information_delete(config):
        username = request.form['user_name_del']
        hobby_name = request.form['hobby_sel']
        with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                query="DELETE FROM user_hobbies where user_loginname = %s AND user_hobby=%s"
                cursor.execute(query, (username,hobby_name))
                connection.commit();
                if cursor.rowcount == 0:
                    return "There is no user and hobby with that user hobby pair <a href='http://localhost:5000/profiles'>Profiles</a>"
                else:
                    return redirect(url_for('hobbies_edit'))




