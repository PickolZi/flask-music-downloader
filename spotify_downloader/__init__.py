from flask import Flask, render_template
from .utils import make_celery
from .routes import main
import os


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.environ.get("SPOTIFY_FLASK_SECRET_KEY")
    app.config["CELERY_CONFIG"] = {"broker_url": "redis://localhost:6379/0", "result_backend": "redis://localhost:6379/0"}

    celery = make_celery(app)
    celery.set_default()

    app.register_blueprint(main)

    return app, celery


from spotify_downloader import routes 