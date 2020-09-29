"""A class that represents a simple date."""

# Component (to be used inside of PatientInfo)
class Date():
    """A class to represent a date."""

    def __init__(self, year=2020, month=9, day=28):
        """Initialize attributes for date."""
        self.year = year
        self.month = month
        self.day = day

    def get_date(self):
        return str(self.year) + "-" + str(self.month) + "-" + str(self.day)

    def set_date(self, y, m, d):
        """Set date."""
        self.year = y
        self.month = m
        self.day = d

    def print_info(self):
        print("DATE: " + str(self.year) + "-" + str(self.month) + "-" + str(self.day))
