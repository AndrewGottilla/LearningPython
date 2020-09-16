### 2020-09-09
### Author: Andrew Gottilla
### Simple game preorder program

# preorder reservation dictionary
preorder_prop = {}

# flag to indicate accepting reservations for preorder
preorders_open = True
# only 10 preorders reservations allowed
preorders_remaining = 10
while preorders_open and preorders_remaining > 0:
    # prompt user for name and address
    name = input("\nEnter your name: ").title()
    address = input("Enter shipping address: ")
    
    # only allow reservations for unique buyers
    if name in preorder_prop.keys():
        print("\n[ SORRY! ONLY ONE PREORDER PER PERSON! ]")
    else:
        # store reservation info into dictionary
        preorder_prop[name] = address
        preorders_remaining -= 1

    # ask if another user would like to reserve a preorder
    repeat = input("\nDoes another person want to preorder as well? (Y/N): ")
    if repeat.upper() == 'N':
        preorders_open = False
print()

# print message if all preorders were reserved
if preorders_remaining == 0:
    print("[ VERY SORRY! ALL PREORDERS HAVE BEEN SOLD! ]\n")

# print out list of preorder reservations
print("- -  -  - P R E O R D E R S   L I S T - - - -")
for name, add in preorder_prop.items():
    print(name + " at " + add + " is being sent a copy.")
print()
