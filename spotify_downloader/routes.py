from flask import Flask, render_template, request, Blueprint, send_from_directory, current_app, send_file
from spotify_downloader.forms import SpotifySongDownloadForm
from spotify_downloader import spotify

import os

main = Blueprint('main', __name__)


@main.route("/", methods=['GET', 'POST'])
def home():
    form = SpotifySongDownloadForm()
    if request.method == "POST" and form.validate_on_submit():
        print('Validated form...')
        print('Downloading...')
        result = spotify.download_song_by_url.delay(form.url.data)

        print(f"Finished Downloading... {result.get()}")
        return send_from_directory(directory=current_app.config["SONG_LOCATION"], path=f"{result.get()}.mp3", as_attachment=True)


    return render_template("index.html", text="Home Page!", form=form)


@main.route("/download/<string:url>")
def download_song(url):
    # TODO: Calls download API 
    spotify.download_song_by_url.delay(url)

    return "Download successful!"