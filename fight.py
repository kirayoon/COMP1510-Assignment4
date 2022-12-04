"""
This module contains the basic fight sequence and the functions that are used in the fight sequence.
"""


import json
import random
import time
from printer import print_health, print_attack_menu, print_enemy_picture, print_from_text_file
from skeleton import get_player_choice, validate_yes_no
from player import show_inventory


def load_enemy(enemy: str) -> dict:
    """
    Return a dictionary of the enemy's stats from enemy.json file.

    :param enemy: a string of the enemy's name
    :precondition: enemy must be a valid enemy name
    :precondition: enemy must be in enemy.json
    :postcondition: returns a dictionary of the enemy's stats
    :return: dictionary of the enemy's stats
    """
    with open('enemy.json') as file:
        enemy_json = json.load(file)
    return enemy_json[enemy]


def calc_min_roll(player_dict: dict, enemy_dict: dict) -> tuple[int, int]:
    """
    Calculate the minimum possible damage the player and enemy can make.

    :param player_dict: dictionary of the player's stats
    :param enemy_dict: dictionary of the enemy's stats
    :precdondition: player_dict and enemy_dict must contain 'attack' key
    :postcondition: returns a tuple of the minimum damage the player and enemy can make
    :return: a tuple of the minimum possible damage for the player and enemy as integers
    """
    min_roll = max(1, player_dict['attack'] - 10)
    enemy_min_roll = max(1, enemy_dict['attack'] - 10)
    return min_roll, enemy_min_roll


def death_sequence(player_dict: dict) -> None:
    """
    Restart the level or end the game if the player dies.

    Player dies if their hp is 0 or less.

    :param player_dict: dictionary of the player's stats
    :precondition: player_dict must contain 'turn', 'hp', 'max_hp', 'xp', and 'location' keys
    :precondition: player_dict values must be integers, except for 'location' which must be a tuple of integers
    :postcondition: restart level if player chooses yes
    :postcondition: end game if player chooses no
    """
    print('''
    You died.
    That was unfortunate.
    
    You can start again from the beginning of the level with your inventory intact.
    ''')
    restart = validate_yes_no('Restart the level? (y/n)')
    if restart == 'y':
        player_dict['turn'] = 0
        player_dict['hp'] = player_dict['max_hp']
        player_dict['xp'] = 0
        player_dict['location'] = (0, 0)
    elif restart == 'n':
        if validate_yes_no('Quit the game? (y/n)') == 'y':
            print_from_text_file('goodbye.txt')
            exit()
        else:
            return death_sequence(player_dict)


def victory(player_dict: dict, enemy_dict: dict) -> None:
    """
    Gain xp and loot from the enemy if the enemy is defeated.

    Enemy is defeated if their hp is 0 or less.
    
    :param player_dict: dictionary of the player's stats
    :param enemy_dict: dictionary of the enemy's stats
    :precondition: player_dict must contain 'xp' and 'inventory' keys
    :precondition: player_dict['xp'] must be an integer
    :precondition: player_dict['inventory'] must be a dictionary with string keys and integer values
    :precondition: enemy_dict must contain 'name', 'drop', and 'xp_gain' keys
    :precondition: enemy_dict['name'] must be a string
    :precondition: enemy_dict['drop'] must be a string
    :precondition: enemy_dict['xp_gain'] must be an integer
    :postcondition: add xp to player_dict['xp']
    :postcondition: add loot to player_dict['inventory']
    """
    print_health(player_dict, enemy_dict)
    enemy_name = enemy_dict['name']
    enemy_drop_name = enemy_dict['drop']
    print(f'''
        You defeated the {enemy_name}!
        You gained {enemy_dict['xp_gain']} xp!
        
        {enemy_name} has been added to your inventory!
        
        ''')
    player_dict['xp'] += enemy_dict['xp_gain']
    if enemy_name in player_dict['inventory']:
        player_dict['inventory'][enemy_drop_name] += 1
    else:
        player_dict['inventory'][enemy_drop_name] = 1


def charge(player_dict: dict, enemy_dict: dict, player_min_roll: int) -> int:
    player_damage = 2 * player_dict['attack']
    self_damage = random.randint(player_min_roll, player_dict['attack'])
    player_dict['hp'] -= self_damage

    print(f'''
    You feel your power increasing!
    You rush at the {enemy_dict['name']} and do {player_damage} damage!

    However, in your rage, you also did {self_damage} damage to yourself.
    
    ''')
    return player_damage


def claw(player_dict: dict, enemy_dict: dict, player_min_roll: int) -> int:
    player_damage = random.randint(player_min_roll, player_dict['attack'])
    print(f'''
    You clawed at the {enemy_dict['name']}! It did {player_damage} damage!
    They say ouchie :(
    
    ''')
    return player_damage


def bite(player_dict: dict, enemy_dict: dict) -> int:
    player_damage = random.randint(0, 2 * player_dict['attack'])
    if player_damage == 0:
        print('''
                You haven't had food in too long! 
                You forgot how to bite and you missed!
                
                    ''')
    else:
        print(f'''
        You bit the {enemy_dict['name']}! It did {player_damage} damage!
        
        What a yummy taste!
        
        ''')
    return player_damage


def enemy_turn(player_dict: dict, enemy_dict: dict, enemy_min_roll: int) -> None:
    enemy_damage = random.randint(enemy_min_roll, enemy_dict['attack'])
    player_dict['hp'] -= enemy_damage
    print('      ', random.choice(enemy_dict['attack_flavour_text']), '\n\n')


def fight_sequence(enemy: str, player_dict: dict) -> None:
    enemy_dict = load_enemy(enemy)
    print(f'{"FIGHT!":^56}')
    time.sleep(1)

    while True:
        # 1. print ascii image from file
        file_to_use = enemy_dict['name']
        print_enemy_picture(file_to_use + '.txt')
        # 2. print health bars
        print_health(player_dict, enemy_dict)

        # 3. print attack options
        player_attacks = {'claw': 'claw', 'bite': 'bite', 'charge': 'charge', 'inventory': 'inventory'}
        print_attack_menu(player_attacks)
        move = get_player_choice(player_attacks)

        # Get min rolls
        player_min_roll, enemy_min_roll = calc_min_roll(player_dict, enemy_dict)

        if move == 'inventory':
            # TODO: remove main from here
            show_inventory(player_dict)
            input('Press enter to continue...')
            continue
        elif move == 'charge':
            damage = charge(player_dict, enemy_dict, player_min_roll)
            # continue
        elif move == 'claw':
            damage = claw(player_dict, enemy_dict, player_min_roll)
        else:  # move is bite
            damage = bite(player_dict, enemy_dict)

        # 6. subtract hp from enemy
        enemy_dict['hp'] -= damage
        if enemy_dict['hp'] <= 0 or player_dict['hp'] <= 0:
            break

        # 7. Enemy's turn
        enemy_turn(player_dict, enemy_dict, enemy_min_roll)
        if player_dict['hp'] <= 0:
            break

        print_health(player_dict, enemy_dict)
        input('Press enter to continue...')

    if enemy_dict['hp'] <= 0:
        victory(player_dict, enemy_dict)
    if player_dict['hp'] <= 0:
        print_health(player_dict, enemy_dict)
        death_sequence(player_dict)


def main():
    print('Please run game.py. This is a module.')


if __name__ == '__main__':
    main()
