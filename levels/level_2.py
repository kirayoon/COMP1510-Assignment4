import random

def intro_text():
    print('''
    You smell a whiff of something delicious.. You follow the smell until it leads you to a house.
    You knock on the door, but when no one answered, you decided to go inside.
    You 
    ''')


def default(player_dict: dict):
    print('''
    nothing here...
    ''')


def soup(player_dict: dict):
    print('''
    OH GOODY! SOUP! 
    ''')


def egg(player_dict: dict):
    print('''
    
    ''')


def scraps(player_dict: dict):
    choice = random.randint(1, 4)
    if choice == 1:
        print('''
        
        ''')
    elif choice == 2:
        print('''
        
        ''')
    elif choice == 3:
        print('''
        
        ''')
    else:
        print('''
        
        ''')


def level2():
    print('hello')
