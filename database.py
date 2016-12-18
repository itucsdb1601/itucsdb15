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
from unisports import unisports as unisports
from academics import academics as academics

app = Flask(__name__)


def initialize_database(config):
    with dbapi2.connect(config) as connection:
        cursor = connection.cursor()
        profile.initialize_profiles(config)
        Interaction_c.initialize_interaction(config)
        university.initialize_universities(config)
        unisports.initialize_unisports(config)
        academics.initialize_academics(config)

        connection.commit();
        return 'tables are created <a href="http://localhost:5000">Home</a>'

