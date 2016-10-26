from flask import Flask, render_template

from datetime import datetime


app = Flask(__name__)


@app.route('/')
def home_page():
    now = datetime.now()
    day = now.strftime('%A')
    return render_template('home.html', day_name=day)


@app.route('/profiles')
def profiles():
    return render_template('profiles.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/favorites')
def favorites():
    return render_template('favorites.html')

@app.route('/followers')
def followers():
    return render_template('followers.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
