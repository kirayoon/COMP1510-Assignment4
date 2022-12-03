import random
import json
import time


def default(player_dict: dict):
    print('''
    nothing here...
    ''')


def mushroom(player_dict: dict):
    print('''
    You found a mushroom.''')
    choice = input('    Eat mushroom? (y/n)')
    if choice == 'y':
        rand = random.randint(1, 2)
        if rand == 1:
            print('''
    You ate the mushroom. Delicious!
    You gained 5 HP.
    ''')
            player_dict['hp'] += 5
        else:
            print('''
    You ate a POISONOUS mushroom. YUCK!
    You lose 5 HP.
    ''')
            player_dict['hp'] -= 5

    elif choice == 'n':
        print('''
    You left the mushroom alone.''')
    else:
        print('Invalid input. Enter y or n')


def berry(player_dict: dict):
    pass


def nut(player_dict: dict):
    pass


def deer(player_dict: dict):
    pass
