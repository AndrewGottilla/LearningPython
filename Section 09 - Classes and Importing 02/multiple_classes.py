# Parent class (in the context of PatientInfo)
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

# Child class - inherits from parent class
class PatientInfo(Person):
    """Represents aspects of a person specific to a patient's information.
        Then initialize attributes specific to a patient's information."""

    ## Default values are allowed here as well. The example I've created here doesn't suit using this idea well.
    ## def __init__(self, first_name, last_name, gender, ethnicity, height, weight, temperature=98.6):
    def __init__(self, fname, lname, gender, ethnicity, height, weight, date=Date()):
        """Initialize attributes for out patient."""
        super().__init__(fname, lname)
        self.gender = gender
        self.ethnicity = ethnicity
        self.height = height # in inches
        self.weight = weight # in pounds
        self.dob = date

    ## Just a method to show that you can adjust num values using methods as well
    def adjust_weight(self, pounds):
        """Adjust weight (gain/loss) for our patient."""
        self.weight += pounds

    ## def switch_it_up(self, new_gender):
    def set_gender(self, new_gender):
        """Adjust the gender of our pateint."""
        self.gender = new_gender

    def print_info(self):
        """Print out copy of medical record information."""
        print("PATIENT: " + self.get_person_name(), end='')
        print("   DOB: " + self.dob.get_date())
        print("Gender: " + self.gender, end='')
        print("\t  Ethnicity: " + self.ethnicity)
        print("Height: " + str(int(self.height/12)) + "'" + str(self.height%12) + "\"", end='')
        print("\t  Weight: " + str(self.weight) + " lbs")
