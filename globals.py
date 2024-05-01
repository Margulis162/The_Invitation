import timer
import threading

# constants

# format strings
text_format_lft = '{margin:25}{text:<70}{margin:25}'
text_format_cntr = '{margin:25}{text:^70}{margin:25}'
text_format_end = '{margin:25}{fill:30}{text:^10}{fill:30}{margin:25}'
upper_bar = '{margin:25}{time:<35}{room:>35}'
intro_format_str = '{margin:10}{text:^100}{margin:10}'

general_instructions_move = r'type a direction to move. Example: "west"'
general_instructions_usage = r'type "take a/the" + "item name" to grab an item. Example: "take gloves"'

# for checking for unknown command
all_commands = [
    ('east', 'west', 'north', 'south'),
    ('take the key', 'take the gloves', 'take the karate guide', 'take the drink', 'take a slice'),
    'help'
]

# variables

victory = False

# status is also a condition for victory
status = 'You are hungry, low energy, and absolutely do not know how to fight'

# end game status for debugging
# status = 'You are well-fed, energized, and know few karate kicks'

time_left = 5  # this one is adjusted to allow more or less time for completion

current_room = ['inner dungeon']

# if inventory is empty
no_items = 'You are empty handed'

inventory = []

command = ""

# starts timer in a separate thread
thread_timer = threading.Thread(target=timer.timer)

you_see = {
    'inner dungeon': [
        "The bars of your cage are ridiculously far apart,",
        "it won't be a problem to squeeze out.",
        "There is also a door on the SOUTH wall."  # can be factored out in the future.
    ],
    'outer dungeon': [
        "There is a skeleton. It has energy drink in  it's hands.",
        "If only you would have GLOVES to TAKE THE DRINK",
        "You can go WEST and NORTH from here."
    ],
    'main hallway': [
        "Nothing to watch here except macabre paintings.",
        "You do not have time for this.",
        "You can go all directions from here."
    ],
    'the great hall': [
        "That's likely where the 'party' is suppose to be held.",
        "The hall is huge and not well maintained.",
        "Dust, spiderweb, and blood stains are everywhere.",
        "You see a pizza box in the corner.",
        "You are hungry, so take a TAKE A SLICE.",
        "You can go EAST and NORTH from here."
    ],
    'bed chambers': [
        "The room is pretty much empty,",
        "except for the fancy coffin in the very center.",
        "The lid is closed for now.",
        "After closer inspection,",
        "you see a KEY laying nearby the coffin.",
        "You can only go WEST from here."
    ],
    'laboratory': [
        "That is where the undead do their unholy research.",
        "Walls are covered with jars,",
        "containing some wierd creatures.",
        "Some of them are staring at you.",
        "THE GLOVES!",
        "You can only go EAST and SOUTH."
    ],
    'library': [
        "Endless rows of books.",
        "You are only interested in that KARATE GUIDE.",
        "You can only go WEST from here."
    ],
    'entrance': [
        "Escape is here!",
        "The doors shut behind you."
        "The henchman is guarding the exit,",
        "and you are not ready to take on him.",
        "He grins at you, and you go back slowly.",
        "The doors are supper heavy",
        "It takes you quite a few seconds to open them.",
        "You lost precious time.",
        "YES, THERE IS A TIME PENALTY FOR THIS ROOM!"
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
