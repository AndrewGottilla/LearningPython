### 2020-09-06
### Author: Andrew Gottilla
### Lesson 19: Looping through a list (aka getting to the good stuff)

# list of random names
months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

# using a for loop to print a list
# each indented line is read as part of loop in Python
for month in months:
    print(month.title())

# fill string with list values cuz why not
all_months = ''
for month in months:
    all_months += month.title() + ' '

print(all_months)