"""A class that represents a simple video game."""

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
