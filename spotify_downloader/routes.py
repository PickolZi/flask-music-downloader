import os
import zipfile

from flask import Flask, render_template, request, Blueprint, send_from_directory, current_app, request, redirect, url_for
from spotify_downloader.forms import SpotifySongDownloadForm, SpotifyGetUser
from spotify_downloader import spotify
from spotify_downloader.spotify_api import sp
from wtforms import BooleanField


main = Blueprint('main', __name__)


@main.route("/", methods=['GET', 'POST'])
def home():
    form = SpotifySongDownloadForm()

    if form.validate_on_submit and request.method == "POST":
        return redirect(url_for('main.user', user_id=form.input.data))

    return render_template("home.html", title="Home", form=form)

@main.route("/user/<string:user_id>", methods=["POST", "GET"])
def user(user_id):
    user = sp.user(user_id)
    playlists = sp.user_playlists(user_id)['items']

    form = SpotifyGetUser()
    if form.validate_on_submit():
        return redirect(url_for('main.user', user_id=form.user.data))

    return render_template("user.html", form=form, title="Users", user=user, playlists=playlists, page="user")

@main.route("/user/<string:user_id>/playlist/<string:playlist_id>", methods=["POST", "GET"])
def user_playlist(user_id, playlist_id):
    user = sp.user(user_id)
    playlists = sp.user_playlists(user_id)['items']
    playlist = sp.user_playlist(user=user_id, playlist_id=playlist_id)

    form = SpotifyGetUser()
    if form.validate_on_submit():
        return redirect(url_for('main.user', user_id=form.user.data))
               
    song_ids = request.form.getlist('song_choice')
    if song_ids != []:
        print(f"song_ids: {song_ids}")
        for song_id in song_ids:
            download_song(song_id=song_id)  # Downloads song
    
        # Zips and returns all the songs
        zipfolder = zipfile.ZipFile('music.zip', 'w', compression=zipfile.ZIP_STORED)
        for root, dirs, files in os.walk('.'):
            for file in files:
                if file[-3:] == "mp3":
                    zipfolder.write(file)
            zipfolder.close()

        # Deletes all mp3s in file
        for root, dirs, files in os.walk('.'):
            for file in files:
                if file[-3:] == "mp3":
                    os.remove(file)
        
        return send_from_directory(directory=current_app.config["SONG_LOCATION"], path="music.zip", as_attachment=True)
   
    return render_template("user_playlist.html", form=form, title="playlist", user=user, playlists=playlists, playlist=playlist, page="playlist")

@main.route("/dir")
def get_files():
    return "hello world"

@main.route("/download/<string:song_id>", methods=["GET"])
def download_song(song_id): 
    SPOT_URL = "https://open.spotify.com/track/" + song_id
    result = spotify.download_song_by_url.delay(SPOT_URL)

    return send_from_directory(directory=current_app.config["SONG_LOCATION"], path=f"{result.get()}.mp3", as_attachment=True)