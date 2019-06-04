import os
from flask import Flask, session, redirect, url_for, escape, request, flash
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from flask import render_template
import planisphere


app = Flask(__name__)
app.secret_key = os.environ.get('MY_LPTHW_SECRETKEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
