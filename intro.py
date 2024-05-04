import globals
from render import clean_screen


def establish_text_speed(speed_dictionary, text_orientation):
    # Get a list of all possible speeds
    possible_speeds = list(speed_dictionary.keys())

    print(text_orientation.format(margin=' ', text="What is your preferred typing speed? Possible types:"))

    # Receive user input for the desired text speed
    text_speed_input = (input(text_orientation.format(margin=' ', text=", ".join(possible_speeds) + "\n"))
                        .lower())

    # Loop until the player enters a proper typing speed
    while text_speed_input not in possible_speeds:
        print(text_orientation.format(margin=' ', text="Incorrect input. What is your preferred typing speed? "
                                                       "Possible types:\n"))
        text_speed_input = (input(text_orientation.format(margin=' ', text=", ".join(possible_speeds) + "\n"))
                            .lower())

    return text_speed_input


def render():
    clean_screen()
    """code guilty of the title screen, it also passes integer to render function to set up the timer"""

    # format strings for introduction logo and story

    intro_logo = (
        r'_________   _                    _________  _________   _______   _________  _________   _______    _       ',
        r'\__   __/  ( (    /|  |\     /|  \__   __/  \__   __/  (  ___  )  \__   __/  \__   __/  (  ___  )  ( (    /|',
        r'   ) (     |  \  ( |  | )   ( |     ) (        ) (     | (   ) |     ) (        ) (     | (   ) |  |  \  ( |',
        r'   | |     |   \ | |  | |   | |     | |        | |     | (___) |     | |        | |     | |   | |  |   \ | |',
        r'   | |     | (\ \) |  ( (   ) )     | |        | |     |  ___  |     | |        | |     | |   | |  | (\ \) |',
        r'   | |     | | \   |   \ \_/ /      | |        | |     | (   ) |     | |        | |     | |   | |  | | \   |',
        r'___) (___  | )  \  |    \   /    ___) (___     | |     | )   ( |     | |     ___) (___  | (___) |  | )  \  |',
        r'\_______/  |/    )_)     \_/     \_______/     )_(     |/     \|     )_(     \_______/  (_______)  |/    )_)',
        '',
        '',
        '',
    )

    intro_text = (
        'You have been invited to a party… ',
        'It turned out to be a snack, because the host is a bloody Vampire.',
        'Luckily, you arrived early and the master of the castle is still asleep.',
        'His henchman locked you in the dungeon and is guarding the entrance into the castle.',
        'You are also too thin to be stopped by bars.',
        '',
        'Now you have to hurry up and get out of the castle, before the party starts...'

    )

    # logo print
    for i in intro_logo:
        print(globals.intro_format_str.format(margin=' ', text=i))

    # story print
    for i in intro_text:
        print(globals.intro_format_str.format(margin=' ', text=i))

    # variable indicates start of the game
    new_game = input(globals.intro_format_str.format(margin=' ', text="Enter start or exit\n")).lower()

    # fancy while loop to check if the input is correct
    while new_game not in ('start', 'exit'):
        new_game = input(globals.intro_format_str.format(margin=' ', text="Enter start or exit\n")).lower()
        print(new_game)
    # if game is initiated returns true to the condition statement from which the function is called
    if new_game == 'start':
        # Set the players desired text speed
        globals.selected_text_speed = globals.text_speeds[establish_text_speed(globals.text_speeds,
                                                                               globals.intro_format_str)]

        return True


    else:
        return False
