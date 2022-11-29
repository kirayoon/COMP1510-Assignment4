import json
import random
from typing import Callable


# 10, 5, 3, 2,


def check_event(board: dict, player_dict: dict):
    location = player_dict['location']
    event_dict = {'event1': default, 'event2': fish, 'event3': slippery_rock, 'event4': heavy_current}
    current_event = board[location]
    event_func = event_dict[current_event]
    event_func(player_dict)



