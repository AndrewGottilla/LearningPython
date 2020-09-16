### 2020-09-07
### Author: Andrew Gottilla
### Lesson 25: Tuples

# only way to modify a tuple is by overwriting it
# Use tuples when you want to store a set of values that should not be changed
#   during the lifetime of the program
coordinates = (1003, 5069)
print("Original coordinates: ")
for c in coordinates:
    print(c)

coordinates = (2020, 6970)
print("New coordinates: ")
for c in coordinates:
    print(c)
