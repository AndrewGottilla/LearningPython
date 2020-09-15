### 2020-09-14
### Author: Andrew Gottilla
### Lesson 48: Returning a dictionary from a function

def build_video_game(title, developer, publisher):
    """Create a dictionary of video game information"""
    vg = {'title' : title, 'developer' : developer, 'publisher' : publisher}
    return vg

def print_vg_shelf(shelf):
    """Properly print a list of video game dictionaries"""
    counter = 0
    for video_game in shelf:
        counter += 1
        print("GAME " + str(counter) + ": " + video_game['title'])
        print("DEVELOPER: " + video_game['developer'])
        print("PUBLISHER: " + video_game['publisher'])
        print()


# Shelf of video games
video_game_shelf = []

print("- - - Video Game Shelf - - -\n")
while True:
    # getting user input
    print("- ADDING VIDEO GAME -")
    title = input("Enter video game title: ")
    developer = input("Enter " + title + "'s developer: ")
    publisher = input("Enter " + title + "'s publisher: ")

    # creating video game dictionary using a function then adding it to a list
    new_video_game = build_video_game(title, developer, publisher)
    video_game_shelf.append(new_video_game)

    # user controlled loop (without any input validation just enter an 'n' or 'y' please)
    answer = input("\nWould you like to add another game to your shelf? (Y/N): ")
    print()
    if answer.strip().upper() == 'N':
        break
# end of while loop

# print video game shelf using function
print("- - - VIDEO GAME SHELF - - -")
print_vg_shelf(video_game_shelf)