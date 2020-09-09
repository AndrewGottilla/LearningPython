### 2020-09-08
### Author: Andrew Gottilla
### Lesson 29: Python's if-elif-else chain

# Get user balance
balance = input("What is your bank balance?: $")

# Adjust output based on user balance
if int(balance) <= 0:
    print("Would you like to make a deposit?")
elif int(balance) <= 50:
    print("You do not qualify for interest.")
elif int(balance) < 100:
    print("Your interest rate is 1%.")
else:
    print("Your interest rate is 2%.")