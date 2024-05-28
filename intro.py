import globals
from render import clean_screen
from colorama import init, Fore, Back, Style

def establish_text_speed(speed_dictionary, text_orientation):
    # Get a list of all possible speeds
    possible_speeds = list(speed_dictionary.keys())

    print('\n' + Style.DIM + text_orientation.format(left='', center="What is your preferred typing speed? Possible types:", right='') + Style.RESET_ALL)

    # Receive user input for the desired text speed
    text_speed_input = (input(Style.DIM + text_orientation.format(left='', center=", ".join(possible_speeds) + "\n", right='') + Style.RESET_ALL )
                        .lower())

    # Loop until the player enters a proper typing speed
    while text_speed_input not in possible_speeds:
        print(Style.DIM + text_orientation.format(left='', center="Incorrect input. What is your preferred typing speed? "
                                                       "Possible types:\n",
                                                       right='') + Style.RESET_ALL)
        text_speed_input = input(Style.DIM + text_orientation.format(left='', center=", ".join(possible_speeds) + "\n",
                                                          right='' + Style.RESET_ALL)
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
        'You have been invited to a dinner party… ',
        'Unfortunately, the host is a bloody Vampire and you\'re the main course.',
        'Luckily, you arrived early and the master of the castle is still asleep.',
        'His henchman has locked you in the dungeon and is guarding the entrance into the castle.',
        '',
        'You have to hurry up and get out of the castle before the party starts...'

    )

    # logo print
    for i in intro_logo:
        print(Fore.RED + Style.BRIGHT + globals.main_str.format(left='', center=i, right='') + Fore.RESET + Style.RESET_ALL)

    # story print
    for i in intro_text:
        print(globals.main_str.format(left='', center=i, right=''))

  

 
    # variable indicates start of the game
    new_game = input('\n' + Style.DIM + globals.main_str.format(left='', center="Enter start or exit\n", right='') + Style.RESET_ALL).lower()
    

    # fancy while loop to check if the input is correct
    while new_game not in ('start', 'exit'):
        new_game = input('\n' + Style.DIM + globals.main_str.format(left='', center="Enter start or exit\n", right='') + Style.RESET_ALL).lower()
    # if game is initiated returns true to the condition statement from which the function is called
    if new_game == 'start':
        # Set the players desired text speed
        globals.selected_text_speed = globals.text_speeds[establish_text_speed(globals.text_speeds,
                                                                               globals.main_str)]

        return True


    else:
        return False
