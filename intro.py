def render():
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
        print(intro_format_str.format(margin=' ', text=i))

    # story print
    for i in intro_text:
        print(intro_format_str.format(margin=' ', text=i))

    # variable indicates start of the game
    new_game = input(intro_format_str.format(margin=' ', text="Enter start or exit\n")).lower()

    # fancy while loop to check if the input is correct
    while new_game not in ('start', 'exit'):
        new_game = input(intro_format_str.format(margin=' ', text="Enter start or exit\n")).lower()
        print(new_game)
    # if game is initiated returns true to the condition statement from which the function is called
    if new_game == 'start':
        return True
    else:
        return False


intro_format_str = '{margin:10}{text:^100}{margin:10}'
