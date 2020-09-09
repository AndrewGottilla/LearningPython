### 2020-09-08
### Author: Andrew Gottilla
### Lesson 33: The get() method

# The get() method will print a statement or nothing if key does not exist
video_game = {'title' : 'The Last of Us Part II', 'director' : 'Neil Druckmann', 'price' : 59.99}

print(video_game.get('title'))
print(video_game.get('price', 'Sorry, the game does not have a price yet.'))