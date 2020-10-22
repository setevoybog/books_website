from flask import Flask
from books_website.config import Config


def create_app(config_class=Config):
    app = Flask(__name__)

    from books_website.main.routes import main
    app.register_blueprint(main)

    return app
