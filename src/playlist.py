class Playlist():
    def __init__(self, spotify, name):
        self.spotify = spotify
        self.user = spotify.current_user()['id']
        self.name = name
        self.songs = []

    def print_songs(self):
        print(self.songs)

    def create_playlist(self):
        # Create playlist
        uri = self.spotify.user_playlist_create(self.user, self.name)['uri']

        
        # Remove duplicates
        songs = remove_duplictates(self.songs)

        # Break list of songs into groups of 100
        song_groups = [songs[i:i + 100] for i in range(0, len(songs), 100)]

        # Add songs
        for group in song_groups:
            self.spotify.playlist_add_items(uri, group)

    def add_album_from_uri(self, uri):
        # Add songs from album
        for track in self.spotify.album_tracks(uri)['items']:
            self.songs.append(track['uri'])

    def add_album(self, album, artist):
        # Find album
        q=f"album:{album} artist:{artist}"
        album = self.spotify.search(q, limit=1, type='album')['albums']['items'][0]['uri']
        
        # Add songs to list
        self.add_album_from_uri(album)

    def add_artist(self, artist):
        # Get artist
        q=f"{artist}"
        artist_uri = self.spotify.search(q, limit=1, type='artist')['artists']['items'][0]['uri']

        # Get artist's albums
        albums = self.spotify.artist_albums(artist_uri, album_type='album', limit=25)['items']
        for album in albums:
            self.add_album_from_uri(album['uri'])

def remove_duplictates(songs):
    clean = set()
    return [song for song in songs if not (song in clean or clean.add(song))]