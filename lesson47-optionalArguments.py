### 2020-09-14
### Author: Andrew Gottilla
### Lesson 47: Optional arguments

def format_name(first_name, last_name, middle_name=""):
    """Returns a full name"""
    if middle_name:
        full_name = first_name + " '" + middle_name + "' " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()

myself = format_name("andrew", "gottilla", "godzilla")
print(myself)

myself = format_name("andrew", "gottilla")
print(myself)