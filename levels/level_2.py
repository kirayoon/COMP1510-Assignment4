import random


def check_event(board: dict, player_dict: dict):
    location = player_dict['location']
    event_dict = {'event1': default, 'event2': soup, 'event3': egg, 'event4': scraps}
    current_event = board[location]
    event_func = event_dict[current_event]
    event_func(player_dict)


def default(player_dict: dict):
    choice = random.randint(1, 2)
    if choice == 1:
        print('''
        
        ''')
    else:
        print('''
        
        ''')


def soup(player_dict: dict):
    print('''
    
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
