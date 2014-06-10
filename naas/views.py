from flask import request, session, g, redirect, url_for, \
     abort, render_template, flash, jsonify
import requests

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

@app.route('/developer/<uid>',methods=['GET','POST'])
def developer(uid):
    # incoming request
    if request.method == 'POST':
        username = request.values['username']
        email = request.values['email']
        dev = Developer(username,email)
        db.session.add(dev)
        db.session.commit()

        json_data = {'id': dev.id, 'username': dev.username,\
                'email': dev.email, 'accurl':str(request.url)+\
                '/'+str(dev.id)}
        return jsonify(json_data)
    
    if request.method == 'GET':
        user = Developer.query.get(uid)
        u_data = {'id': user.id, 'username': user.username,\
                'email': user.email, 'accurl':request.url}
 
        return jsonify(u_data)
        
