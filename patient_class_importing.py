from person_class import Person
from date_class import Date

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