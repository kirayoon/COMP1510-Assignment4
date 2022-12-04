import random
from fight import fight_sequence
from skeleton import validate_yes_no


def default(player_dict: dict):
    print('''
    nothing here...
    ''')


def deer(player_dict: dict):
    print('''
    It's a deer! Just standing there.
    The deer doesn't know what's about to happen.
    Let's hurry up and kill it.
    ''')
    fight_sequence('deer', player_dict)


def berry(player_dict: dict):
    print('''
    You found a berry.
    1 berry has been added to your inventory.
    ''')
    if 'berry' in player_dict['inventory']:
        player_dict['inventory']['berry'] += 1
    else:
        player_dict['inventory']['berry'] = 1


def nut(player_dict: dict):
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


def mushroom(player_dict: dict):
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


def main():
    print('Please run game.py. This is a module.')


if __name__ == '__main__':
    main()
