### 2020-09-28
### Author: Andrew Gottilla
### Lesson 58: Inheritance

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

# Child class - inherits from parent class
class PatientInfo(Person):
    """Represents aspects of a person specific to a patient's information.
        Then initialize attributes specific to a patient's information."""

    ## Default values are allowed here as well. The example I've created here doesn't suit using this idea well.
    ## def __init__(self, first_name, last_name, gender, ethnicity, height, weight, temperature=98.6):
    def __init__(self, fname, lname, gender, ethnicity, height, weight):
        """Initialize attributes for out patient."""
        super().__init__(fname, lname)
        self.gender = gender
        self.ethnicity = ethnicity
        self.height = height # in inches
        self.weight = weight # in pounds

    ## Just a method to show that you can adjust num values using methods as well
    def adjust_weight(self, pounds):
        """Adjust weight gain/loss for our patient."""
        self.weight += pounds

    ## def switch_it_up(self, new_gender):
    def set_gender(self, new_gender):
        """Adjusts the gender of our pateint."""
        self.gender = new_gender

    def print_info(self):
        """Print out copy of medical record information."""
        print("PATIENT: " + self.get_person_name())
        print("Gender: " + self.gender, end='')
        print("\tEthnicity: " + self.ethnicity)
        print("Height: " + str(int(self.height/12)) + "'" + str(self.height%12) + "\"", end='')
        print("\tWeight: " + str(self.weight) + " lbs")

p = PatientInfo("Andrew", "Gottilla", "Dude", "Sicilian", 71, 145.5)
print(p.get_person_name())
p.print_info()

print()

# Let's say time passed and I started to eat more and exercise
# I put on some more muscle since the last visit
# Also I had surgery
p.adjust_weight(8)
p.set_gender("Dudette")
p.print_info()