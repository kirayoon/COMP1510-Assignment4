import random


def default():
    print('''
    nothing here...
    ''')


def soup(player_dict: dict):
    print('''
    OH GOODY! SOUP!
    ''')


def scraps(player_dict: dict):
    rand = random.randint(1, 2)
    if rand == 1:
        print('''
        *crunch* *squish*
        You stepped on a rat...
        ''')
        choice = input("Eat the rat? (y/n)")
        if choice == 'y':
            print('yummy.. You gained 5 HP & 10 XP!')
            player_dict['hp'] += 5
            player_dict['xp'] += 10
        elif choice == 'n':
            pass
        else:
            print('Invalid input. Enter y or n')

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
        choice = input("Steal the honey? (y/n)")
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
            print('Invalid input. Enter y or n')

    else:
        print('''
        OUCH! 
        You stepped on a nail!
        
        You lost 3 hp
        ''')
        player_dict['hp'] -= 3
