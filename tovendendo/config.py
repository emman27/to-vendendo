import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    WTF_CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY', 'MINHA-AVO')
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'postgres://postgres@127.0.0.1/tovendendo')
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'data/')


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'postgres://postgres@127.0.0.1/tovendendo_dev')


class TestConfig(DevelopmentConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres@127.0.0.1/tovendendo_test'
    CSRF_ENABLED = False
    WTF_CSRF_ENABLED = False
