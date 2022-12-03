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
            print('yummy.. You gained 1 HP!')
            player_dict['hp'] += 1
        elif choice == 'n':
            pass
        else:
            print('Invalid input. Enter y or n')
    elif rand == 2:
        print('''
        WoooaaaaAAAAHHH!
        You slipped on a banana peel and fell on your face. 
        You have a nosebleed. boohoo :(
    
        You lost 1 hp
        ''')
        player_dict['hp'] -= 1
    elif rand == 3:
        print('''
        You found a jar of honey!
        ''')
        choice = input("Eat the honey? (y/n)")
        if choice == 'y':
            print('yummy.. You gained 1 HP!')
            player_dict['hp'] += 1
        elif choice == 'n':
            pass
        else:
            print('Invalid input. Enter y or n')
    else:
        print('''
        OUCH! 
        You stepped on a nail!
        
        You lost 1 hp
        ''')
        player_dict['hp'] -= 1
