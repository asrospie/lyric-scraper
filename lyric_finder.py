from bs4 import BeautifulSoup
import requests
import string

def linkBuilder(song, artist):
    song = song.translate(str.maketrans('', '', string.punctuation))
    artist = artist.translate(str.maketrans('', '', string.punctuation))
    base = "https://genius.com/"
    songList = song.split(" ")
    artistList = artist.split(" ")
    for i in artistList:
        if i == "":
            continue
        base += i + "-"
    for i in songList:
        if i == "":
            continue
        base += i + "-"
    base += "lyrics"
    return base

def getHtml(song, artist):
    return requests.get(linkBuilder(song, artist)).text

def getLyrics(song, artist):
    html = getHtml(song, artist)
    soup = BeautifulSoup(html, "html.parser")
    try:
        print(soup.select(".lyrics")[0].getText().strip())
    except IndexError:
        print("Song not found")