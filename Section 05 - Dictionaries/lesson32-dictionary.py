### 2020-09-08
### Author: Andrew Gottilla
### Lesson 32: Dictionaries

# Video game dictionary
video_game = {'title' : 'The Last of Us Part II', 'director' : 'Neil Druckmann', 'price' : 59.99}

# Print video game information and include video game price if video game has price key
print(video_game['title'] + " is directed by " + video_game['director'], end='')
if 'price' in video_game:
    print(" and it costs " + str(video_game['price']) + '.')
else:
    print('.')

video_game['rating'] = "M for Mature"

print(video_game['title'] + " is rated " + video_game['rating'] + '.')
