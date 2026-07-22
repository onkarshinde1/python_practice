class Playlist:
    def __init__(self):
        self.songs = []

    def add(self, song):
        self.songs.append(song)

    def __len__(self):
        return len(self.songs)


p = Playlist()
p.add("Song A")
p.add("Song B")
p.add("Song C")

print(len(p.songs))
print(len(p))
