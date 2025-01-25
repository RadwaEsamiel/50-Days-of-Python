from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


date_input = input("which year would you like to travel to? Type the date in this format YYYY-MM-DD : ")

url = f"https://www.billboard.com/charts/hot-100/{date_input}/"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.text, 'html.parser')

songs = soup.select("li ul li h3")

song_titles = []
for song in songs:
    title = song.get_text(strip=True)
    song_titles.append(title)

print(song_titles)




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

for song in song_titles:
    try:
        result = sp.search(q=f"track:{song} year:2020", type="track", limit=1)
        
        if result["tracks"]["items"]:
            song_uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(song_uri)
        else:
            print(f"Song '{song}' not found on Spotify.")
    
    except Exception as e:
        print(f"Error processing song '{song}': {e}")

print(song_uris)

playlist = sp.user_playlist_create(user_id, name=f"{date_input} Billboard 100", public=False, description="Top 100 Billboard songs")

playlist_id = playlist["id"]
sp.playlist_add_items(playlist_id, song_uris)
print(f"Playlist '{date_input} Billboard 100' created and songs added successfully!")

