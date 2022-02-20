from flask import Flask,render_template,url_for
from flask_sqlachemy import SQLAlchemy

app=Flask(__name__)  #make an instance of the app

@app.route('/login')         #define the route and what happens in the route
def login():
    return render_template('login.html')

@app.route('/home')         #define the route and what happens in the route
def home():
    return render_template('home.html')

@app.route('/register')         #define the route and what happens in the route
def register():
    return render_template('register.html')


if __name__=='__main__':
    app.run(debug=True)