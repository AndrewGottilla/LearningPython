### 2020-09-14
### Author: Andrew Gottilla
### Lesson 46: Returning value from function

def format_name(first_name, last_name):
    """Returns a full name"""
    full_name = first_name + " " + last_name
    return full_name.title()

myself = format_name('andrew', 'gottilla')
print(myself)

def get_formatted_name(email):
    """Returns a formatted username"""
    username = email.lower().strip()
    return username

user = get_formatted_name("Andrew_Gottilla@email.com     ")
print("User email is " + user + ".")
