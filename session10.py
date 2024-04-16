#Convert UML Diagram into python class and methods
class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def play(self):
        print(f"Playing '{self.title}' by {self.artist}")

class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"'{song.title}' removed from the playlist")
        else:
            print(f"'{song.title}' not found in the playlist")

    def play_all(self):
        if self.songs:
            print("Playing all songs in the playlist:")
            for song in self.songs:
                song.play()
        else:
            print("Playlist is empty")

# Eg:
song1 = Song("Nan Ready Dan", "Anirudh")
song2 = Song("Panju Mittai", "Deva")
song3 = Song("Thangamey", "Vijay Sethupathy")

playlist = Playlist()
playlist.add_song(song1)
playlist.add_song(song2)
playlist.add_song(song3)

playlist.play_all()

playlist.remove_song(song2)

playlist.play_all()

#END OF TASK SESSION10