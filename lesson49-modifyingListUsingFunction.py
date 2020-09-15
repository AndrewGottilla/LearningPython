### 2020-09-14
### Author: Andrew Gottilla
### Lesson 49: Modifying a list using a function

def update_donations(donation_queue, donation_list):
    """Simulate updating donations list."""
    print("- - FULFILLING DONATION QUEUE - -")
    while donation_queue:
        donator = donation_queue.pop()
        donation_list.append(donator)
        print("Thanks to " + donator + " for donating!")

def show_donation_list(donation_list):
    """Show all of the donators"""
    for ppl in donation_list:
        print(ppl)

d_queue = ['Andrew Gottilla', 'Nathan Drake', 'Cave Johnson', 'Gordon Freeman']
d_list = ['Sae Nijima']

update_donations(d_queue, d_list)
print("\n- - DONATION LIST - -")
show_donation_list(d_list)
print()