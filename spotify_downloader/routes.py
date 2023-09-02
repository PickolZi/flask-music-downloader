import os
import zipfile

from flask import Flask, render_template, request, Blueprint, send_from_directory, current_app, request, redirect, url_for, flash, abort
from spotify_downloader.forms import SpotifySongDownloadForm, SpotifyGetUser
from spotify_downloader import spotify
from spotify_downloader.spotify_api import sp, return_spotify_user, return_spotify_user_playlist
from wtforms import BooleanField

from spotipy.exceptions import SpotifyException


main = Blueprint('main', __name__)


@main.route("/", methods=['GET', 'POST'])
def home():
    """
    If the user inputs a valid Spotify user's id into the input field. Redirect them to main.user page to display their playlists.
    """
    form = SpotifySongDownloadForm()

    if form.validate_on_submit and request.method == "POST":
        if return_spotify_user(form.input.data):
            return redirect(url_for('main.user', user_id=form.input.data))
        else:
            flash("User does not exist")
        
    return render_template("home.html", title="Home", form=form)

@main.route("/user/<string:user_id>", methods=["POST", "GET"])
def user(user_id):
    """
    Is redirected from the home page or same page to load the user's information as well as all their public Spotify playlists.
    """

    if not return_spotify_user(user_id):
        abort(404)
        
    # Calls spotify api to lookup user and their playlists.
    user = sp.user(user_id)
    playlists = sp.user_playlists(user_id)['items']

    # The following is when the user is already on the user page, but is trying to lookup another user.
    form = SpotifyGetUser()
    if form.validate_on_submit():
        if return_spotify_user(user_id=form.user.data):
            return redirect(url_for('main.user', user_id=form.user.data))
        else:
            flash("User not found")
        
    return render_template("user.html", form=form, title="Users", user=user, playlists=playlists, page="user")

@main.route("/user/<string:user_id>/playlist/<string:playlist_id>", methods=["POST", "GET"])
def user_playlist(user_id, playlist_id):
    """
    Redirected from the main.user page. Displays all the songs and their info for the selected playlist. Allows the user to download each or every song 
    and returns a zip of the downloaded songs.
    """
    if not return_spotify_user(user_id):
        abort(404)
    if not return_spotify_user_playlist(user_id, playlist_id):
        abort(404)

    # Calls spotify's api to get the user and the playlist's information.
    user = sp.user(user_id)
    playlist = sp.user_playlist(user=user_id, playlist_id=playlist_id)
    playlists = sp.user_playlists(user_id)['items']

    # The following is when the user is already on the playlist page, but is trying to lookup another user.
    form = SpotifyGetUser()
    if form.validate_on_submit():
        if return_spotify_user(user_id=form.user.data):
            return redirect(url_for('main.user', user_id=form.user.data))
        else:
            flash("User not found")
               

    # Depending on the checkboxes selected, will grab the song's ids to download, zip, clean, and return the zipped up music.
    song_ids = request.form.getlist('song_choice')
    if song_ids != []:
        # Clears songs from directory before downloading multiple songs.
        # Bug: When downloading individual songs by calling the main.download endpoint, it does not remove pre-downloaded songs, because this route calls
        #      the same endpoint and we need the songs to exist until it is time to zip. Therefore, we need to clear the songs beforehand. 
        clear_songs_from_directory()

        # Downloads each song
        for song_id in song_ids:
            download_song(song_id=song_id)  
    
        # Zips all the downloaded mp3s into "music.zip"
        zipfolder = zipfile.ZipFile('music.zip', 'w', compression=zipfile.ZIP_STORED)
        for root, dirs, files in os.walk('.'):
            for file in files:
                if file[-3:] == "mp3":
                    zipfolder.write(file)
            zipfolder.close()

        # Deletes all downloaded mp3s in the directory
        clear_songs_from_directory()
        
        # Returns "music.zip"
        return send_from_directory(directory=current_app.config["SONG_LOCATION"], path="music.zip", as_attachment=True)
   
    return render_template("user_playlist.html", form=form, title="playlist", user=user, playlists=playlists, playlist=playlist, page="playlist")

@main.route("/download/<string:song_id>", methods=["GET"])
def download_song(song_id): 
    """
    Given the song_id, downloads and then returns the song file.
    TODO: Turn into API endpoint that can be called. Read Comment at end of function.
    """
    try:
        SPOT_URL = "https://open.spotify.com/track/" + song_id
        result = spotify.download_song_by_url.delay(SPOT_URL)

        results = result.get()
    except SpotifyException:
        abort(404)

    """
    Had to comment out return function acting as endpoint. Certain songs would not be returned back to the user, my assumption being that the song's title 
    had special characters that made it difficult to return through the below's path name.
    """
    # return send_from_directory(directory=current_app.config["SONG_LOCATION"], path=f"{results}.mp3", as_attachment=True)

def clear_songs_from_directory():
    """
    Deletes all downloaded mp3s in the directory
    """
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file[-3:] == "mp3":
                os.remove(file)