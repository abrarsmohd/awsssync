import os
from flask import Flask
from flask import render_template,url_for,flash,redirect,request,Blueprint, jsonify, json
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from wtforms import ValidationError, validators
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration


TEMPLATE_DIR = os.path.abspath('templates')
STATIC_DIR = os.path.abspath('static')
print(TEMPLATE_DIR)
print(STATIC_DIR)

app = Flask(__name__)

bootstrap = Bootstrap(app)

sentry_sdk.init(
    dsn="https://5ca65acfe1d9455697a8a28b9ebe2c99@o422148.ingest.sentry.io/5344687",
    integrations=[FlaskIntegration()]
    )

app.config['SECRET_KEY'] = 'mysecret'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///'+ os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db =   SQLAlchemy(app)
Migrate(app,db)


from mysync.users.views import user
app.register_blueprint(user)
