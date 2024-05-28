import globals
import os
from colorama import init, Fore, Back, Style
from dynamic_typing_func import print_dynamic_text_1_1 as dynamic

def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear') # checks what kind of command to apply depending on the system

def hide_cursore():
    print('\033[?25l', end="")
    
def screen():
    """prints the screen"""
    clean_screen()
    hide_cursore()
    # screen separator for better readability
    print( Style.DIM + globals.main_str.format(left=u"#" * 30, center=u"#" * 140, right="#" * 30))
    print(globals.main_str.format(left=" " * 30, center=u"#" * 140, right=" " * 30 + Style.RESET_ALL))
    
    # upper bar with time left and current room
    print(Style.DIM + globals.main_str.format(left="Time before sunset " + Style.RESET_ALL + Fore.RED + Style.BRIGHT+ str(globals.time_left) + Fore.RESET  + Style.RESET_ALL + Style.DIM + " min" + Style.RESET_ALL,
                                    center=" " * 152,
                                    right= Style.DIM + "You are in "+ Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + globals.current_room.name.upper() + Style.RESET_ALL ))
   
    # separation line
    print( Style.DIM + globals.main_str.format(left="_" * 30, center = "_" * 140, right = "_" * 30 ) + Style.RESET_ALL)
    
    # status bar indicates progress and gives clues on what needs to be done
    print(globals.main_str.format(left=Style.DIM + "status:" + Style.RESET_ALL, center = globals.status, right = "" ))

     # separation line
    print(Style.DIM + globals.main_str.format(left="_" * 30, center = "_" * 140, right = "_" * 30 ) + Style.RESET_ALL)
   
    # prints inventory or its lack
    if len(globals.inventory) == 0:
        print(globals.main_str.format(left= Style.DIM + "You have:" + Style.RESET_ALL, center ="You are empty handed", right = "" ))
    else:
        print(globals.main_str.format(left= Style.DIM + "You have:" + Style.RESET_ALL, center = ', '.join(globals.inventory), right = "" ))

    # separation line
    print(Style.DIM + globals.main_str.format(left="_" * 30, center = "_" * 140, right = "_" * 30 )+ Style.RESET_ALL)
    print(globals.main_str.format(left=" " * 30, center = " " * 140, right = " " * 30 ))
    # askii test

    
    for i in globals.current_room.map:
        print(Style.BRIGHT  + i + Style.RESET_ALL)

    
     # separation line
    print(Style.DIM + globals.main_str.format(left="_" * 30, center = "_" * 140, right = "_" * 30 )+ Style.RESET_ALL)
    print(globals.main_str.format(left=" " * 30, center = " " * 140, right = " " * 30 ))
    # room description, I loop through it since some are pretty lengthy, that helps to display it nice.
    # dynamic()
    for i in globals.description:
        print(globals.main_str.format( left='', center=''.join(i), right=''))
      
        

    # separation line
    print(Style.DIM + globals.main_str.format(left="_" * 30, center = "_" * 140, right = "_" * 30 )+ Style.RESET_ALL)
    print(globals.main_str.format(left=" " * 30, center = " " * 140, right = " " * 30 ))
    # instructions
    print(Style.DIM + globals.main_str_long_sides.format(left=globals.general_instructions_move, center ="", right=globals.general_instructions_usage) + Style.RESET_ALL)

    # screen separator for better readability
    # separation line
    print(Style.DIM + globals.main_str.format(left="_" * 30, center = "_" * 140, right = "_" * 30 )+ Style.RESET_ALL)
