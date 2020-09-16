### 2020-09-15
### Author: Andrew Gottilla
### Video game class

class Video_Game():
    """A class to create a video game (duh)"""

    def __init__(self, title, developer, publisher):
        """Initialize the title, developer, and publisher attributes"""
        self.title = title
        self.developer = developer
        self.publisher = publisher

    def get_title(self):
        """Returns title of video game"""
        return self.title

    def get_developer(self):
        """Returns developer of video game"""
        return self.developer
    
    def get_publisher(self):
        """Returns publisher of video game"""
        return self.publisher

    def set_title(self, t):
        """Sets title of video game"""
        self.title = t

    def set_developer(self, dev):
        """Sets developer of video game"""
        self.developer = dev

    def set_publisher(self, pub):
        """Sets publisher of video game"""
        self.publisher = pub

    def print_vg(self):
        """Print all details of a video game"""
        print("TITLE: " + self.title.title())
        print("DEVELOPER: " + self.developer)
        print("PUBLISHER: " + self.publisher)