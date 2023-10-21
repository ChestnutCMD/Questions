"""Flask App configuration."""


class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@pg/postgres"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER_URL = '/'
