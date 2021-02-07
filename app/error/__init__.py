'''
Created on 06-Feb-2021

@author: vyada
'''
from flask import Blueprint
bp = Blueprint('error', __name__)


from app.error import handlers
