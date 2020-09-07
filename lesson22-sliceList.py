### 2020-09-07
### Author: Andrew Gottilla
### Lesson 22: Slicing a list

names = ['xavier', 'andrew', 'john', 'chantelle', 'dan', 'robin', 'juan', 'keisha', 'chris', 'erica', 'erika', 'angel', 'estevan']

# print a slice of names list from index 0 to 1
print(names[0:2])

# print a slice of names list from index 1 to 2
print(names[1:3])

# print a slice of names list from beginning to index 2
print(names[:3])

# print a slice of names list from index 2 to end
print(names[2:])

# a negative index returns an element a certain distance from end of list
# print a slice of names list that is the last 3 elements
print(names[-3:])