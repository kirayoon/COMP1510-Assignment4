import json
import random
import time
from fight import fight_sequence
from skeleton import validate_yes_no


soup_counter = 0
chair_counter = 0


def default(player_dict: dict):
    print('''
    nothing here...
    ''')


def soup(player_dict: dict):
    global soup_counter

    print('''
    OHH GOODY! SOUP!
        ''')
    time.sleep(1)

    if soup_counter == 0:
        print('''
    You taste the soup and it's TOO SPICY!
    
    You gain 150 XP! But you still need to find the perfect soup...
        ''')
        player_dict['xp'] += 200

    elif soup_counter == 1:
        print('''
    You taste the soup and it's TOO SWEET!??!
    
    You gain 150 XP! But you still need to find the perfect soup...
        ''')
        player_dict['xp'] += 200

    elif soup_counter == 2:
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
        fight_sequence('papa', player_dict)
    soup_counter += 1


def scraps(player_dict: dict):
    rand = random.randint(1, 4)
    if rand == 1:
        print('''
        *crunch* *squish*
        You stepped on a rat...
        ''')
        choice = validate_yes_no("Eat the rat? (y/n)")
        if choice == 'y':
            print('yummy.. You gained 5 HP & 10 XP!')
            player_dict['hp'] += 5
            player_dict['xp'] += 10
        elif choice == 'n':
            print('''
        You left the dead rat alone.''')

    elif rand == 2:
        print('''
        WoooaaaaAAAAHHH!
        You slipped on a banana peel and fell on your face. 
        You have a nosebleed. boohoo :(
    
        You lost 1 HP & gained 10 XP
        ''')
        player_dict['hp'] -= 5
        player_dict['xp'] += 10

    elif rand == 3:
        print('''
        You found a jar of honey!
        ''')
        choice = validate_yes_no("Steal the honey? (y/n)")
        if choice == 'y':
            if 'honey' in player_dict['inventory']:
                player_dict['inventory']['honey'] += 1
            else:
                player_dict['inventory']['honey'] = 1
            print('1 honey has been added to your inventory')
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
        player_dict['hp'] -= 3


def chair(player_dict: dict):
    global chair_counter

    print('''
    You found a chair!
    ''')

    if chair_counter == 0:
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

    elif chair_counter == 1:
        print('''
        You sit on the chair and it's TOO STINKY!??!
        ''')
        time.sleep(1)
        print('''
        Yuck.
    
        You lose 5 HP.''')

        player_dict['hp'] -= 5

    elif chair_counter == 2:
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
        player_dict['hp'] += 10
    chair_counter += 1
