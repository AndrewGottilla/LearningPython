### 2020-09-08
### Author: Andrew Gottilla
### Lesson 35: Dictionary methods

# Survey dictionary: participant : favorite flavor
fav_chips_survey = {
    'andrew': 'Dill Pickle',
    'chris' : 'BBQ',
    'thomas': 'Honey BBQ',
    'mike'  : 'Salt and Vinegar',
    'bobby' : 'Original',
    'hank'  : 'BBQ',
    'peggy' : 'Original',
    'tony'  : 'Salt and Vinegar',
    'bill'  : 'Jalapeno',
    'ted'   : 'BBQ'
}

print("- - Favorite Chips Survey - -\n")

# Printing all keys of a dictionary : .keys() method
print("Participants:")
for participant in fav_chips_survey.keys():
    print(participant.title() + ", ", end='')
print("and myself! Just kidding.\n")

# Printing the key-value pairs while looping : .items() method
print("Survey results:")
for key, val in fav_chips_survey.items():
    print("Participant: " + key.title() + "\n   -Favorite flavor: " + val)
print()

# Using set() function to print all unique values of dictionary : .values() method
print("All unique chip flavors:")
for flavor in set(fav_chips_survey.values()):
    print("-" + flavor)
print()