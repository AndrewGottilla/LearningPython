### 2020-12-03
### Author: Andrew Gottilla
### Lesson 64: Handling file exception

filename = input('Enter the name of the file to be printed (without .txt): ')

try:
    with open(filename + '.txt') as file_object:
        contents = file_object.read()
        print('\n= ----- FILE CONTENTS ----- =')
        print(contents.strip() + '\n')
except FileNotFoundError:
    print('ERROR: FILE NOT FOUND: [' + filename + '.txt] !!')