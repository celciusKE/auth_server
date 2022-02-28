from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__)  # make an instance of the app
app.config['SECRET_KEY'] = 'secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:titan12@localhost/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(80), nullable=False)


def __init__(self, uname,Email,Password):
    self.uname = username
    self.Email = email
    self.Password = password


@app.route('/login', method=['GET', 'POST'])  # define the route and what happens in the route
def login():
    form = login()
    return render_template('login.html', form=form)


@app.route('/home', method=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/register')
def register():
    form = register()
    return render_template('register.html', form=form)


@app.route('/submit', methods=['post'])
def submit():
    global username, password, email
    if request.method == 'post':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        # print(username,password,email)

    if username == '' or password == '' or email == '':
        return render_template('home.html', message='Please enter required field')
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
