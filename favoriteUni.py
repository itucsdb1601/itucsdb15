import json
import os
import psycopg2 as dbapi2
import re
from flask import Flask, request, render_template, redirect
from flask.helpers import url_for

app = Flask(__name__)

class favoriteUnis:

    def savefavoriteUni(config):
        uni_name = None
        fav_department = None
        user_logname = None
        if request.method == 'POST':
            uni_name = request.form['uni_text']
            print(uni_name)
            user_logname = request.form['floginname_text']
            print(user_logname)
            fav_department = request.form['department_text']
            print(fav_department)
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    query = """INSERT INTO favoriteunis(uni_name, fav_department, user_logname) VALUES (%s, %s, %s)"""
                    cursor.execute(query, (uni_name, fav_department, user_logname))
                    connection.commit();
                    return 'Your favorite university has been successfully posted <a href="http://localhost:5000">Home</a>'
                except:
                    return 'Your favorite university cannot be added due to foreign key constraints! <a href="http://localhost:5000">Home</a>'


    def favoriteUnis_db(config):
        with dbapi2.connect(config) as connection:
            if request.method == 'GET':
                cursor = connection.cursor()
                query = """SELECT DISTINCT favoriteunis.user_logname, favoriteunis.uni_name, fav_department from FAVORITEUNIS, UNIVERSITYLIST where favoriteunis.uni_name=universitylist.uni_name"""
                cursor.execute(query)
                connection.commit();
                return render_template('favoriteUnis.html', favoriteUni_list=cursor)


    def favoriteUnis_db_delete(config, deletefavoriteUni):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM FAVORITEUNIS where user_logname = %s"
            cursor.execute(query, (deletefavoriteUni,))
            connection.commit();
            return redirect(url_for('favoriteUnis'))

    def favoriteUnis_db_update(config, updatefavoriteUni):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """SELECT fav_department from FAVORITEUNIS where user_logname = '%s'""" % (updatefavoriteUni)
            cursor.execute(query)
            connection.commit();
            return render_template('favoriteUnis_update.html', favoriteUni_updates=cursor)


    def favoriteUnis_db_update_apply(config, updatefavoriteUni):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            try:
                fav_department = request.form['favorites_text']
                query = """UPDATE FAVORITEUNIS set fav_department ='%s' where user_logname = '%s'""" % (fav_department, updatefavoriteUni)
                cursor.execute(query)
                connection.commit();
                return redirect(url_for('favoriteUnis'))
            except:
                return 'Value cannot be NULL! <a href="http://localhost:5000">Home</a>'






