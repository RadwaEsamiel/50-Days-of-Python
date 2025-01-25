from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


with open('YouTube Music.htm', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

recap_section = soup.find(string="2024 Recap")
songs = []

if recap_section:
    start_after_recap = recap_section.find_parent()
    song_titles = start_after_recap.find_all_next('yt-formatted-string', class_='title')

    for title in song_titles:
        song_name = title.get_text(strip=True)
        if song_name:
            songs.append(song_name)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:8888/callback",
        client_id="7190c0475ce24e798c201939ac373934",
        client_secret="8108ef28434e4c288edd3706b6d5cd14",
        show_dialog=True,
        cache_path="token.txt",
        username="Radwa Esmaiel",
    )
)
user_id = sp.current_user()["id"]

song_uris = []

for song in songs:
    try:
        result = sp.search(q=f"track:{song}", type="track", limit=1)

        if result["tracks"]["items"]:
            song_uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(song_uri)
        else:
            print(f"Song '{song}' not found on Spotify.")

    except Exception as e:
        print(f"Error processing song '{song}': {e}")

print(song_uris)

playlist = sp.user_playlist_create(user_id, name=f"YouTube Music Recap", public=False,
                                   description="Top 100 played Songs")

playlist_id = playlist["id"]
sp.playlist_add_items(playlist_id, song_uris)
print(f"Playlist YouTube Music Recap created and songs added successfully!")