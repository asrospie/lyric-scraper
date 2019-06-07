from lyric_finder import getLyrics
from lyric_finder import linkBuilder
import subprocess as sp
from spotify_info import currently_playing

def main():
    song = ""
    artist = ""
    username = input("Enter spotify username: ")
    while True:
        song, artist = currently_playing(username)
        sp.call('clear', shell=True)
        print("CURRENTLY PLAYING: " + song)
        print("ARTIST: " + artist)
        print()
        getLyrics(song, artist)
        print(linkBuilder(song, artist))
        print()
        response = input("Press any enter for a new song or type exit: ")
        if response.lower() == "exit":
            break
        sp.call('clear', shell=True)

main()