import globals
import time


def timer():
    """sets up timer for the game completion"""
    time_limit_min = globals.time_left
    # we are counting till the time expires aka equals to 0
    while time_limit_min > 0 and not globals.victory:
        # 60 seconds delay before a minute expires
        time.sleep(60)
        time_limit_min -= 1
        # updating global variable
        globals.time_left = time_limit_min
