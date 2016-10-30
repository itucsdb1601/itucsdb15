import json
import os
import psycopg2 as dbapi2
import re
from flask import Flask


app = Flask(__name__)


def initialize_database(config):
    with dbapi2.connect(config) as connection:
        cursor = connection.cursor()

        query = """CREATE TABLE IF NOT EXISTS USER_LOGIN (user_id serial primary key,user_name VARCHAR (60) UNIQUE NOT NULL,user_password VARCHAR(20))"""
        cursor.execute(query)

        try:
            query = """insert into USER_LOGIN(user_name,user_password) values('saracso','1234567890')"""
            cursor.execute(query)
        except:
            print("Oops!  That user name exists.  Try again...")
        connection.commit();
        return 'Value is inserted'


