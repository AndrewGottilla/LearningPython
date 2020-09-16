### 2020-09-08
### Author: Andrew Gottilla
### Lesson 28: Using in and not in statements

registered = ['xavier77', 'andrewman79', 'xX_j0hn_Xx', '101_ch4nte113', 'dantheman69']
admins = registered[0:2]

print("'- - '`~ Welcome to Champion's Lair v0.09b ~`' - -")

new_user = input("Enter a sick new username: ")

if new_user not in registered:
    print("\n[Congrats! That username is free.]")
else:
    print("\n[Username already taken!]")

if new_user in admins:
    print("\t└ THIS USERNAME BELONGS TO AN ADMIN")
else:
    print()
