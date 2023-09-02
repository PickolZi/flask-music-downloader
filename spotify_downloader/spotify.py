import os, json
from celery import shared_task
from spotdl import Spotdl


with open("SECRETS.json", "r") as file:
    SECRETS = json.load(file)

CLIENT_ID = SECRETS.get('SPOTIFY_KEY')
CLIENT_SECRET = SECRETS.get('SPOTIFY_SECRET')

player = Spotdl(CLIENT_ID, CLIENT_SECRET)


@shared_task(bind=True)
def download_song_by_url(self, url):
    """
    Celery function that downloads the song through a task queue using the spotdl module
    """
    song = player.search([url])
    song_name = f"{song[0].artist} - {song[0].name}"
    print(f"song: {song_name}")
    song, path = player.download(song[0])

    return song_name        

def download_playlist_by_url(url):
    songs = player.search([SPOT_PLAYLIST])
    player.download_songs(songs)
