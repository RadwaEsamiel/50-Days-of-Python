import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=["playlist-modify-public", "playlist-modify-private"],
        redirect_uri="http://localhost:8888/callback",
        client_id="7190c0475ce24e798c201939ac373934",
        client_secret="8108ef28434e4c288edd3706b6d5cd14",
        show_dialog=True,
        cache_path="token.txt",
        username="Radwa Esmaiel",
    )
)
user_id = sp.current_user()["id"]



playlist_id = "5WzPUIFchpYYG8zKej6lny"

results = sp.playlist_tracks(playlist_id)
track_ids = [track['track']['id'] for track in results['items']]

# Shuffle the track IDs
random.shuffle(track_ids)


# Create a new playlist
new_playlist = sp.user_playlist_create(user_id, "Shuffled Playlist", public=True)

# Add shuffled tracks to the new playlist
sp.playlist_add_items(new_playlist['id'], track_ids)

print("Shuffled playlist created successfully!")