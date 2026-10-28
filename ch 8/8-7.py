def make_album(artist_name, album_title, no_songs=None):
    """To build an album for an artist"""
    artist_and_album = {'artist': artist_name, 'album': album_title}
    if no_songs:
       artist_and_album ['songs'] = no_songs
    return artist_and_album

album = make_album('eminem','slim shaddy',7)
print(album)

album = make_album('drake','ice man')
print(album)

album = make_album('lil wayne','i am music',10)
print(album)