"""A class that represents a simple person."""

class Person():
    """A class to represent a person."""

    def __init__(self, first_name, last_name):
        """Initialize the attributes to describe a person."""
        self.first_name = first_name
        self.last_name = last_name

    def get_person_name(self):
        """Return a formatted name for our person."""
        return (self.first_name.title() + " " + self.last_name.title())

    def print_info(self):
        """Prints a copy of person information."""
        print("PERSON: " + self.get_person_name())