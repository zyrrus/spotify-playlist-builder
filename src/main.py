import os, sys
import re

import spotipy
import spotipy.util as util

from playlist import Playlist

DIV = "======================================"

def intro():
    # Header -----------------------------------------
    print(DIV)
    print("|          Build a playlist          |")
    print(DIV)

    # Get title --------------------------------------
    title = input("Enter playlist name: ")

    # Instructions -----------------------------------
    print("\nOptions ------------------------------")
    print("r: (record) - (artist) to add an album\n" +
          "a: (artist) to add a whole artist\n" + 
          "q: to quit")
    print(DIV)

    return title

def get_songs(playlist):
    while True:
        # Get user input
        raw_text = input()

        # Split tags from artist/albums
        split_text = re.split(":\s*", raw_text, 1)
        tag = split_text[0]
        rest = split_text[1]

        # Parse the input
        if tag == "q":
            ## Quit
            break
        elif tag == "r":
            ## Add album
            pair = re.split("\s*-\s*", rest, 1)
            playlist.add_album(pair[0], pair[1])
        elif tag == "a":
            ## Add artist
            playlist.add_artist(rest)
    print(DIV)

def main(token):
    # Init Spotipy
    sp = spotipy.Spotify(auth=token)

    # Print intro and get title
    title = intro()

    # Create playlist 
    playlist = Playlist(sp, title)
    get_songs(playlist)

    # Create the playlist on Spotify
    playlist.create_playlist()
    print("Done")


if __name__ == '__main__':
    # Authenticate
    scope = 'playlist-modify-private, playlist-modify-public'
    username = sys.argv[1]
    
    # Authenticate user
    try:
        token = util.prompt_for_user_token(username, scope)
    except:
        os.remove(f".cache-{username}")
        token = util.prompt_for_user_token(username, scope)
    
    # Run if authenticated
    if token:
        main(token)
    else:
        print("Can't get token for", username)
