### Today
### Author: Andrew Gottilla
### Lesson 15: How to edit lists

# clear list : months = []
print("Let's fix this list!")
months = ['january', 'january', 'february', 'march', 'spril', 'june', 'july', 'august', 'september', 'october', 'november']
print('months: ' + str(months))
print()

# delete element of list
del months[1]
print('Duplicate month deleted.')
print('months: ' + str(months))
print()

# edit element of list
months[3] = 'april'
print("April fixed!")
print('months: ' + str(months))
print()

# insert element into list
months.insert(4, 'may')
print("May inserted!")
print('months: ' + str(months))
print()

# append (add to end) element into list
months.append('december')
print("Appended December!")
print('months: ' + str(months))
print()

print('months (fixed): ' + str(months))
