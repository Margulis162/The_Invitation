import globals
import os
from dynamic_typing_func import print_dynamic_text_1_1 as dynamic
from askii import tuplarizator

def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear') # checks what kind of command to apply depending on the system

def hide_cursore():
    print('\033[?25l', end="")
    
def screen():
    """prints the screen"""
    clean_screen()
    hide_cursore()
    # screen separator for better readability
    print(globals.main_str.format(left="#" * 30, center="#" * 140, right="#" * 30))
    print(globals.main_str.format(left=" " * 30, center="#" * 140, right=" " * 30))
    
    # upper bar with time left and current room
    print(globals.main_str.format(left=f"time before sunset {globals.time_left} min",
                                    center=" " * 140,
                                    right=f"You are in {globals.current_room.upper()}"))
   
    # separation line
    print(globals.main_str.format(left="_" * 30, center = "_" * 140, right = "_" * 30 ))
    
    # status bar indicates progress and gives clues on what needs to be done
    print(globals.main_str.format(left="status:", center = globals.status, right = "" ))

     # separation line
    print(globals.main_str.format(left="_" * 30, center = "_" * 140, right = "_" * 30 ))
   
    # prints inventory or its lack
    if len(globals.inventory) == 0:
        print(globals.main_str.format(left="You have:", center ="You are empty handed", right = "" ))
    else:
        print(globals.main_str.format(left="You have:", center = ''.join(globals.inventory), right = "" ))

    # separation line
    print(globals.main_str.format(left="_" * 30, center = "_" * 140, right = "_" * 30 ))
    print(globals.main_str.format(left=" " * 30, center = " " * 140, right = " " * 30 ))
    # askii test

    # FIXME the aski portion is a mess, do not recomend to tuch it until I'm done with it
    
    art = tuplarizator.make_tuple("askii/inner_dungeon.txt")
    for i in art:
        print(globals.main_askii.format(center=i))


    
     # separation line
    print(globals.main_str.format(left="_" * 30, center = "_" * 140, right = "_" * 30 ))
    print(globals.main_str.format(left=" " * 30, center = " " * 140, right = " " * 30 ))
    # room description, I loop through it since some are pretty lengthy, that helps to display it nice.
    # dynamic()
    for  i in globals.description:
        print(globals.main_str.format( left='', center=''.join(i), right=''))
      
        

    # separation line
    print(globals.main_str.format(left="_" * 30, center = "_" * 140, right = "_" * 30 ))
    print(globals.main_str.format(left=" " * 30, center = " " * 140, right = " " * 30 ))
    # instructions
    print(globals.main_str_long_sides.format(left=globals.general_instructions_move, center ="", right=globals.general_instructions_usage))

    # screen separator for better readability
    # separation line
    print(globals.main_str.format(left="_" * 30, center = "_" * 140, right = "_" * 30 ))
