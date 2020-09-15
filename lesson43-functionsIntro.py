### 2020-09-14
### Author: Andrew Gottilla
### Lesson 43: Introduction to functions

# creating a function
def video_game(title, esrb): # function header. define the function
    """Displays a message about a video game.""" # function description
    print(title + " is a video game rated " + esrb + ".") # everything else tabbed is the function definition
    print() # including this line

video_game("God of War", "M for mature")
video_game("Beat Saber", "T for teen")
