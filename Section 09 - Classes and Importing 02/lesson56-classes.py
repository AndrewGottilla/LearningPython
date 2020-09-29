### 2020-09-15
### Author: Andrew Gottilla
### Lesson 56: Classes (Finally, the fun part)

class Video_Game():
    """A class to create a video game (duh)."""

    def __init__(self, title, developer, publisher):
        """Initialize the title, developer, and publisher attributes"""
        self.title = title
        self.developer = developer
        self.publisher = publisher

    def print_vg(self):
        """Print all details of a video game"""
        print("TITLE: " + self.title.title())
        print("DEVELOPER: " + self.developer)
        print("PUBLISHER: " + self.publisher)


print("- - First Game - -")
# initialize class
my_vg = Video_Game("Nier: Automata", "Platinum Games", "Square Enix")
# use print method
my_vg.print_vg()
print()

print("- - Second Game - -")
# another class
ur_vg = Video_Game("Yoshi's Island", "Nintendo", "Nintendo")
# wow who woulda guessed
ur_vg.print_vg()
print()
