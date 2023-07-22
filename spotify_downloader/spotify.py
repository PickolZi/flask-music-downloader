import os
from celery import shared_task
from spotdl import Spotdl

SPOT_URL = "https://open.spotify.com/track/4IOxk5ep5ONrdlL0ZIy64v?si=5ec15380afb543c9"
SPOT_PLAYLIST = "https://open.spotify.com/playlist/3qfCNtFo7EQTBDXzCqExS1"

CLIENT_ID = os.environ.get("SPOTIFY_KEY")
CLIENT_SECRET = os.environ.get("SPOTIFY_SECRET")
player = Spotdl(CLIENT_ID, CLIENT_SECRET)

@shared_task(bind=True)
def download_song_by_url(self, url):
    print(f"Downloading {url}")
    song = player.search([url])
    player.download(song[0])

    return "Download Successful from Celery."

def download_playlist_by_url(url):
    songs = player.search([SPOT_PLAYLIST])
    player.download_songs(songs)

# download_song_by_url(player, SPOT_URL)
# download_playlist_by_url(player, SPOT_PLAYLIST)


