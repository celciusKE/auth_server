from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.UUid, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(20), unique=True)
    contact = db.Column(db.Integer(20), unique=True)
    password = db.Column(db.String(80))


def __repr__(self):
    return f"User('{self.username}','{self.email}','{self.password}')"
