### 2020-09-07
### Author: Andrew Gottilla
### Lesson 23: Looping through a slice

names = ['xavier', 'andrew', 'john', 'chantelle', 'dan', 'robin', 'juan', 'keisha', 'chris', 'erica', 'erika', 'angel', 'estevan']

# looping through slice using for loop
print ("Here are the names of the last three dudes:")
for name in names[-3:]:
    print(name.title())