### 2020-09-09
### Author: Andrew Gottilla
### Lesson 37: Dictionary of lists aka game journalist generator

# Video game dictionary
video_game = {
    'title' : 'The Last of Us Part II',
    'developer' : "Naughty Dog",
    'rating' : 'M',
    'price' : 59.99,
    # list inside dictionary
    'genre' : ['action-adventure', 'survival', 'shooter']
}

# Print beginning of statement
print(video_game['title'] + " is a(n) ", end='')

# Printing a list inside of a dictionary
for genre in video_game['genre']:
    print(genre + ' ', end='')

# Print rest of output
print("developed by " + video_game['developer'] + ".")
print("This game is rated " + video_game['rating'] + ", so you already know what kind of experience you're in for.")
print("We expect to see " + video_game['title'] + " hit the shelves for the price of $" + str(video_game['price']) + "!")