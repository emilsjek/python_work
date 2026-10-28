def make_album(artist_name, album_title):
    """To build an album for an artist"""
    artist_and_album = {'artist': artist_name, 'album': album_title}
    return artist_and_album

while True:
    print("\nPlease state the album details:")
    print("(enter q anytime to quit)")

    artist = input("What is the artists name: ")
    if artist == 'q':
        break

    album = input("What is the album name: ")
    if album == 'q':
        break

    created = make_album(artist, album)
    print(created)

