### 2020-09-15
### Author: Andrew Gottilla
### Lesson 55: Another module

def print_video_game(video_game):
    """Print out all information about video game (dictionary)"""
    print("PRINTING VIDEO GAME - -")
    for key, val in video_game.items():
        print(key.title() + ": " + str(val))
    print()

def clear_video_game():
    """Returns an empty dictionary"""
    new_game = {}
    return new_game

def default_video_game():
    """Returns a default video game dictionary"""
    new_game = {'title' : 'Default Viddy Game', 'developer' : 'Some studio', 'publisher' : 'Some other studio'}
    return new_game