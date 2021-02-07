'''
Created on 25-Jan-2021

@author: vyada
'''
import os

basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    '''
    classdocs
    '''
    SECRET_KEY = 'abcdef'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE=3
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
        