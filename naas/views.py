from flask import request, session, g, redirect, url_for, \
     abort, render_template, flash, jsonify

from datetime import datetime

from flask.ext.sqlalchemy import SQLAlchemy
#imports the modules for database, SQLAlchemy contains columns which are defined in the developer class
from naas import app

from naas import models
from naas.models import db, Developer

db.create_all()

@app.route('/')
def index():
    return "hello world"

@app.route('/RegisterDev',methods=['GET','POST'])
def developer():
    if not session.get('logged_in'):
        dev = Developer(username=username,email=email)
        db.session.add(dev)
        db.session.commit()
        return redirect(url_for('index'))
    return redirect(url_for('index'))
