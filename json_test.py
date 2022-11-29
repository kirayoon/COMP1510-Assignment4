import json


def fish(player_dict: dict):
    print('''
    Splish splash a salmon jumps out and slaps you in the face.
    You better show it who's boss.
    ''')
    fight('fish', player_dict)


def fight(enemy: str, player_dict: dict):
    # fight code here
    # code to read json file
    with open('enemy.json') as f:
        enemy_dict = json.load(f)
        print(enemy_dict['dog']['name'])

    return True


player_dict = {'name': 'player'}
fish(player_dict)
