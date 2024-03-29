import os

version = "1.1.0"
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = True
    TESTING = True
    #SQLALCHEMY_TRACK_MODIFICATIONS = False
    #SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:////{}/data.db'.format(basedir))

class Production(Config):
    DEBUG = False

class Development(Config):
    DEBUG = True

class Testing(Config):
    TESTING = True