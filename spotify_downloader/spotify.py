import os
from celery import shared_task
from spotdl import Spotdl

CLIENT_ID = os.environ.get("SPOTIFY_KEY")
CLIENT_SECRET = os.environ.get("SPOTIFY_SECRET")

player = Spotdl(CLIENT_ID, CLIENT_SECRET)

@shared_task(bind=True)
def download_song_by_url(self, url):
    song = player.search([url])
    song_name = f"{song[0].artist} - {song[0].name}"
    print(f"song: {song_name}")
    song, path = player.download(song[0])

    return song_name

def download_playlist_by_url(url):
    songs = player.search([SPOT_PLAYLIST])
    player.download_songs(songs)

# download_song_by_url(player, SPOT_URL)
# download_playlist_by_url(player, SPOT_PLAYLIST)

if __name__ == "__main__":
    results = download_song_by_url("Typa Girl")