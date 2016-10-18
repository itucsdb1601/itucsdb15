import datetime
import os

from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def layout_page():
    now = datetime.datetime.now()
    return render_template('layout.html', current_time=now.ctime())
@app.route('/home')
def home_page():
    now = datetime.datetime.now()
    return render_template('home.html', current_time=now.ctime())
@app.route('/profiles')
def open_profiles():
    now = datetime.datetime.now()
    return render_template('profiles.html', current_time=now.ctime())
@app.route('/followersfollowing')
def open_followersFollowing():
    now = datetime.datetime.now()
    return render_template('followersfollowing.html', current_time=now.ctime())
@app.route('/notifications')
def open_notifications():
    now = datetime.datetime.now()
    return render_template('notifications.html', current_time=now.ctime())
@app.route('/settings')
def open_settings():
    now = datetime.datetime.now()
    return render_template('settings.html', current_time=now.ctime())
@app.route('/favorites')
def open_favorites():
    now = datetime.datetime.now()
    return render_template('favorites.html', current_time=now.ctime())


if __name__ == '__main__':
    VCAP_APP_PORT = os.getenv('VCAP_APP_PORT')
    if VCAP_APP_PORT is not None:
        port, debug = int(VCAP_APP_PORT), False
    else:
        port, debug = 5000, True
    app.run(host='0.0.0.0', port=port, debug=debug)
