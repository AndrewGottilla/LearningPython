### 2020-09-14
### Author: Andrew Gottilla
### Lesson 52: Mixed arguments

def video_game(title, developer, *genre):
    """Assign some info to a video game"""
    print(title + " is a(n) ", end="")
    for g in genre:
        print(g, end=" ")
    print("game developed by " + developer + ".")

video_game("The Last of Us Part II", "Naughty Dog", "action-adventure", "survival", "shooter")
