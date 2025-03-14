import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import base64

client_id = "bb9065496490454189a3c979dd17fef8"
client_secret = "7515274a5d6e41be8e1536b0cde823ea"

client_credential_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credential_manager)

# Se busca información sobre Blackpink.
result = sp.search(q='KARINA', type='artist', limit=1)

followers = result['artists']['items'][0]['followers']
karina_id = result['artists']['items'][0]['id']


id_karina = "1QZuAtDYNrk2QMogJulsyq"
id_dalila = "3ruk44IzmsPppwo7VOknwZ"

results_karina = sp.artist_albums(id_karina, album_type="album")
results_dalila = sp.artist_albums(id_dalila, album_type="album")

print("Albunes de Karina:")
for num,item in enumerate(results_karina["items"]):
    print(f"{num}- {item["name"]}")

print("Albunes de Dalila:")
for num,item in enumerate(results_dalila["items"]):
    print(f"{num}- {item["name"]}")