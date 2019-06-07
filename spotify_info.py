import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import requests
import json

def user_auth(username):
    scope = "user-read-currently-playing"
    client_id = ""
    client_secret = ""
    redirect_uri = ""
    try:
        creds = open("client.creds", "r")
        client_id = creds.readline().strip()
        client_secret = creds.readline().strip()
        redirect_uri = creds.readline().strip()
    except:
        print("Reading from credential file was unsuccessful")
        sys.exit()
    token = util.prompt_for_user_token(username, scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
    return token

def currently_playing(username):
    token = user_auth(username)
    url = "https://api.spotify.com/v1/me/player/currently-playing"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token
    }
    response = requests.get(url, headers=headers)
    json_data = json.loads(response.text)
    song = trim_song_title(json_data["item"]["name"])
    return song, json_data["item"]["artists"][0]["name"]

def trim_song_title(song):
    split_song = song.split(" ")
    index = 0
    result = ""
    for i in range(0, len(split_song)):
        if '(' in split_song[i] or '-' in split_song[i]:
            index = i
            print(i)
            break
    for i in range(0, index):
        if i == index - 1:
            result += split_song[i]
        else:
            result += split_song[i] + " "
    return result