import time
import render
import globals
import globals  # FIXME Remove this later this is for testing purposes


# Prints text input into a string dynamically on the terminal, one character at a time
# Can accept any input that can be converted to a string.
# Arguments:
# text (string-convertible)
# The string that will be printed to the terminal.
# Can accept non-string types as long as they can be converted to a string.

# print_delay (int) default value: 0.25
# used to establish the delay between each character in the text in seconds.

# char_end (string)
# allows a specific string of characters to be added after each character in the input string. Optional.

# *custom_delays (tuple(string, int))
# accepts an unlimited number of tuples containing a string and integer value.
# Used to set custom delays on specific characters, overriding the print delay.
# Example: ("!,?.", 1) will give any explanation points, question marks, commas or periods in the string a
# 1-second delay.

# def print_dynamic_text(text, print_delay=0.25, char_end="", *custom_delays):
#     for character in str(text):
#         print(character, end=char_end, flush=True)
#         # Check if the character needs to be delayed differently based on a custom delay. If not, use default timer.
#         for delayed_chars, delay_time in custom_delays:
#             # Check if any of the characters set for delay in the string match the current character
#             if character in delayed_chars:
#                 time.sleep(delay_time)
#                 break
#         else:
#             time.sleep(print_delay)


def print_dynamic_text_1_1(print_delay=0.02):
    # resets description on call 
    globals.description = [[''], [''], [''], ['']]
    # loops through description strings eventually will be moved to the room objects
    for i, text in enumerate(globals.rooms[globals.current_room].description[0] ):
        # slowly adds characters to the description variable and rerenders
        for character in text:
            globals.description[i].append(character)
            time.sleep(print_delay)
            render.screen()


# This is just an example you can use to understand how it works by running this module specifically
# if __name__ == "__main__":
#     dialogue = "The man walked over to the shop, pondering its contents.\n\"Egad!\" he stated oud loud.\n\n"

#     print_dynamic_text(globals.text_format_end.format(margin="", fill="#" * 30, text="'<.\\__/.>'"), 0.01,
#                        "", (" ", 0))  # FIXME Remove later

#     print_dynamic_text(globals.text_format_end.format(margin="", fill="#" * 30, text=" VwwwwV "), 0.01)
#     # FIXME Remove later

    # print_dynamic_text(dialogue, 0.04, "", ("!.?", 0.5), (",", 0.25))
    # print_dynamic_text(dialogue, 0.04, "")

    # input()
