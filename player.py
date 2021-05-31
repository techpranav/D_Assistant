import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
from time import sleep
import spotipy.util as util

username = input("Type the Spotify user ID to use: ")
token = util.prompt_for_user_token(username, show_dialog=True)
sp = spotipy.Spotify(token)
pprint(sp.me())

scope = "user-read-playback-state,user-modify-playback-state"
sp = spotipy.SpotifyOAuth( (client_credentials_manager=SpotifyOAuth(scope=scope))

# Shows playing devices
res = sp.devices()
pprint(res)

# Change track
sp.start_playback(uris=['spotify:track:6gdLoMygLsgktydTQ71b15'])

# Change volume
sp.volume(100)
sleep(2)
sp.volume(50)
sleep(2)
sp.volume(100)