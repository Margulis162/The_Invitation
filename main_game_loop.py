import globals
import time
import render


def take_command():
    globals.command = input(globals.text_format_cntr.format(margin="" * 25, text="Enter a command: \n")).lower().strip()
    return globals.command


def flow():
    """Updates the screen with current info"""

    # TODO: break movement and item interactions into different func for clarity
    while globals.time_left != 0:
        # prints the screen
        render.screen()
        ''' entrance is the villain room, so it is special  this code is responsible for the flow
        while not in the villain room, as for right now for the movement mainly'''
        if globals.current_room[0] != 'entrance':

            take_command()
            # checks if command is unknown. I know there is a less ugly way to check it using 'any',
            # but I need to  learn it first.
            while ((globals.command not in globals.all_commands[0]) and (globals.command not in globals.all_commands[1])
                   and globals.command != "help"):
                print(globals.text_format_cntr.format(margin="", text="The command is unrecognized."
                                                                      " Enter HELP to see the instructions."))
                take_command()

            # this portion is responsible for movement
            if globals.command in globals.all_commands[0]:

                # handles the case when command is legit but the room does not have the direction
                while globals.command not in globals.rooms[globals.current_room[0]][0]:
                    print(globals.text_format_cntr.format(margin="", text="you can't walk through walls yet..."))
                    take_command()

                # handles normal cases of movement
                if globals.current_room[0] != 'laboratory':
                    globals.current_room[0] = globals.rooms[globals.current_room[0]][0].get(globals.command)
                    flow()

                # handles the special case of the library door being locked
                elif globals.current_room[0] == 'laboratory':
                    if globals.command == 'east':
                        if 'key' in globals.inventory:
                            globals.current_room[0] = globals.rooms[globals.current_room[0]][0].get(globals.command)
                            flow()
                        else:
                            print(globals.text_format_cntr.format(margin="", text="The door to the library is locked."))
                            time.sleep(2)
                            flow()
                    else:
                        globals.current_room[0] = globals.rooms[globals.current_room[0]][0].get(globals.command)
                        flow()
            # this portion is responsible for item interactions
            if globals.command in globals.all_commands[1]:
                # energy drink interaction
                # picks up a drink and updates status if conditions are met
                if globals.command == 'take the drink':
                    if globals.current_room[0] == 'outer dungeon' and 'gloves' in globals.inventory:
                        globals.status = globals.status.replace("low energy", "energized")
                        globals.you_see['outer dungeon'] = [
                            "There is a skeleton.",
                            "You can go WEST and NORTH from here."
                        ]
                        flow()
                    # prints a message if the room is not right
                    elif globals.current_room[0] != 'outer dungeon':
                        print(globals.text_format_cntr.format(margin="", text="There is no energy drinks here..."))
                        time.sleep(2)
                        flow()
                    # prints a message if gloves are not in inventory
                    else:
                        print(globals.text_format_cntr.format(margin="", text="I'm not touching it barehanded..."))
                        time.sleep(2)
                        flow()
                # key interaction
                if globals.command == 'take the key':
                    # takes key updates room description and inventory
                    if globals.current_room[0] == 'bed chambers' and 'key' not in globals.inventory:
                        globals.inventory.append('key')
                        globals.you_see['bed chambers'] = [
                            "The room is pretty much empty,",
                            "except for the fancy coffin in the very center.",
                            "The lid is closed for now.",
                            "After closer inspection,",
                            "You do not see anything useful.",
                            "You can only go WEST from here."
                        ]
                        flow()

                    # print error message if key not there
                    elif globals.current_room != 'bed chambers' and 'key' not in globals.inventory:
                        print(globals.text_format_cntr.format(margin="", text="There is no key..."))
                        time.sleep(2)
                        flow()

                    # prints error if key is already in inventory
                    else:
                        print(globals.text_format_cntr.format(margin="", text="You have it already..."))
                        time.sleep(2)
                        flow()

                # gloves interactions
                if globals.command == 'take the gloves':
                    # picks up gloves when condition is met
                    if globals.current_room[0] == 'laboratory' and 'gloves' not in globals.inventory:
                        globals.inventory.append('gloves')
                        globals.you_see['laboratory'] = [
                            "That is where the undead do their unholy research.",
                            "Walls are covered with jars,",
                            "containing some weird creatures.",
                            "Some of them are staring at you.",
                            "You can only go EAST and SOUTH."
                        ]
                        flow()

                    # error on attempt to pick up gloves in a wrong room
                    elif globals.current_room != 'laboratory' and 'gloves' not in globals.inventory:
                        print(globals.text_format_cntr.format(margin="", text="There are no gloves..."))
                        time.sleep(2)
                        flow()

                    # error when you already have gloves
                    else:
                        print(globals.text_format_cntr.format(margin="", text="You have them already..."))
                        time.sleep(2)
                        flow()

                if globals.command == 'take a slice':
                    # picks up slice when condition is met
                    if globals.current_room[0] == 'the great hall' and globals.status.find('hungry'):
                        # replace substr in status
                        globals.status = globals.status.replace('hungry', 'well-fed')
                        # update room description
                        globals.you_see['the great hall'] = [
                            "That's likely where the 'party' is suppose to be held.",
                            "The hall is huge and not well maintained.",
                            "Dust, spiderweb, and blood stains are everywhere.",
                            "You see a pizza box in the corner.",
                            "But you are not hungry.",
                            "You can go EAST and NORTH from here."
                        ]
                        flow()
                    # error when you already ate
                    else:
                        print(globals.text_format_cntr.format(margin="", text="What?"))
                        time.sleep(2)
                        flow()
                # karate guide interaction
                else:
                    if globals.current_room[0] == 'library' and globals.status.find("do not know how to fight"):
                        # replace substr in status
                        globals.status = globals.status.replace("absolutely do not know how to fight",
                                                                "know few karate kicks")
                        flow()
                        # takes care of different scenarios
                    if not globals.victory and globals.time_left > 0:
                        print(globals.text_format_cntr.format(margin="", text="what?1"))
                        time.sleep(2)
                        flow()

            # this is here to satisfy the assignment objectives, I do print instructions every render anyway
            if globals.command in globals.all_commands[2]:
                # instructions
                print(globals.text_format_lft.format(margin="", text=globals.general_instructions_move))
                print(globals.text_format_lft.format(margin="", text=globals.general_instructions_usage))
                time.sleep(6)
                flow()

            # conditions for interaction with items

        # takes care of win by setting up timer to 0 and the globals.victory to true
        elif globals.status == 'You are well-fed, energized, and know few karate kicks':
            globals.victory = True
            globals.time_left = 0
            flow()
            # takes care of the penalty for entering the villain room
        else:
            # time penalty for visiting civilian room
            time.sleep(10)
            # go back to main hallway
            globals.current_room[0] = 'main hallway'
            flow()
