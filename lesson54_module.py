### 2020-09-14
### Author: Andrew Gottilla
### Lesson 54: Module

def create_video_game(title, developer, **other):
    """Assign some info to a video game dictionary"""
    video_game = {}
    video_game['title'] = title
    video_game['developer'] = developer
    for key, value in other.items():
        video_game[key] = value
    return video_game