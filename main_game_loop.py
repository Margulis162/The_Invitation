import globals
import time
import render
from dynamic_typing_func import print_dynamic_text_1_1 as dynamic


def take_command():
    """take the user input, since we do it a lot it makes sense to have a function for it"""
    print('\033[?25h', end="")  # makes hidden cursor visible
    globals.command = input(globals.main_str.format(left="", center="Enter a command: \n", right="")).lower().strip()
    return globals.command


def input_validation(command):
    """checks if input is valid"""
    while (command not in globals.all_commands['moves']) and (command not in globals.all_commands['items']):
        print(globals.main_str.format(left="", center="The command is unrecognized.", right=""))
        command = take_command()


def movement():
    """takes care of switching rooms"""

    # handles the case when room has no door in that direction
    while globals.command not in list(globals.current_room.directions.keys()):
        print(globals.main_str.format(left="", center="you can't walk through walls yet...", right=''))
        take_command()

    # handles normal cases of movement
    if globals.current_room.name != 'laboratory':
        # Changes the current room to the adjacent room based on user command
        globals.current_room = globals.rooms[globals.current_room.directions[globals.command]]
        flow()

    # handles the special case of the library door being locked
    elif globals.current_room.name == 'laboratory':
        if globals.command == 'east':
            if 'key' in globals.inventory:
                globals.current_room = globals.rooms['library']
                flow()
            else:
                print(globals.main_str.format(left="", center="The door to the library is locked.", right=""))
                time.sleep(2)
                flow()
        else:
            globals.current_room = globals.rooms[globals.current_room.directions[globals.command]]
            flow()


def items_interactions():  # FIXME You will have to rework any parts of this function that call the rooms for data. Use the way I called the rooms in the movement function to guide you.
    # energy drink interaction
    # picks up a drink and updates status if conditions are met
    if globals.command == 'take the drink':
        if globals.current_room.name == 'outer dungeon' and 'gloves' in globals.inventory:
            globals.status = globals.status.replace("low on energy", "energized")
            globals.rooms[globals.current_room.name].description = [
                "There is a skeleton.",
                "You can go WEST and NORTH from here."
            ]
            flow()
        # prints a message if the room is not right
        elif globals.current_room.name != 'outer dungeon':
            print(globals.main_str.format(left="", center="There are no energy drinks here...", right=""))
            time.sleep(2)
            flow()
        # prints a message if gloves are not in inventory
        else:
            print(globals.main_str.format(left="", center="I'm not touching it barehanded...", right=""))
            time.sleep(2)
            flow()

    # key interaction
    if globals.command == 'take the key':
        # takes key updates room description and inventory
        if globals.current_room.name == 'bed chambers' and 'key' not in globals.inventory:
            globals.inventory.append('key')
            print(globals.current_room.description )
            globals.rooms[globals.current_room.name].description = [
                "The room is pretty much empty, except for the fancy coffin in the very center.",
                "The lid is closed for now.",
                "After closer inspection, You do not see anything useful.",
                "You can only go WEST from here."
            ]
            flow()

        # print error message if key not there
        elif globals.current_room.name != 'bed chambers' and 'key' not in globals.inventory:
            print(globals.main_str.format(left="", center="There is no key...", right=""))
            time.sleep(2)
            flow()

        # prints error if key is already in inventory
        else:
            print(globals.main_str.format(left="", center="You have it already...", right=''))
            time.sleep(2)
            flow()

    # gloves interactions
    if globals.command == 'take the gloves':
        # picks up gloves when condition is met
        if globals.current_room.name == 'laboratory' and 'gloves' not in globals.inventory:
            globals.inventory.append('gloves')
            globals.rooms[globals.current_room.name].description = [
                "That is where the undead do their unholy research.",
                "Walls are covered with jars, containing some weird creatures.",
                "Some of them are staring at you.",
                "You can only go EAST and SOUTH."
            ]
            flow()

        # error on attempt to pick up gloves in a wrong room
        elif globals.current_room.name != 'laboratory' and 'gloves' not in globals.inventory:
            print(globals.main_str.format(left="", center="There are no gloves...", right=""))
            time.sleep(2)
            flow()

        # error when you already have gloves
        else:
            print(globals.main_str.format(left="", center="You have them already...", right=""))
            time.sleep(2)
            flow()

    # pizza slice interaction
    if globals.command == 'take a slice':
        # picks up slice when condition is met
        if globals.current_room.name == 'the great hall' and 'hungry' in globals.status:
            # replace substr in status
            globals.status = globals.status.replace('hungry', 'well-fed')
            # update room description
            globals.rooms[globals.current_room.name].description = [
                "That's likely where the 'party' is suppose to be held.",
                "The hall is huge and not well maintained. Dust, spiderweb, and blood stains are everywhere.",
                "You see a pizza box in the corner. But you are not hungry.",
                "You can go EAST and NORTH from here."
            ]
            flow()
        # error when you already ate
        else:
            print(globals.main_str.format(left="", center="What?", right=""))
            time.sleep(2)
            flow()
    # karate guide interaction
    else:
        if globals.current_room.name == 'library' and globals.status.find("do not know how to fight"):
            # replace substr in status
            globals.status = globals.status.replace("have no way to defend yourself",
                                                    "know few karate kicks")
            flow()
            # takes care of different scenarios
        if not globals.victory and globals.time_left > 0:
            time.sleep(2)
            flow()


def flow():
    """Updates the screen with current info"""

    # checks if there still time left
    while globals.time_left != 0:

        # prints the screen
        dynamic(globals.selected_text_speed)

        # entrance is the villain room it has special handling
        if globals.current_room.name != 'entrance':
            take_command()

            # checks if command is unknown.
            input_validation(globals.command)

            # this portion is responsible for movement
            if globals.command in globals.all_commands['moves']:
                movement()

            # this portion is responsible for item interactions
            if globals.command in globals.all_commands['items']:
                items_interactions()

        # takes care of win by setting up timer to 0 and the globals.victory to true
        elif globals.status == 'You are well-fed, energized, and know few karate kicks':
            globals.victory = True
            globals.time_left = 0
            flow()
            # takes care of the penalty for entering the villain room
        else:
            # time penalty for visiting vilain room
            time.sleep(10)
            # go back to main hallway
            globals.current_room = globals.rooms['main hallway']
            flow()
