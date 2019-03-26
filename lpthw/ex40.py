'''class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    def list_words(self):
        for line in self.lyrics:
            print(line.split())

    def list_as_dict(self):
        for line in self.lyrics:
            print(line.strip(' '))

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

mexican_anthem = Song(["Mexicanos al grito de guerra",
                        "El acero aprestar del bridon",
                        "y retiemblen su centro la tierra"])

country_song = Song(["One, two, three like a bird I sing",
                    "All she has given me is a set of beautifull wings"])


mexican_anthem.list_words()
mexican_anthem.list_as_dict()'''

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        lst = []

        for line in self.lyrics:
            for w in line.split():
                if len(w) == 2:
                    lst.append(w)
            
        print(lst)

ly = ["Happy birthday to you", "I don't want to get sued", "So I'll stop right there"]

happy_bday = Song(ly)

happy_bday.sing_me_a_song()





























