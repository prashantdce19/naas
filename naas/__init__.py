# Third party lib imports

from flask import Flask

from sqlalchemy.engine.url import URL

from flask.ext.sqlalchemy import SQLAlchemy

# Local imports
from naas import settings

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = URL(**settings.DATABASE)

db = SQLAlchemy(app)

import naas.views
