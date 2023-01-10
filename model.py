from flask import Flask 

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.debug = True
app.secret_key="super secret key"


# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# Creating an SQLAlchemy instance
db = SQLAlchemy(app)
#Base = descriptive_base()


# Models


class user(db.Model):
    user_id = db.Column(db.Integer, primary_key=True,
                        autoincrement=True, nullable=True)
    user_name = db.Column(db.String(150), nullable=False, unique=True)
    user_firstnm = db.Column(db.String(150), nullable=True)
    user_lastnm = db.Column(db.String(150), nullable=True)
    user_email = db.Column(db.String(150), unique=True, nullable=True)
    user_password = db.Column(db.String(150), nullable=False)
    user_address = db.Column(db.String(200), nullable=True)
    user_phone= db.Column(db.String(150), nullable=True)

class lists(db.Model):
    list_id = db.Column(db.Integer, primary_key=True,
                        autoincrement=True, nullable=False)
    list_name = db.Column(db.String(150), nullable=False, unique=True)
    list_description = db.Column(db.String(150), nullable=False)
    list_userid = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    list_cmpflag=db.Column(db.Integer,nullable=False)

class cards(db.Model):
    cards_id = db.Column(db.Integer, primary_key=True,
                        autoincrement=True, nullable=False)
    cards_name = db.Column(db.String(150), nullable=False, unique=True)
    cards_description = db.Column(db.String(300), nullable=False)
    cards_cmpflag=db.Column(db.Integer,nullable=False)
    cards_deadline=db.Column(db.DateTime,nullable=False)
    cards_listid=db.Column(db.Integer,db.ForeignKey('lists.list_id'),nullable=False)
