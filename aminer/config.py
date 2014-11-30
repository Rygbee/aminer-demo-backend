# -*- coding: utf-8 -*-

import os

import redis


class BaseConfig(object):

    PROJECT = "aminer-sample"

    # Get app root path, also can use flask.root_path.
    # ../../config.py
    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    DEBUG = False
    TESTING = False

    ADMINS = ['stack@live.cn']

    # http://flask.pocoo.org/docs/quickstart/#sessions
    SECRET_KEY = 'Some ScKey'


    #Paths in FLask should be configured
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
    APP_STATIC = os.path.join(APP_ROOT, 'static')


    MONGO_ADDRESS = "argcv.com"
    MONGO_PORT = 37017
    MONGO_USER = "keg"
    MONGO_PASS = "tipsikeg2012"


class DefaultConfig(BaseConfig):

    DEBUG = True

    # Flask-babel: http://pythonhosted.org/Flask-Babel/
    ACCEPT_LANGUAGES = ['zh']
    BABEL_DEFAULT_LOCALE = 'en'

    # Flask-cache: http://pythonhosted.org/Flask-Cache/
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 60
