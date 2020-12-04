### 2020-12-03
### Author: Andrew Gottilla
### Lesson 61: Introduction to files

# using strip() when printing from files will eliminate the "hidden" endline (\n) chars at
# the end of each line in the file

print('= Printing all info from a single file =')
with open('myself.txt') as file_object:
    contents = file_object.read()
    print(contents.strip())
print()

# readlines() returns a list
print('= Printing all info from a single file [line by line] =')
with open('people.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())
print()

# manipulating lines works the same as any other list

# using pop()
popped = lines.pop()
print('= Post-popped info =')
for line in lines:
    print(line.strip())
print()

# using sort()
sort_list = lines.sort()
print('= Sorted popped info =')
for line in lines:
    print(line.strip())
print()