import os
from pytz import timezone

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = "]7kML!yBh%D]$\g"
    TIMEZONE = timezone('Europe/Paris')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    POSTGRES = {
    'user': 'gloth',
    'pw': 'password',
    'db': 'postgres',
    'host': 'db',
    'port': '5432',
    }

    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

    SQLALCHEMY_BINDS = {
    'user': SQLALCHEMY_DATABASE_URI,
    'roles': SQLALCHEMY_DATABASE_URI,
    'user_roles': SQLALCHEMY_DATABASE_URI,
    'pathology': SQLALCHEMY_DATABASE_URI,
    'specialty': SQLALCHEMY_DATABASE_URI,
    'pathology_specialty': SQLALCHEMY_DATABASE_URI
    }