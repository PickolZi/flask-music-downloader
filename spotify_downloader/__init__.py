from flask import Flask, render_template
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SPOTIFY_FLASK_SECRET_KEY")

from spotify_downloader import routes