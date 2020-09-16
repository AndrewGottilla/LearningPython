### 2020-09-09
### Author: Andrew Gottilla
### Lesson 41: The continue statement

# List of numbers 0 to 99
number_list = []
for num in range(0,100):
    number_list.append(num)

# Loop through list and print all odd numbers
iterator = 0
while iterator <= len(number_list):
    iterator += 1
    # if number is even then continue else print number
    if iterator % 2 == 0:
        continue
    else:
        print(str(iterator), end=' ')
