### 2020-09-14
### Author: Andrew Gottilla
### Lesson 53: Arbitrary key-value arguments

def create_video_game(title, developer, **other):
    """Assign some info to a video game dictionary"""
    video_game = {}
    video_game['title'] = title
    video_game['developer'] = developer
    for key, value in other.items():
        video_game[key] = value
    return video_game

new_game = create_video_game("The Last of Us Part II", "Naughty Dog", price=59.99, publisher="Sony Interactive Entertainment")
print(new_game)