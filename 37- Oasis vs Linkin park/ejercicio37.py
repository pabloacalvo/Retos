""""
/*
 * EJERCICIO:
 * Oasis y Linkin Park han anunciado nueva gira, pero, ¿quién es más popular?
 * ¡Dos de las bandas más grandes de la historia están de vuelta!
 * Desarrolla un programa que se conecte al API de Spotify y los compare.
 * Requisitos:
 * 1. Crea una cuenta de desarrollo en https://developer.spotify.com.
 * 2. Conéctate al API utilizando tu lenguaje de programación.
 * 3. Recupera datos de los endpoint que tú quieras.
 * Acciones:
 * 1. Accede a las estadísticas de las dos bandas.
 *    Por ejemplo: número total de seguidores, escuchas mensuales,
 *    canción con más reproducciones...
 * 2. Compara los resultados de, por lo menos, 3 endpoint.
 * 3. Muestra todos los resultados por consola para notificar al usuario.
 * 4. Desarrolla un criterio para seleccionar qué banda es más popular.
 */
"""

import requests
import base64

client_id = "bb9065496490454189a3c979dd17fef8"
client_secret = "7515274a5d6e41be8e1536b0cde823ea"


def get_token()->str:
    url = "https://accounts.spotify.com/api/token"
    headers = {
            "Authorization": "Basic " + base64.b64encode(f"{client_id}:{client_secret}".encode()).decode(),
            "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}

    respose = requests.post(url,headers=headers, data=data)
    if respose.status_code != 200:
        raise Exception(f"Error {respose.json()}")
    
    return respose.json()['access_token']

def search_artist(token:str,name:str):
    url = f"https://api.spotify.com/v1/search?q={name}&type=artist&limit=1"
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(
            f"Error obteniendo el artista: {response.json()}"
        )

    results = response.json()
    if results['artists']['items']:
        return results['artists']['items'][0]['id']
    else:
        raise Exception(
            f"No se encontro el artista {name}"
        )
    
def get_followers(token:str, id_artist:str):
    url = f"https://api.spotify.com/v1/artists/{id_artist}"
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url,headers=headers)
    if response.status_code != 200:
        raise Exception(f"Error al obtener los seguidores del artista")
    results = response.json()
    return {
        'Artista': results['name'],
        'Seguidores': results['followers']['total']
        }
    
def get_artists_top_tracks(token:str, id_artist:str):
    url = f"https://api.spotify.com/v1/artists/{id_artist}/top-tracks"
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Error al obtener datos del artista")
    results = response.json()
    top_track = max(results['tracks'], key=lambda track: track['popularity'])
    return {'Cancion':top_track['name'],
            'Popularidad':top_track['popularity']
            }
    



token = get_token()
artists_id_1 = search_artist(token, name="Oasis")
artists_id_2 = search_artist(token, name='Linkin Park')
print(get_followers(token,artists_id_1))
print(get_artists_top_tracks(token, artists_id_1))
print(get_followers(token,artists_id_2))
print(get_artists_top_tracks(token, artists_id_2))

