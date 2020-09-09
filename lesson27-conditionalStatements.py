### 2020-09-07
### Author: Andrew Gottilla
### Lesson 27: Python's conditional statements

access = input("Would you like to access this lesson? (Y/N): ")
if access.upper() == "Y":
    print("\n- - - Access granted! Welcome! - - -")
else:
    print("\nNo problem! Goodbye.")
    # End program
    exit()

print()

print("If you will, a couple quick questions.")
your_age = input("How old are you?: ")
friend_age = input("How old is your best friend?: ")

# need to use int() function to handle user input as an int value instead of string
if int(your_age) >= 18 or int(friend_age) >= 18:
    print("\n! - - One of you is old enough to vote! Please vote this year! - - !")
else:
    print("\nNevermind. You're both too young to vote. Spread the word anyway!")

print()

print("This lesson will require some compliance. Do obey.")
apple = input("Please enter the word 'apple': ")
not_pear = input("Please don't enter the word 'pear': ")

if apple == 'apple' and not_pear != 'pear':
    print("\n- - ~`'Thank you for your compliance! Lesson complete!'`~ - -")
else:
    print("\nUnfortunately, the rules were not properly followed. Goodbye.")