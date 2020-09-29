### 2020-09-28
### Author: Andrew Gottilla
### Lesson 60: Importing classes

# import a single class from module
from video_game_class import Video_Game

# import a single class from a module with multiple classes
from multiple_classes import PatientInfo

# import multiple classes from a module with multiple classes
from multiple_classes import Person, Date

# import whole module
## import multiple_classes
## you will later need to use the proper syntax/notation
## e.g. multiple_classes.Video_Game . . .

# import all classes from module
## from multiple_classes import *
## you will not need to use the prior notation
## not recommended since this will make troubleshooting much harder


new_game = Video_Game('Some game', 'Some dev', 'Some publisher')
new_game.set_esrb('m')
print("- - Video game - -")
new_game.print_vg()
print()

some_date = Date(2020, 2, 18)
generic_patient = PatientInfo('Some', 'Dude', 'Dude', 'Genersian', 70, 145, some_date)
generic_patient.print_info()
