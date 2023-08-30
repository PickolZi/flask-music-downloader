import os
import json

from spotipy import Spotify
from spotipy.exceptions import SpotifyException
from spotipy.oauth2 import SpotifyClientCredentials

with open("SECRETS.json", "r") as file:
    SECRETS = json.load(file)

CLIENT_ID = SECRETS.get('SPOTIFY_KEY')
CLIENT_SECRET = SECRETS.get('SPOTIFY_SECRET')

sp = Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))


def return_spotify_user(user_id):
    """ 
        Gets user information using the user's id.

        user_id: Spotify's user id from Spotify's website.

        Returns: JSON or None
    """
    try:
        user = sp.user(user_id)
    except SpotifyException:
        return None
    
    return user

def return_spotify_user_playlist(user_id, user_playlist):
    """ 
        Gets user's playlist information using the user's id and playlist id

        user_id: Spotify's user id from Spotify's website.
        user_playlist: Spotify's user's playlist id from Spotify's website.

        Returns: JSON or None
    """
    try:
        playlist = sp.user_playlist(user=user_id, playlist_id=user_playlist)
    except SpotifyException:
        return None
        
    return playlist 