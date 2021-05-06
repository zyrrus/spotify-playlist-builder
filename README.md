# Playlist Builder
Given a list of artists and albums, a playlist of all the songs from the albums and all the artist's songs will be created.

## How to use
1. Set the three environment variables: SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, and SPOTIPY_REDIRECT_URI <br>
The first two can be found on the Spotify for Developers Dashboard page after creating a new project (I don't plan on hosting this anywhere). <br>
The third can be any valid url (ex: your github.io page) <br>
NOTE: On Windows, just fill out the empty variables in playlist.bat and set up a Python virtualenv
2. run main.py (or the batch file if on Windows) while passing in your Spotify username as a command-line argument (ex: playlist.bat my_spotify_name)

# Example
```
======================================
|          Build a playlist          |
======================================
Enter playlist name: dummy-playlist

Options ------------------------------
r: (record) - (artist) to add an album
a: (artist) to add a whole artist
q: to quit
======================================
a: artist1
a: artist2
r: album - artist1
======================================
Done
```
