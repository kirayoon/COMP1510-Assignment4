"""
This module contains event functions for level 2.
"""


import random
import time
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


def soup(player_dict: dict) -> None:
    """
    Gain 200 XP for each soup found, and execute fight_sequence if third soup is found.

    Use the player_dict['soup_counter'] to keep track of how many soups have been found.

    :param player_dict: dictionary containing player information
    :precondition: player_dict must be a dictionary containing 'xp' as key
    :precondition: player_dict['xp'] must be an integer
    :postcondition: increases player_dict['xp'] by 200 for each soup found
    :postcondition: executes fight_sequence with 'papa' as parameter if third soup is found
    """
    num_soup = player_dict['soup_counter']

    print('''
    OHH GOODY! SOUP!
        ''')
    time.sleep(1)

    if num_soup == 0:
        print('''
    You taste the soup and it's TOO SPICY!
    
        You gain 150 XP! But you still need to find the perfect soup...
        ''')
        player_dict['xp'] += 200

    elif num_soup == 1:
        print('''
    You taste the soup and it's TOO SWEET!??!
    
        You gain 150 XP! But you still need to find the perfect soup...
        ''')
        player_dict['xp'] += 200

    elif num_soup == 2:
        print('''
    You taste the soup and it's...
    
        PERFECT!
    
        You drink the entire bowl. You gain 300 XP!
        ''')
        player_dict['xp'] += 300
        print('...')
        time.sleep(3)
        print('''
        
            The door swings wide open. The Lobs are here!''')
        time.sleep(2)
        print('''
            They see the house in shambles and the soup bowl empty.''')
        time.sleep(2)
        print('''
            Papa Lob yells, "You're not going anywhere, Bear!"
            ''')
        input('Press enter to continue...')
        fight_sequence('papa', player_dict)
    player_dict['soup_counter'] += 1


def scraps(player_dict: dict) -> None:
    """
    Execute random events.

    Random events can result in gain or loss in hp or xp, or add items to inventory.

    :param player_dict: dictionary containing player information
    :precondition: player_dict must be a dictionary containing 'hp', 'xp', and 'inventory' as keys
    :postcondition: executes random events based on random number
    """
    rand = random.randint(1, 4)
    if rand == 1:
        print('''
        *crunch* *squish*
        You stepped on a rat...
        ''')
        choice = validate_yes_no('''
        Eat the rat? (y/n)''')
        if choice == 'y':
            print('''
            yummy.. You gained 5 HP & 10 XP!''')
            player_dict['hp'] = min(player_dict['hp'] + 5, player_dict['max_hp'])
            player_dict['xp'] += 10
        elif choice == 'n':
            print('''
            You left the dead rat alone.''')

    elif rand == 2:
        print('''
        WoooaaaaAAAAHHH!
        You slipped on a banana peel and fell on your face. 
        You have a nosebleed. boohoo :(
    
        You lost 2 HP & gained 10 XP
        ''')
        player_dict['hp'] = max(player_dict['hp'] - 2, 1)
        player_dict['xp'] += 10

    elif rand == 3:
        print('''
        You found a jar of honey!
        ''')
        choice = validate_yes_no('''
        Steal the honey? (y/n)''')
        if choice == 'y':
            if 'honey' in player_dict['inventory']:
                player_dict['inventory']['honey'] += 1
            else:
                player_dict['inventory']['honey'] = 1
            print('''
            1 honey has been added to your inventory''')
        elif choice == 'n':
            print('''
            You left the honey alone.
            What an ethical choice!
            
            You gained 10 XP!
            ''')
            player_dict['xp'] += 10

    else:
        print('''
        OUCH! 
        You stepped on a nail!
        
        You lost 3 hp
        ''')
        player_dict['hp'] = max(player_dict['hp'] - 3, 1)


def chair(player_dict: dict) -> None:
    """
    Execute chair events based on how many chairs have been found.

    Use the player_dict['chair_counter'] to keep track of how many chairs have been found.

    :param player_dict: dictionary containing player information
    :precondition: player_dict must be a dictionary containing 'hp' and 'xp' as keys
    :postcondition: executes events based on how many chairs have been found
    :postcondition: chair events can result in gain or loss in hp or xp
    """
    num_chair = player_dict['chair_counter']

    print('''
    You found a chair!
    ''')

    if num_chair == 0:
        print('''
        You sit on the chair and it's TOO STINKY!??!
        ''')
        time.sleep(1)
        print('''
        Yuck.

        You lose 5 HP. But you gain 5 XP for trying.''')
        player_dict['hp'] = max(player_dict['hp'] - 5, 1)
        player_dict['xp'] += 5

    elif num_chair == 1:
        print('''
        You sit on the chair and it's TOO SMALL!

        Uh oh. You're stuck!
        ''')
        time.sleep(1)
        print('''
        still stuck..''')
        time.sleep(1)
        print('''
        POP! You're free!

        But what a waste of time. You lost 5 XP.''')
        player_dict['xp'] -= 5

    elif num_chair == 2:
        print('''
        You sit on the chair and it's...
        ''')
        time.sleep(1)
        print('''
        PERFECT!''')
        time.sleep(1)
        print('''
    
        But it shatters into pieces... bad bear.
    
        You gain 10 XP & 10 HP.
        ''')
        player_dict['xp'] += 10
        player_dict['hp'] = min(player_dict['hp'] + 10, player_dict['max_hp'])
    player_dict['chair_counter'] += 1


def main():
    """
    Drive the program
    """
    print('Please run game.py. This is a module.')


if __name__ == '__main__':
    main()
