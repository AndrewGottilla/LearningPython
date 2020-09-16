### 2020-09-15
### Author: Andrew Gottilla
### Lesson 55: Importing modules and functions

# import a module, a function, a module with an alias, and a function with an alias
import lesson54_module
# from lesson54_module import * # also imports all functions
import lesson55_module as vgmod
# from lesson55_module import print_video_game # importing a function
# from lesson55_module import default_video_game as def_vg # importing function as alias

print("- - Made Video Game - -")
# using create_video_game() function from module
new_game = lesson54_module.create_video_game("The Last of Us Part II", "Naughty Dog", price=59.99, publisher="Sony Interactive Entertainment")
# using print_video_game() function from module using alias
vgmod.print_video_game(new_game)

# using clear_video_game() function from module using alias
print("- - Clear Video Game - -")
new_game = vgmod.clear_video_game()
vgmod.print_video_game(new_game)

#using def_video_game() with alias def_vg() from module using alias
print("- - Default Video Game - -")
new_game = vgmod.default_video_game()
vgmod.print_video_game(new_game)
