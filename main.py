from lyric_finder import getLyrics
from lyric_finder import linkBuilder
import subprocess as sp

def main():
    song = ""
    artist = ""
    while True:
        song = input("Enter the Song Title: ")
        if song.lower() == "exit":
            print("Goodbye")
            break
        artist = input("Enter the Artist's Name: ")
        if artist.lower() == "exit":
            print("Goodbye")
            break
        getLyrics(song, artist)
        print(linkBuilder(song, artist))
        print()
        input("Press any enter for a new song")
        sp.call('clear', shell=True)

main()