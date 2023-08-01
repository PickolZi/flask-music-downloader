import os

from flask import Flask, render_template, request, Blueprint, send_from_directory, current_app, send_file
from spotify_downloader.forms import SpotifySongDownloadForm
from spotify_downloader import spotify
from spotify_downloader.spotify_api import sp


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

@main.route("/user/<string:user_id>")
def user(user_id):
    user = sp.user(user_id)
    playlists = sp.user_playlists(user_id)['items']

    return render_template("user.html", title="Users", user=user, playlists=playlists)

@main.route("/user/<string:user_id>/playlist/<string:playlist_id>")
def user_playlist(user_id, playlist_id):
    user = sp.user(user_id)
    playlist = sp.user_playlist(user=user_id, playlist_id=playlist_id)

    return render_template("user_playlist.html", user=user, playlist=playlist)

@main.route("/download/<string:song_id>", methods=["GET"])
def download_song(song_id): 
    SPOT_URL = "https://open.spotify.com/track/" + song_id
    result = spotify.download_song_by_url.delay(SPOT_URL)

    return send_from_directory(directory=current_app.config["SONG_LOCATION"], path=f"{result.get()}.mp3", as_attachment=True)