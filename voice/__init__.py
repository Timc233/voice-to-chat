from flask import Flask
from voice.config import Config
from voice.router import voice


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(voice)

    return app
