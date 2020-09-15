### 2020-09-14
### Author: Andrew Gottilla
### Lesson 51: Arbitrary arguments

# the * symbol in the parameter tells Python to create a tuple that takes in whatever
# values it receieves
def create_passenger(*requests):
    """Summarize passenger requests"""
    print("\nThis passenger has requested: ")
    # print(requests)
    for request in requests:
        print("- " + request)


create_passenger('window seat', 'seat near top of plane', 'order drink ahead of time')
print()