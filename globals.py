import timer
# to keep timer in separate
import threading
import json
# to get terminal size
import shutil

# constants


# class Room:
"""suppose to replace you_see and rooms"""

    # def __init__(self, name, description, directions, items, map):
    #     self.name = name
    #     self.description = description  # suppose to replace you_see 
    #     self.directions = directions
    #     self.items = items
    #     self.map = map


# def data_extractor():
"""extracts data from json file and turns em into python dict"""
    # with open('rooms.json', 'r') as f:
    #     raw_data = f.read()
    #     data = json.loads(raw_data)
    #     return data


# def rooms_populator(rooms):
"""populates roomz with room objects, shall I rename it?"""
    # roomz = []
    # for key in rooms:
    #     roomz.append(Room(key, rooms[key]['description'], rooms[key]['directions'], rooms[key]['items']))
    # return roomz


# rooms_data = data_extractor()

# roomz = rooms_populator(rooms_data)

# formatting

screen_len = shutil.get_terminal_size().columns
main_str = '{left:<30}{center:^140}{right:>30}'.center((screen_len - 100) // 2)
main_str_long_sides = '{left:<80}{center:^40}{right:>80}'.center((screen_len - 100) // 2)
main_askii = '{center:^200}'.center((screen_len - 100) // 2)
general_instructions_move = r'type a direction to move. Example: "west"'
general_instructions_usage = r'type "take a/the" + "item name" to grab an item. Example: "take gloves"'

# Typing speed types:
text_speeds = {"fast": 0.01,
               "medium": 0.04,
               "slow": 0.06
               }

# for checking for unknown command
all_commands = {
    "moves":
        ('east', 'west', 'north', 'south'),
    "items":
        ('take the key', 'take the gloves', 'take the karate guide', 'take the drink', 'take a slice'),
}

# variables
victory = False

# status is also a condition for victory
status = 'You are hungry, low on energy, and have no way to defend yourself'

# end game status for debugging
# status = 'You are well-fed, energized, and know few karate kicks'

time_left = 5  # this one is adjusted to allow more or less time for completion

current_room = 'inner dungeon'

# Indicates the player's selected typing speed. It is set to medium by default.
selected_text_speed = None

# if inventory is empty
no_items = 'You are empty handed'

inventory = []

command = ""

# this one is responsible for dynamic typing 
description = [[''], [''], [''], ['']]  # just so the bottom lines do not jump

# starts timer in a separate thread
thread_timer = threading.Thread(target=timer.timer)

you_see = {
    'inner dungeon': [
        "You wake up inside of the dungeon chambers.",
        "The bars of the chamber are ridiculously far apart. Escape will be quite simple.",
        "There is also a door on the SOUTH wall."  
    ],
    'outer dungeon': [
        "Upon entry, you notice a skeleton holding an energy drink in it's bony hands.",
        "It's bones look cold and slimy. You should probably look for GLOVES before trying to TAKE THE DRINK!",
        "You can go WEST and NORTH from here."
    ],
    'main hallway': [
        "A menagerie of macabre paintings string the walls.",
        "Unfortunately, you have little time to absorb their meaning.",
        "You can go all directions from here."
    ],
    'the great hall': [
        "This hall is likely where the 'party' is supposed to be held.",
        "The room is quite spacious, but poorly maintained. Dust, spiderwebs and bloodstains are scattered everywhere.",
        "In the corner, you notice a pizza box. Why not TAKE A SLICE?",
        "You can go EAST and NORTH from here."
    ],
    'bed chambers': [
        "The chambers are disturbingly empty, save for the fancy coffin at the chamber's center.",
        "The lid is closed for now. Upon closer inspection, you see a KEY laying beside the coffin.",
        "You can go WEST from here."
    ],
    'laboratory': [
        "This is where the undead do their unholy research.",
        "The walls are covered with jars containing a variety of preserved creatures.",
        "You feel like some of them are staring at you. You can TAKE THE GLOVES lying on one of the counter tops.",
        "You can go EAST and SOUTH from here."
    ],
    'library': [
        "The rows of shelves loaded with knowledge feel nearly endless.",
        "While searching through the books, you encounter the KARATE GUIDE. That could be really useful!",
        "You can go WEST from here."
    ],
    'entrance': [
        "While attempting to escape, the doors shut behind you. A henchman is guarding the exit",
        "and you are not ready to take him on. He grins at you, and you go back slowly.",
        "The doors are super heavy. It takes you many seconds to open them.",
        "You lost a lot of extra time from this endeavor. Perhaps you should look for more items to help you.",
    ]
}

# dict
rooms = {
    'inner dungeon': [
        {'south': 'outer dungeon'},
        {'items': []}],
    'outer dungeon': [
        {'north': 'inner dungeon', 'west': 'main hallway'},
        {'items': ['energy drink']}
    ],
    'main hallway': [
        {'south': 'the great hall', 'west': 'entrance', 'north': 'laboratory', 'east': 'outer dungeon'},
        {'items': []}
    ],
    'the great hall': [
        {'north': 'main hallway', 'east': 'bed chambers'},
        {'items': ['slice of pizza']}
    ],
    'bed chambers': [
        {'west': 'the great hall'},
        {'items': ['key']}
    ],
    'laboratory': [
        {'south': 'main hallway', 'east': 'library'},
        {'items': ['gloves']}
    ],
    'library': [
        {'west': 'laboratory'},
        {'items': ['karate guide']}
    ],
    'entrance': [
        {},
        {}
    ],
}

maps = { 

    'inner dungeon': (
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                       _________________   ______     _____                             ',
        '                                                                                                                                      |                 |_|      |   |     |                            ',
        '                                                                                                                                      |                  _       |   |  X  |                            ',
        '                                                                                                                                      |_______   _______| |______|   |_   _|                            ',
        '                                                                                                                              _____    _______| |_______              _| |_                             ',
        '                                                                                                                         o   |     |__|                 |____________|     |                            ',
        '                                                                                                               <----    /|\         __                   ____________      |                            ',
        '                                                                                                                         A   |_____|  |_______   _______|            |_____|                            ',
        '                                                                                                                        / \            _______| |________   ______                                      ',
        '                                                                                                                                      |                  |_|      |                                     ',
        '                                                                                                                                      |                   _       |                                     ',
        '                                                                                                                                      |__________________| |______|                                     ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        '
    ),

    'outer dungeon': (
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                       _________________   ______     _____                             ',
        '                                                                                                                                      |                 |_|      |   |     |                            ',
        '                                                                                                                                      |                  _       |   |     |                            ',
        '                                                                                                                                      |_______   _______| |______|   |_   _|                            ',
        '                                                                                                                              _____    _______| |_______              _| |_                             ',
        '                                                                                                                         o   |     |__|                 |____________|     |                            ',
        '                                                                                                               <----    /|\         __                   ____________   X  |                            ',
        '                                                                                                                         A   |_____|  |_______   _______|            |_____|                            ',
        '                                                                                                                        / \            _______| |________   ______                                      ',
        '                                                                                                                                      |                  |_|      |                                     ',
        '                                                                                                                                      |                   _       |                                     ',
        '                                                                                                                                      |__________________| |______|                                     ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        '
    ),

    'main hallway': (
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                       _________________   ______     _____                             ',
        '                                                                                                                                      |                 |_|      |   |     |                            ',
        '                                                                                                                                      |                  _       |   |     |                            ',
        '                                                                                                                                      |_______   _______| |______|   |_   _|                            ',
        '                                                                                                                              _____    _______| |_______              _| |_                             ',
        '                                                                                                                         o   |     |__|                 |____________|     |                            ',
        '                                                                                                               <----    /|\         __         X         ____________      |                            ',
        '                                                                                                                         A   |_____|  |_______   _______|            |_____|                            ',
        '                                                                                                                        / \            _______| |________   ______                                      ',
        '                                                                                                                                      |                  |_|      |                                     ',
        '                                                                                                                                      |                   _       |                                     ',
        '                                                                                                                                      |__________________| |______|                                     ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        '
    ),

    'the great hall': (
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                       _________________   ______     _____                             ',
        '                                                                                                                                      |                 |_|      |   |     |                            ',
        '                                                                                                                                      |                  _       |   |     |                            ',
        '                                                                                                                                      |_______   _______| |______|   |_   _|                            ',
        '                                                                                                                              _____    _______| |_______              _| |_                             ',
        '                                                                                                                         o   |     |__|                 |____________|     |                            ',
        '                                                                                                               <----    /|\         __                   ____________      |                            ',
        '                                                                                                                         A   |_____|  |_______   _______|            |_____|                            ',
        '                                                                                                                        / \            _______| |________   ______                                      ',
        '                                                                                                                                      |                  |_|      |                                     ',
        '                                                                                                                                      |        X          _       |                                     ',
        '                                                                                                                                      |__________________| |______|                                     ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        '
    ),

     'bed chambers':(
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                       _________________   ______     _____                             ',
        '                                                                                                                                      |                 |_|      |   |     |                            ',
        '                                                                                                                                      |                  _       |   |     |                            ',
        '                                                                                                                                      |_______   _______| |______|   |_   _|                            ',
        '                                                                                                                              _____    _______| |_______              _| |_                             ',
        '                                                                                                                         o   |     |__|                 |____________|     |                            ',
        '                                                                                                               <----    /|\         __                   ____________      |                            ',
        '                                                                                                                         A   |_____|  |_______   _______|            |_____|                            ',
        '                                                                                                                        / \            _______| |________   ______                                      ',
        '                                                                                                                                      |                  |_|      |                                     ',
        '                                                                                                                                      |                   _   X   |                                     ',
        '                                                                                                                                      |__________________| |______|                                     ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        '
     ),

      'laboratory':(
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        ',
        '                (o__0)   (@__@)  (X__x)                                                                                                _________________   ______     _____                             ',
        '                                                                                                                                      |                 |_|      |   |     |                            ',
        '                                                                                                                                      |        X         _       |   |     |                            ',
        '                                                                                                                                      |_______   _______| |______|   |_   _|                            ',
        '                                                                                                                              _____    _______| |_______              _| |_                             ',
        '                                                                                                                         o   |     |__|                 |____________|     |                            ',
        '                                                                                                               <----    /|\         __                   ____________      |                            ',
        '                                                                                                                         A   |_____|  |_______   _______|            |_____|                            ',
        '                                                                                                                        / \            _______| |________   ______                                      ',
        '                                                                                                                                      |                  |_|      |                                     ',
        '                                                                                                                                      |                   _       |                                     ',
        '                                                                                                                                      |__________________| |______|                                     ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        '
      ), 

    'library':(
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                       _________________   ______     _____                             ',
        '                                                                                                                                      |                 |_|      |   |     |                            ',
        '                                                                                                                                      |                  _   X   |   |     |                            ',
        '                                                                                                                                      |_______   _______| |______|   |_   _|                            ',
        '                                                                                                                              _____    _______| |_______              _| |_                             ',
        '                                                                                                                         o   |     |__|                 |____________|     |                            ',
        '                                                                                                               <----    /|\         __                   ____________      |                            ',
        '                                                                                                                         A   |_____|  |_______   _______|            |_____|                            ',
        '                                                                                                                        / \            _______| |________   ______                                      ',
        '                                                                                                                                      |                  |_|      |                                     ',
        '                                                                                                                                      |                   _       |                                     ',
        '                                                                                                                                      |__________________| |______|                                     ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        '
    ),

    'entrance':(
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                       _________________   ______     _____                             ',
        '                                                                                                                                      |                 |_|      |   |     |                            ',
        '                                                                                                                                      |                  _       |   |     |                            ',
        '                                                                                                                                      |_______   _______| |______|   |_   _|                            ',
        '                                                                                                                              _____    _______| |_______              _| |_                             ',
        '                                                                                                                         o   |     |__|                 |____________|     |                            ',
        '                                                                                                               <----    /|\     X   __                   ____________      |                            ',
        '                                                                                                                         A   |_____|  |_______   _______|            |_____|                            ',
        '                                                                                                                        / \            _______| |________   ______                                      ',
        '                                                                                                                                      |                  |_|      |                                     ',
        '                                                                                                                                      |                   _       |                                     ',
        '                                                                                                                                      |__________________| |______|                                     ',
        '                                                                                                                                                                                                        ',
        '                                                                                                                                                                                                        '
    ) 
}