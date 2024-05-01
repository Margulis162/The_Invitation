import globals


def screen():
    """prints the screen"""
    # screen separator for better readability
    print(globals.text_format_end.format(margin="", fill="#" * 30, text="'<.\\__/.>'"))
    print(globals.text_format_end.format(margin="", fill="#" * 30, text=" VwwwwV "))
    # upper bar with time left and current room
    print(globals.upper_bar.format(margin="", time=f"time before sunset {globals.time_left} min",
                                   room=f"You are in {globals.current_room.upper()}"))
    # separation line
    print(globals.text_format_lft.format(margin="", text="_" * 70))
    # status bar indicates progress and gives clues on what needs to be done
    print(globals.text_format_lft.format(margin="", text=globals.status))

    # prints inventory or its lack
    if len(globals.inventory) == 0:
        print(globals.text_format_lft.format(margin="", text=globals.no_items))
    else:
        print(globals.text_format_lft.format(margin="", text="You have: " + ', '.join(globals.inventory)))
    # separation line
    print(globals.text_format_lft.format(margin="", text="_" * 70))
    # room description, I loop through it since some are pretty lengthy, that helps to display it nice.
    for i in globals.you_see[globals.current_room]:
        print(globals.text_format_cntr.format(margin="", text=i))

    # separation line
    print(globals.text_format_lft.format(margin="", text="_" * 70))
    # instructions
    print(globals.text_format_lft.format(margin="", text=globals.general_instructions_move))
    print(globals.text_format_lft.format(margin="", text=globals.general_instructions_usage))
    # screen separator for better readability
    # separation line
    print(globals.text_format_lft.format(margin="", text="_" * 70))
