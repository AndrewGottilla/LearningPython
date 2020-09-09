### 2020-09-09
### Author: Andrew Gottilla
### Lesson 40: Ending a while loop

prompt = "Please enter 'q' to quit the program.\nEnter your name: "
user_input = ""

# Simple while loop that stops when user enters q
print("This is an example of a while loop that requires user input to quit the program.\n")
while user_input != 'q':
    user_input = input(prompt).lower()
    print("User input: " + user_input.title() + '\n')
print("- - Loop over! - -\n")

# A flag variable acts as a signal to stop a loop
flag = True
while flag:
    user_input = input(prompt).lower()
    print("User input: " + user_input.title() + '\n')
    if user_input == 'q':
        flag = False
print("- - Loop over! - -\n")

# Using break statement to end continuous loop
while True:
    user_input = input(prompt).lower()
    print("User input: " + user_input.title() + '\n')
    if user_input == 'q':
        break
print("- - Loop over! - -\n")