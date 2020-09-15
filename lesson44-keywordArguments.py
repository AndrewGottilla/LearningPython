### 2020-09-14
### Author: Andrew Gottilla
### Lesson 44: Keyword arguments

def video_game(title, score):
    """Displays a message about a video game."""
    print(title + " is a video game with a score of " + str(score) + " out of 100.")
    print()

video_game(score=93, title='The Last of Us Part II')