import json
import random
import time

import skeleton


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

    #  Select the right enemy
    enemy_attack = enemy_dict['attack']
    enemy_hp = enemy_dict['max_hp']
    xp_gain = enemy_dict['xp_gain']
    #
    # print(enemy_hp, enemy_attack, xp_gain)
    # while enemy_hp > 0:
    #     print from
    time.sleep(1)
    print(f'{"FIGHT!":^56}')
    while enemy_hp > 0 and player_dict['hp'] > 0:
        # 1. print ascii image from file

        # 2. print health bars
        print_health(player_dict, enemy_dict)

        # 3. print attack options
        player_attacks = {'claw': 'claw', 'bite': 'bite', 'charge': 'charge', 'inventory': 'inventory'}
        print_attack_menu(player_attacks)
        move = get_player_choice(player_attacks)

        min_roll = max(1, player_dict['attack'] - 10)
        enemy_min_roll = max(1, enemy_attack - 10)
        if move == 'inventory':
            # TODO: remove main from here
            main.show_inventory(player_dict)
            continue
        elif move == 'charge':
            player_damage = 2 * player_dict['attack']
            enemy_hp -= player_damage
            self_damage = random.randint(min_roll, player_dict['attack'])
            player_dict['hp'] -= self_damage

            print(f'''
            You feel your power increasing!
            You rush at the enemy and do {player_damage} damage!
            
            However, in your rage, you also did {self_damage} damage to yourself.
            ''')
            continue
        elif move == 'claw':
            player_damage = random.randint(min_roll, player_dict['attack'])
        else: #move is bite
            player_damage = random.randint(0, 2 * player_dict['attack'])
            if player_damage == 0:
                print('''
                You haven't had food in too long! 
                You forgot how to bite and you missed!
                ''')
        print(f'''
        You used {move}! It did {player_damage} damage!
        ''')
        print(random.choice(enemy_dict['attack_flavour_text']))
        # 6. subtract hp from enemy
        enemy_hp -= player_damage
        # 7. subtract hp from player
        enemy_damage = random.randint(enemy_min_roll, enemy_attack)
        player_dict['hp'] -= enemy_damage

        input('Press enter to continue...')

    if enemy_hp <= 0:
        print(f'''
        You defeated the {enemy}!
        You gained {xp_gain} xp!
        ''')
        player_dict['xp'] += xp_gain
        input('Press enter to continue...')
    if player_dict['hp'] <= 0:
        print('''
        You died.
        That was unfortunate.
        ''')
        if input('Would you like to play again? (y/n) ').lower() == 'y':
            # need to decide what to do if they die
            pass



def get_player_choice(command_map: dict) -> str:
    choices = list(command_map.keys())
    player_choice = input('Enter the number or first letter of an option: ')

    if player_choice.isdigit() and 1 <= int(player_choice) <= len(choices):
        return choices[int(player_choice) - 1]

    # TODO: see if this can be reformatted
    valid_choice = list(filter(lambda choice: choice.startswith(player_choice.lower()), choices))

    if len(valid_choice) != 1:
        print_out = '*** Invalid choice. Please try again. ***'
        print(f'\n{print_out:^47}\n')
        return get_player_choice(command_map)

    return valid_choice[0]
