"""Flask App configuration."""
#SQLALCHEMY_DATABASE_URI = 'sqlite:///./questions.db'


class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5432/postgres"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER_URL = '/'
