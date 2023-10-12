def make_album(artist_name, album_title, number_of_songs = None):
    album = {}
    album['artist_name'] = artist_name
    album['album_title'] = album_title
    if number_of_songs:
        album['number_of_songs'] = number_of_songs
    return album

album1 = make_album('Pink Floyd', 'The Wall')
print(album1)
album2 = make_album('Caparezza', 'Prisoner 709')
print(album2)
album3 = make_album('Pino Daniele', 'Terra Mia', 12)
print(album3)

while True:
    print("\nEnter the information about the album:")
    print("(enter 'q' any time if you want to quit the program)")
    artist = input("Artist Name: ")
    if artist == 'q':
        break
    title = input("Album Title: ")
    if title == 'q':
        break
    album = make_album(artist, title)
    print(f"\nGood, the album is created and it is: {album}")