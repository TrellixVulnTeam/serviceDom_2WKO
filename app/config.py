import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_TRACK_MODIFICATIONS = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'DBDOM.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
