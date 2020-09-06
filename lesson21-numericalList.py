### 2020-09-06
### Author: Andrew Gottilla
### Lesson 21: Numerical lists (aka Big Data baybeeee)

# Create list of numbers from 1 to 5
numbers = list(range(1,6))
print (numbers)

# Create list of odd numbers from 1 to 50
odd_numbers = list(range(1,51,2))
print(odd_numbers)

# Create list of squared numbers
squares = []
for val in range(1,10):
    squares.append(val ** 2)
print(squares)

# using min() function to print lowest number in list
print(min(numbers))

# using max() function to print highest number in list
print(max(numbers))

# using sum() function to print sum of all numbers in a list
print(sum(numbers))
