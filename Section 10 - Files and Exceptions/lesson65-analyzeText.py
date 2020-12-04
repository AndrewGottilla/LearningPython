### 2020-12-03
### Author: Andrew Gottilla
### Lesson 65: Analyzing text

filename = 'people.txt'

try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print('ERROR: FILE NOT FOUND: [' + filename + '] !!')
else:
    people = contents.split('\n')
    num_people = len(people)
    print('There are ' + str(num_people) + ' people in ' + filename + '!')