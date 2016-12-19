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

