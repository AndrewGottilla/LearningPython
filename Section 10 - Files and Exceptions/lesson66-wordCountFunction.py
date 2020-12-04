### 2020-12-03
### Author: Andrew Gottilla
### Lesson 66: Word counting function

def word_count(filename):
    """Count the amount of words inside a file"""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print('ERROR: FILE NOT FOUND: [' + filename + '] !!')
    else:
        people = contents.split()
        num_people = len(people)
        print('There are ' + str(num_people) + ' words in ' + filename + '.')

filenames = ['people.txt', 'myself.txt', 'poo.txt']
for files in filenames:
    word_count(files)