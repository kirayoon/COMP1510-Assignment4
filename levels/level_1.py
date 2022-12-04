"""
This module contains event functions for level 1.
"""


import random
from fight import fight_sequence


def default(player_dict: dict) -> None:
    """
    Print a random message and add 1 water to the player's inventory.

    :param player_dict: dictionary containing player's stats
    :precondition: player_dict must be a dictionary containing 'inventory' as key
    :precondition: player_dict['inventory'] must be a dictionary
    :postcondition: prints a random message to screen
    :postcondition: adds 'water' to player_dict['inventory']
    """
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
    print('1 water has been added to your inventory')
    if 'water' in player_dict['inventory']:
        player_dict['inventory']['water'] += 1
    else:
        player_dict['inventory']['water'] = 1


def slippery_rock(player_dict: dict) -> None:
    """
    Remove 1 hp from player's hp.

    :param player_dict: dictionary containing player's stats
    :precondition: player_dict must be a dictionary containing 'hp' as key
    :precondition: player_dict['hp'] must be an integer
    :postcondition: removes 1 hp from player_dict['hp']
    """
    print('''
    WoooaaaaAAAAHHH!
    You slipped on a rock and fell. 
    You bruised your arm. How unfortunate :(
    
    You lost 1 hp
    ''')
    player_dict['hp'] -= 1


def heavy_current(player_dict: dict) -> None:
    """
    Print a simple message.
    """
    print('''
    You're in a heavy current.''')


def fish(player_dict: dict):
    """
    Execute fight_sequence with a fish.

    :param player_dict: dictionary containing player's stats
    :precondition: player_dict must be a dictionary
    :postcondition: executes fight_sequence with 'fish' as parameter
    """
    print('''
    Splish splash a salmon jumps out and slaps you in the face.
    You better show it who's boss.
    ''')
    fight_sequence('fish', player_dict)


def main():
    print('Please run game.py. This is a module.')


if __name__ == '__main__':
    main()
