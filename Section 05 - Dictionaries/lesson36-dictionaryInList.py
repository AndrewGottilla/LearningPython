### 2020-09-09
### Author: Andrew Gottilla
### Lesson 36: List of dictionaries

# Video game dictionaries
video_game_0 = {
    'title' : 'The Last of Us Part II',
    'developer' : "Naughty Dog",
    'rating' : 'M',
    'price' : 59.99
}
video_game_1 = {
    'title' : 'Call of Duty: World at War',
    'developer' : "Treyarch",
    'rating' : 'M',
    'price' : 19.99
}
video_game_2 = {
    'title' : 'Super Smash Bros. Ultimate',
    'developer' : "Nintendo",
    'rating' : 'E10+',
    'price' : 59.99
}

# Create list of dictionaries
video_games = [video_game_0, video_game_1, video_game_2]

# Printing list of dictionaries
print("\n- - Video Game List Of Dictionaries - -")
print("------------------------------------")
for vg in video_games:
    for key, val in vg.items():
        print(key.title() + ": " + str(val))
    print()

# - OR SIMPLY -
#>for vg in video_games:
#>    print(vg)

# Inventory dictionary
inventory = []

# Make 50 new games for inventory
for new_game in range(0,50):
    new_game = {'title' : 'Rad new shooter', 'developer' : 'Big company', 'rating' : 'M', 'price' : 59.99}
    inventory.append(new_game)

# Replacing some of the inventory
for game in inventory[0:15]:
    if game['title'] == "Rad new shooter":
        game['title'] = "Sick new platformer"
        game['rating'] = 'E'

# Printing list of dictionaries (up to 5 items in this case)
print("\n- - 5 Most Recent Games In Stock - -")
print("------------------------------------")
for game in inventory[0:5]:
    for key, val in game.items():
        print(key.title() + ": " + str(val))
    print()

# - OR SIMPLY -
#>for game in inventory[0:5]:
#>  print(game)
