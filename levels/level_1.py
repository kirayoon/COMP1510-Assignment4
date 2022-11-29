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


def default(player_dict: dict):
    choice = random.randint(1, 2)
    if choice == 1:
        print('''
        You're in the middle of a river.
        There's water rushing all around you. 
        The rocks are slippery! Don't fall!
        ''')
    else:
        print('''
        Water rushes all around you.
        You see fish jumping in the distance.
        Your tummy rumbles.
        ''')
    if 'water' in player_dict['inventory']:
        player_dict['inventory']['water'] += 1
    else:
        player_dict['inventory']['water'] = 1


def slippery_rock(player_dict: dict):
    print('''
    You're on a slippery rock.
    ''')


def heavy_current(player_dict: dict):
    print('''
    You're in a heavy current.
    ''')


def fish(player_dict: dict):
    print('''
    Splish splash a salmon jumps out and slaps you in the face.
    You better show it who's boss.
    ''')
    fight('fish')


def fight(enemy: str, player_dict: dict):
    # fight code here
    # code to read json file
    with open('enemy.json') as f:
        enemy_dict = json.load(f)
        print(enemy_dict)

    return True
