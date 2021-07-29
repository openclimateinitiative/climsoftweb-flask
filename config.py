from collections import OrderedDict
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    #BABEL_DEFAULT_LOCALE = 'fr'
    DEBUG = True
    LANGUAGES = ['en', 'fr']

    if not os.environ.get('SECRET_KEY'):
        raise RuntimeError('SECRET_KEY environment variable must be specified')
    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'db.sqlite3')

    #SQLALCHEMY_DATABASE_URI = 'mysql://root:admin@localhost/mariadb_climsoft_test_db_v4?port=3306'

    SQLALCHEMY_BINDS = OrderedDict([
        ('climsoft4_prod', 'mysql+mysqldb://root:admin@192.168.1.131/mariadb_climsoft_test_db_v4'),
    ])

    DEFAULT_CDMS = list(SQLALCHEMY_BINDS.keys())[0]
