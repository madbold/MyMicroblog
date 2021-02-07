'''
Created on 25-Jan-2021

@author: vyada
'''

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from elasticsearch import Elasticsearch


db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = 'Please log in to access this page.'

bootstrap = Bootstrap()
moment = Moment()



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']]) \
        if app.config['ELASTICSEARCH_URL'] else None

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    from app.auth import  bp as bp_auth
    from app.error import bp as bp_error
    from app.main import bp as bp_main
    app.register_blueprint(bp_error)
    app.register_blueprint(bp_auth, url_prefix='/auth')
    app.register_blueprint(bp_main)
    return app

from app import  models