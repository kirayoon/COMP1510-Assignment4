import json
import random
import time

import main


# 10, 5, 3, 2,


def default(player_dict: dict):
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


def slippery_rock(player_dict: dict):
    print('''
    WoooaaaaAAAAHHH!
    You slipped on a rock and fell. 
    You bruised your arm. How unfortunate :(
    
    You lost 1 hp
    ''')
    player_dict['hp'] -= 1


def heavy_current(player_dict: dict):
    print('''
    You're in a heavy current.
    ''')


def fish(player_dict: dict):
    print('''
    Splish splash a salmon jumps out and slaps you in the face.
    You better show it who's boss.
    ''')
    fight_sequence('fish', player_dict)


def fight_sequence(enemy: str, player_dict: dict):
    # fight code here
    # code to read json file
    # with open('enemy.json') as f:
    #     enemy_dict = json.load(f)

    # for testing
    with open('..\\enemy.json') as f:
        enemy_json = json.load(f)
    enemy_dict = enemy_json[enemy]
    print(enemy_dict)

def convert_health_to_bars(health: int, max_health: int) -> tuple[str, str]:
    health_bar_size = 20
    health_per_dash = int(max_health / health_bar_size)
    current_health_dashes = int(health / health_per_dash)
    lost_health = health_bar_size - current_health_dashes
    health_percentage = str(int(health / max_health * 100)) + '%'
    health_bar = '█' * current_health_dashes + ' ' * lost_health
    return health_bar, health_percentage


def print_health(player_dict: dict, enemy_dict: dict):
    player_health_bar, player_health_percentage = convert_health_to_bars(player_dict['hp'], player_dict['max_hp'])
    enemy_health_bar, enemy_health_percentage = convert_health_to_bars(enemy_dict['hp'], enemy_dict['max_hp'])

    print(f'{player_dict["name"]:^22} {enemy_dict["name"]:^41}')
    print('|' + player_health_bar + '|' + ' ' * 10 + '|' + enemy_health_bar + '|')
    print(f'{player_health_percentage:^22} {enemy_health_percentage:^40}')

