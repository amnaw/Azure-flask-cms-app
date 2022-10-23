"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session
from logging.config import dictConfig
from flask.logging import default_handler

app = Flask(__name__)
app.config.from_object(Config)

# Add any logging levels and handlers with app.logger
# logging.basicConfig(
#    level=logging.WARNING,
#    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFOs',
        'handlers': ['wsgi']
    }
})

app.logger.removeHandler(default_handler)

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views
