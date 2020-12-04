### 2020-12-03
### Author: Andrew Gottilla
### Lesson 62: Writing to file

## w: Writing to a file. All file content is erased then replaced. ##
print('= Writing to a file / Creating new file =')

with open('new_person.txt', 'w') as file_object:
    # get info from user
    name = input('Enter a name for the new person: ')
    gender = input('Enter ' + name + '\'s gender: ').upper()
    age = str(input('Enter ' + name + '\'s age: '))
    state = input('Enter ' + name + '\'s state: ').upper()

    # write to file
    file_object.write(name + '\t' + gender + '\t' + age + '\t' + state)
print()

with open('new_person.txt') as file_object:
    print('= -----------------person file----------------- =')
    print(file_object.read())
print()

## a: Append to a file. All content is added to the end of the file. ##
print('= Appending to a file / Adding content to a file =')

with open('new_people.txt', 'a') as file_object:
    # get info from user
    name = input('Enter a name for the new person: ')
    gender = input('Enter ' + name + '\'s gender: ').upper()
    age = str(input('Enter ' + name + '\'s age: '))
    state = input('Enter ' + name + '\'s state: ').upper()

    # write to file
    file_object.write(name + '\t' + gender + '\t' + age + '\t' + state + '\n')
print()

with open('new_people.txt') as file_object:
    print('= -----------------people file----------------- =')
    print(file_object.read())