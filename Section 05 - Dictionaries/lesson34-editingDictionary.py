### 2020-09-08
### Author: Andrew Gottilla
### Lesson 34: Editing Dictionaries

# Video game dictionary
video_game = {
    'title' : 'The Last of Us Part II',
    'developer' : "Naughty Dog",
    'director' : 'Neil Druckmann',
    'price' : 59.99
}

# Print dictionary
print("Video game dictionary:\n" + str(video_game))

# Looping through key-value pairs
print("\n- - Video game dictionary breakdown - -")
for key, val in video_game.items():
    print("Key: " + key + "\n   -Value: " + str(val))
print()

# Delete item from dictionary
del video_game['price']
print("Video game (price deleted):\n" + str(video_game))
print()

# Add item to dictionary
video_game['rating'] = "M for Mature"
print("Video game (rating added):\n" + str(video_game))
print()
