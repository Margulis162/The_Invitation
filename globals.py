import timer
# to keep timer in separate
import threading
import json
# to get terminal size
import shutil

# constants


class Room:
    """suppose to replace you_see and rooms"""

    def __init__(self, name, description, directions, items, map):
        self.name = name
        self.description = description  # suppose to replace you_see 
        self.directions = directions
        self.items = items
        self.map = map


def data_extractor():
    """extracts data from json file and turns em into python dict"""
    with open('rooms.json', 'r') as f:
        raw_data = f.read()
        data = json.loads(raw_data)
        return data


def rooms_populator(rooms_data):
    """populates rooms with room objects, shall I rename it?"""
    data = {}
    for key in rooms_data:
        data[key] = (Room(key, rooms_data[key]['description'], rooms_data[key]['directions'], rooms_data[key]['items'], rooms_data[key]['map']))
    return data


rooms_data = data_extractor()

rooms = rooms_populator(rooms_data)

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

current_room = rooms['inner dungeon']

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