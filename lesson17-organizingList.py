### 2020-09-06
### Author: Andrew Gottilla
### Lesson 17: Organizing a list

# list of scrambled names
names = ['xavier', 'andrew', 'john', 'chantelle', 'dan', 'robin', 'juan', 'keisha', 'chris', 'erica', 'erika', 'angel', 'estevan']
print('names:\n' + str(names) + '\n')

# using sort() method
names.sort()
print('names sorted:\n' + str(names) + '\n')

# using sort() method to reverse sort
names.sort(reverse=True)
print('names sorted in reverse:\n' + str(names) + '\n')

# reset list
names = ['xavier', 'andrew', 'john', 'chantelle', 'dan', 'robin', 'juan', 'keisha', 'chris', 'erica', 'erika', 'angel', 'estevan']
print('names reset:\n' + str(names) + '\n')

# using sorted() method to print a list after being sorted without altering list
print('names sorted but not altered:\n' + str(sorted(names)) + '\n')
print('You can see the names list is unaltered:\n' + str(names) + '\n')

# using reverse() method
names.reverse()
print('names reversed:\n' + str(names) + '\n')