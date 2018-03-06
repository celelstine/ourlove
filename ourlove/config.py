import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv('SECRET_KEY', "--00jkbsjbsjbskb92902292bjbsjbsk|||kjs")
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://cele:smilesh2o@localhost:5432/ourlove')

class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True