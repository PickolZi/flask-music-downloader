from flask import Flask, render_template
from .utils import make_celery
from .routes import main
import os, json


def create_app():
    app = Flask(__name__)

    with open("SECRETS.json", "r") as file:
        SECRETS = json.load(file)

    app.config["SECRET_KEY"] = SECRETS.get('SPOTIFY_FLASK_SECRET_KEY')
    app.config["CELERY_CONFIG"] = {"broker_url": "redis://redis:6379/0", "result_backend": "redis://redis:6379/0"}

    cur_path = app.root_path
    parent_path = os.path.abspath(os.path.join(cur_path, '..'))  # Gets Parent directory
    app.config["SONG_LOCATION"] = parent_path

    celery = make_celery(app)
    celery.set_default()

    app.register_blueprint(main)

    return app, celery


from spotify_downloader import routes 