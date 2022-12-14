"""
This module contains event functions for level 3.
"""


import random
from fight import fight_sequence
from skeleton import validate_yes_no


def default(player_dict: dict) -> None:
    """
    Print a simple message.
    """
    print('''
    nothing here...
    ''')
    player_dict['useless_events'] += 1


def deer(player_dict: dict) -> None:
    """
    Execute fight_sequence with a deer.

    :param player_dict: dictionary containing player information
    :precondition: player_dict must be a dictionary
    :postcondition: executes fight_sequence with 'deer' as parameter

    Too difficult to test
    """
    print('''
    It's a deer! Just standing there.
    The deer doesn't know what's about to happen.
    Let's hurry up and kill it.
    ''')
    fight_sequence('deer', player_dict)


def berry(player_dict: dict) -> None:
    """
    Add 1 berry to player's inventory.

    :param player_dict: dictionary containing player information
    :precondition: player_dict must be a dictionary containing 'inventory' as key
    :precondition: player_dict['inventory'] must be a dictionary
    :postcondition: adds 1 berry to player_dict['inventory']
    """
    print('''
    You found a berry.
    1 berry has been added to your inventory.
    ''')
    if 'berry' in player_dict['inventory']:
        player_dict['inventory']['berry'] += 1
    else:
        player_dict['inventory']['berry'] = 1


def nut(player_dict: dict) -> None:
    """
    Add 1 hazelnut to player's inventory if player chooses to crack it.

    :param player_dict: dictionary containing player information
    :precondition: player_dict must be a dictionary containing 'xp' and 'inventory' as keys
    :precondition: player_dict['xp'] must be an integer and player_dict['inventory'] must be a dictionary
    :postcondition: increases player_dict['xp'] by 10 if player chooses to crack the nut
    :postcondition: adds 1 hazelnut to player_dict['inventory'] if player chooses to crack it
    """
    print('''
    You found a hazelnut. We love hazelnuts!
    ''')
    choice = validate_yes_no('    Crack the nut? (y/n)')
    if choice == 'y':
        print('''
    You cracked the nut. How fun and delicious!
    
    You gained 10 XP. 1 hazelnut has been added to your inventory.
    ''')
        player_dict['xp'] += 10
        if 'hazelnut' in player_dict['inventory']:
            player_dict['inventory']['hazelnut'] += 1
        else:
            player_dict['inventory']['hazelnut'] = 1
    elif choice == 'n':
        print('''
    You left the nut alone.
    Interesting choice.''')


def mushroom(player_dict: dict) -> None:
    """
    Lose or gain 5 hp if player chooses to eat the mushroom.

    :param player_dict: dictionary containing player information
    :precondition: player_dict must be a dictionary containing 'hp' as key
    :precondition: player_dict['hp'] must be an integer
    :postcondition: randomly increase or decrease player_dict['hp'] by 5 if player chooses to eat the mushroom
    """
    print('''
    You found a mushroom.''')
    choice = validate_yes_no('    Eat mushroom? (y/n)')
    if choice == 'y':
        rand = random.randint(1, 2)
        if rand == 1:
            print('''
    You ate the mushroom. Delicious!
    You gained 5 HP.
    ''')
            player_dict['hp'] = min(player_dict['hp'] + 5, player_dict['max_hp'])
        else:
            print('''
    You ate a POISONOUS mushroom. YUCK!
    You lose 5 HP.
    ''')
            player_dict['hp'] = max(player_dict['hp'] - 5, 1)

    elif choice == 'n':
        print('''
    You left the mushroom alone.''')


def main():
    """
    Drive the program
    """
    print('Please run game.py. This is a module.')


if __name__ == '__main__':
    main()
