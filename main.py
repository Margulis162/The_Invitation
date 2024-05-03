# +++imports+++

# needed for time limitation
import globals
import intro
import main_game_loop


def game_over():
    """just ascii message for game over scenario"""
    msg = (
        r"  __ _  __ _ _ __ ___   ___    _____   _____ _ __",
        r" / _` |/ _` | '_ ` _ \ / _ \ / _ \ \ / / _ \ '__|",
        r"| (_| | (_| | | | | | |  __/ | (_) \ V /  __/ |  ",
        r" \__, |\__,_|_| |_| |_|\___|  \___/ \_/ \___|_|  ",
        r"  __/ |                                          ",
        r" |___/                                           "
    )
    for i in msg:
        print(globals.text_format_cntr.format(margin="", text=i))
    print(globals.text_format_cntr.format(margin="", text=""))
    print(globals.text_format_cntr.format(margin="", text="the vampire has awaken"))


def win():
    """just ascii message for win scenario"""
    msg = (
        r"__   _______ _   _   _    _ _____ _   _   _",
        r"\ \ / /  _  | | | | | |  | |_   _| \ | | | |",
        r" \ V /| | | | | | | | |  | | | | |  \| | | |",
        r"  \ / | | | | | | | | |/\| | | | | . ` | | |",
        r"  | | \ \_/ / |_| | \  /\  /_| |_| |\  | |_|",
        r"  \_/  \___/ \___/   \/  \/ \___/\_| \_/ (_)"
    )
    for i in msg:
        print(globals.text_format_cntr.format(margin="", text=i))
    print(globals.text_format_cntr.format(margin="", text=""))
    print(globals.text_format_cntr.format(margin="", text="you have escaped!"))


def main():
    """ this function does everything and contains all the other functions."""

    # A sneaky way to call a function I found - from the condition. Somewhat useful.
    if intro.render():
        # renders while time is ticking
        globals.thread_timer.start()
        main_game_loop.flow()

        # prints the outcome of the game once time is up needs to be formatted
        # stops the timer
        win() if globals.victory else game_over()

    else:
        print(globals.text_format_cntr.format(margin='', text="Bye!"))


main()

"""
order is arbitrary
TODO:
1. done
2. make rendered screen a bit wider, add askii graphics for each room https://www.ascii-art-generator.org/
3. done 
4. add different text colors for readability
5. make class for rooms restructure data accordingly
6. implement final battle, more conditions a player meets (well-fed, energized, knows karate)
better the chances are. That if we feel like it.
7. I do not like the delay after a player tries to do something of limits like entering library without key.
Though I feel like it is needed right now. Perhaps, if we manage to use os to reprint the screen and we add different
colors to the screen we might be able to highlight the message somehow else?
8. ???

"""
