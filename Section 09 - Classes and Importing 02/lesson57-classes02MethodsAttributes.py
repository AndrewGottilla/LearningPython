### 2020-09-28
### Author: Andrew Gottilla
### Lesson 57: Classes 02: methods and attributes

class Video_Game():
    """A class to create a video game (duh)."""

    def __init__(self, title, developer, publisher):
        """Initialize the title, developer, and publisher attributes"""
        self.title = title
        self.developer = developer
        self.publisher = publisher
        self.esrb = "rp" # Default value

    def print_vg(self):
        """Print all details of a video game"""
        print("TITLE: " + self.title.title())
        print("DEVELOPER: " + self.developer)
        print("PUBLISHER: " + self.publisher)
        print("ESRB: " + self.esrb.upper())

    def set_esrb(self, esrb):
        """Set the ESRB rating."""
        self.esrb = esrb


print("- - First Game - -")
my_vg = Video_Game("NieR: Re[in]carnation", "Applibot", "Square Enix")
my_vg.print_vg()
print()

print("- - Second Game - -")
ur_vg = Video_Game("Yoshi's Island", "Nintendo", "Nintendo")
ur_vg.set_esrb("e") # using method to modify attribute
ur_vg.print_vg()
print()

print("- - Third Game - -")
our_vg = Video_Game("Marvel's Spider-Man", "Insomniac Games", "Sony Interactive Entertainment")
our_vg.esrb = "t" # directly modify attribute
our_vg.print_vg()
print()
