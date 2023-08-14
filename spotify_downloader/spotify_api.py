import os
import json

from spotipy import Spotify
from spotipy.exceptions import SpotifyException
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = os.environ.get("SPOTIFY_KEY")
CLIENT_SECRET = os.environ.get("SPOTIFY_SECRET")


sp = Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))


# Prints dictionary in neat JSON format.
def pretty_print(my_dict):
    print(json.dumps(my_dict, indent=2))


def return_spotify_user(user_id):
    """ 
        Gets user information using the user's id.

        user_id: Spotify's user id from their website.

        Returns: JSON or None
    """
    try:
        user = sp.user(user_id)
    except SpotifyException:
        return None
    
    return user

if __name__ == "__main__":
    USER_ID = "lclq7kwxx6gwfnk21rp67y0ml"
    user = sp.user(USER_ID)  # Gets the User's information
    user_playlists = sp.user_playlists(USER_ID)  # Gets all of the User's playlist and it's info
    # user_playlist = sp.user_playlist("pickolzhd", playlist_id="3ajkaWGkyGU9HKFozBV1il")  # Gets the user playlist given name and playlist id.

    pretty_print(user_playlists)

