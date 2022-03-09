from flask import Flask, render_template, session, abort, url_for, redirect
from authlib.integrations.flask_client import OAuth
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from flask_migrate import Migrate



app = Flask(__name__)
oauth = OAuth(app)
app.secret_key='password'
gooogle=oauth.register(
    name='google',
    client_id=os.getenv("600098052876-l430cauc1sh7q8dulimt5f3o84jivuvl.apps.googleusercontent.com"),
    client_secret=os.getenv("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"),
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',
    # This is only needed if using openId to fetch user info
    client_kwargs={'scope': 'openid email profile'},
)
app.config['SECRET KEY'] = 'root'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://auth_dba:titan12@localhost/auth_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}','{self.content}')"

@app.route('/submit')
def index():
    return render_template('login.html')

@app.route('/login')
def login():
    google = oauth.create_client('google')
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)

@app.route('/authorize')
def authorize():
    google = oauth.create_client('google')
    token = google.authorize_access_token()
    resp = google.get('userinfo')
    user_info = resp.json()
    user = oauth.google.userinfo()
    session['profile'] = user_info
    session.permanent = True
    return redirect('/')
if __name__ == '__main__':
    app.debug = True
    app.run()
