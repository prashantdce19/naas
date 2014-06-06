from flask import Flask, request, flash, url_for, redirect
from flask.ext.sqlalchemy import SQLAlchemy

from naas import db

from datetime import datetime


class Developer(db.Model):
    id = db.Column(db.Integer , primary_key = True)  #defines the id
    email = db.Column(db.String(90), unique = True)  #defines the Developer's email ID
    username = db.Column(db.String(120), unique = True) #defines the username of Developer
   
   # created_on = db.Column(db.DateTime)

    def __init__(self, email, username):
        self.email = email
        self.username = username
       
       # self.creation = datetime.now()

    def __repr__(self):
        return "<User %r>" % self.username

