import json
import random
import time
from printer import print_health, print_attack_menu
from skeleton import get_player_choice
from player import show_inventory


def fight_sequence(enemy: str, player_dict: dict):
    # fight code here
    # code to read json file
    # with open('enemy.json') as f:
    #     enemy_dict = json.load(f)

    # for testing
    with open('enemy.json') as file:
        enemy_json = json.load(file)
    enemy_dict = enemy_json[enemy]
    print(enemy_dict)

    #  Select the right enemy
    # enemy_attack = enemy_dict['attack']
    # enemy_hp = enemy_dict['max_hp']
    # xp_gain = enemy_dict['xp_gain']
    #
    # print(enemy_hp, enemy_attack, xp_gain)
    # while enemy_hp > 0:
    #     print from
    time.sleep(1)
    print(f'{"FIGHT!":^56}')
    while enemy_dict['hp'] > 0 and player_dict['hp'] > 0:
        # 1. print ascii image from file

        # 2. print health bars
        print_health(player_dict, enemy_dict)

        # 3. print attack options
        player_attacks = {'claw': 'claw', 'bite': 'bite', 'charge': 'charge', 'inventory': 'inventory'}
        print_attack_menu(player_attacks)
        move = get_player_choice(player_attacks)

        min_roll = max(1, player_dict['attack'] - 10)
        enemy_min_roll = max(1, enemy_dict['attack'] - 10)
        if move == 'inventory':
            # TODO: remove main from here
            show_inventory(player_dict)
            continue
        elif move == 'charge':
            player_damage = 2 * player_dict['attack']
            enemy_dict['hp'] -= player_damage
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
        else:  # move is bite
            player_damage = random.randint(0, 2 * player_dict['attack'])
            if player_damage == 0:
                print('''
            You haven't had food in too long! 
            You forgot how to bite and you missed!
                ''')
        print(f'''
        You used {move}! It did {player_damage} damage!
        ''')
        print('      ', random.choice(enemy_dict['attack_flavour_text']), '\n\n')
        # 6. subtract hp from enemy
        enemy_dict['hp'] -= player_damage
        # 7. subtract hp from player
        enemy_damage = random.randint(enemy_min_roll, enemy_dict['attack'])
        player_dict['hp'] -= enemy_damage

        input('Press enter to continue...')

    if enemy_dict['hp'] <= 0:
        print_health(player_dict, enemy_dict)
        print(f'''
        You defeated the {enemy}!
        You gained {enemy_dict['xp_gain']} xp!
        ''')
        player_dict['xp'] += enemy_dict['xp_gain']
        # input('Press enter to continue...')

    if player_dict['hp'] <= 0:
        print('''
        You died.
        That was unfortunate.
        ''')
        if input('Would you like to play again? (y/n) ').lower() == 'y':
            # need to decide what to do if they die
            pass
