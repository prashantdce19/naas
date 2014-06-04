from flask import request, session, g, redirect, url_for, \
     abort, render_template, flash, jsonify

from naas import app

@app.route('/')
def index():
    return 'Hello, World!'
