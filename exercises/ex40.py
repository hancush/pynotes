class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def intro(self):
        print "Here, dude, let me tell you a story:"
        self.sing_song()
        print "Isn't life poignant?"

    def sing_song(self):
        for line in self.lyrics:
            print "\t" + line

lyrics = ["Will you tell all your friends",
          "You've got your gun to my head",
          "This song was only wishful thinking"]

go = Song(lyrics)

go.intro()

#happy_bday = Song(["Happy birthday to you",
#                   "I don't want to get sued",
#                   "So I'll stop right there"])

#bulls_on_parade = Song(["They rally around tha family",
#                        "With pockets full of shells"])

#happy_bday.sing_me_a_song()

#bulls_on_parade.sing_me_a_song()
