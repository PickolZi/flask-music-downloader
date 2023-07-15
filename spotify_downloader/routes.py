from flask import Flask, render_template, request
from spotify_downloader import app
from spotify_downloader.forms import SpotifySongDownloadForm
from spotify_downloader import spotify

@app.route("/", methods=['GET', 'POST'])
def home():
    form = SpotifySongDownloadForm()
    if request.method == "POST" and form.validate_on_submit():
        # spotify.download_song_by_url(spotify.player, "https://open.spotify.com/track/4IOxk5ep5ONrdlL0ZIy64v?si=5ec15380afb543c9")
        return f"Form was submitted successfully! {form.url.data} is now downloading to server."

    return render_template("index.html", text="Home Page!", form=form)