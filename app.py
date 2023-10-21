from flask import Flask
from flask_restx import Api


from config import Config
from setup_db import db
from views.question import questions_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    app.app_context().push()
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(questions_ns)


if __name__ == '__main__':
    app = create_app(Config())
    db.create_all()
    app.run(host='0.0.0.0', port=5000)
