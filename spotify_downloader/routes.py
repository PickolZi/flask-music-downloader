from flask import Flask, render_template, request, Blueprint
from spotify_downloader.forms import SpotifySongDownloadForm
from spotify_downloader import spotify

main = Blueprint('main', __name__)

@main.route("/", methods=['GET', 'POST'])
def home():
    form = SpotifySongDownloadForm()
    if request.method == "POST" and form.validate_on_submit():
        print('validated form')
        spotify.download_song_by_url.delay(form.url.data)
        print('downloading')
        return f"Form was submitted successfully! {form.url.data} is now downloading to server."

    return render_template("index.html", text="Home Page!", form=form)

@main.route("/download/<string:url>")
def download_song(url):
    spotify.download_song_by_url.delay(url)

    return "Download successful!"