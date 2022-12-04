"""
This module contains the basic fight sequence and the functions that are used in the fight sequence.
"""

import itertools
import json
import random
import time
from pathlib import Path
from printer import print_health, print_attack_menu, print_enemy_picture, print_from_text_file, print_map, \
    print_scrolling_text
from skeleton import get_player_choice, validate_yes_no
from player import show_inventory
from levels import level_final
from skeleton import make_board


def load_enemy(enemy: str) -> dict:
    """
    Return a dictionary of the enemy's stats from enemy.json file.

    :param enemy: a string of the enemy's name
    :precondition: enemy must be a valid enemy name
    :precondition: enemy must be in enemy.json
    :postcondition: returns a dictionary of the enemy's stats
    :return: dictionary of the enemy's stats
    """
    with open(Path('json/') / 'enemy.json') as file:
        enemy_json = json.load(file)
    return enemy_json[enemy]


def calc_min_roll(player_attack: int, enemy_attack: int) -> tuple[int, int]:
    """
    Calculate the minimum possible damage the player and enemy can make.

    :param player_attack: the attack of the player as an integer
    :param enemy_attack: the attack of the enemy as an integer
    :precdondition: player_attack and enemy_attack must be integers >= 0
    :postcondition: returns a tuple of the minimum damage the player and enemy can make
    :return: a tuple of the minimum possible damage for the player and enemy as integers
    """
    min_roll = max(1, player_attack - 10)
    enemy_min_roll = max(1, enemy_attack - 10)
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


def charge(player_dict: dict, enemy_name: str, player_min_roll: int) -> int:
    """
    Return twice the amount of player's attack points and deal random amount of self damage.

    :param player_dict: dictionary of the player's stats
    :param enemy_name: the enemy's name as a string
    :param player_min_roll: minimum damage the player can deal
    :precondition: player_dict must contain 'attack' and 'hp' keys
    :precondition: player_dict['attack'] and player_dict['hp'] must be integers
    :precondition: enemy_name must be a string
    :precondition: player_min_roll must be an integer
    :postcondition: return twice the amount of player's attack points
    :postcondition: deal random amount of self damage between player_min_roll and player's attack points
    :return: the amount of damage the player dealt to the enemy
    """
    player_damage = 2 * player_dict['attack']
    self_damage = random.randint(player_min_roll, player_dict['attack'])
    player_dict['hp'] -= self_damage

    print(f'''
    You feel your power increasing!
    You rush at the {enemy_name} and do {player_damage} damage!

    However, in your rage, you also did {self_damage} damage to yourself.
    
    ''')
    return player_damage


def claw(player_dict: dict, enemy_name: str, player_min_roll: int) -> int:
    """
    Return the amount of damage player will deal.

    Amount of damage is random between player's minimum damage and player's attack points.

    :param player_dict: dictionary of the player's stats
    :param enemy_name: the enemy's name as a string
    :param player_min_roll: minimum damage the player can deal
    :precondition: player_dict must contain 'attack' key
    :precondition: player_dict['attack'] must be an integer
    :precondition: enemy_name must be a string
    :precondition: player_min_roll must be an integer
    :postcondition: return an integer of the amount of damage the player will deal
    :return: an integer of the amount of damage the player will deal
    """
    player_damage = random.randint(player_min_roll, player_dict['attack'])
    print(f'''
    You clawed at the {enemy_name}! It did {player_damage} damage!
    They say ouchie :(
    
    ''')
    return player_damage


def bite(player_dict: dict, enemy_name: str) -> int:
    player_damage = random.randint(0, 2 * player_dict['attack'])
    if player_damage == 0:
        print('''
                You haven't had food in too long! 
                You forgot how to bite and you missed!
                
                    ''')
    else:
        print(f'''
        You bit the {enemy_name}! It did {player_damage} damage!
        
        What a yummy taste!
        
        ''')
    return player_damage


def enemy_turn(player_dict: dict, enemy_dict: dict, enemy_min_roll: int) -> None:
    enemy_damage = random.randint(enemy_min_roll, enemy_dict['attack'])
    player_dict['hp'] -= enemy_damage
    print('      ', random.choice(enemy_dict['attack_flavour_text']), '\n\n')


def player_turn(player_dict: dict, enemy_name: str, player_attacks: dict, player_min_roll: int) -> int or None:
    print_attack_menu(player_attacks)
    move = get_player_choice(player_attacks)

    if move == 'inventory':
        # TODO: remove main from here
        show_inventory(player_dict)
        input('Press enter to continue...')
        return None
    elif move == 'charge':
        return charge(player_dict, enemy_name, player_min_roll)
    elif move == 'claw':
        return claw(player_dict, enemy_name, player_min_roll)
    else:  # move is bite
        return bite(player_dict, enemy_name)


def final_boss_defeated():
    print_from_text_file('hunter_dead.txt')
    print('''
    You have defeated the final boss!
    You have won the game!
    
    ''')
    exit()


def fight_sequence(enemy: str, player_dict: dict) -> None:
    enemy_dict = load_enemy(enemy)
    # Get dictionary of possible player attacks
    player_attacks = player_dict['attacks']
    current_level = player_dict['level']

    # Add attack to move list if player is high enough level
    player_options = dict(itertools.takewhile(lambda item: item[1] <= current_level, player_attacks.items()))
    player_options['inventory'] = 4
    print(f'{"FIGHT!":^56}')
    time.sleep(1)

    while True:
        # 1. print ascii image from file
        file_to_use = enemy_dict['name']
        print_enemy_picture(file_to_use + '.txt')

        # 2. print health bars
        print_health(player_dict, enemy_dict)

        # 3. print attack options
        player_min_roll, enemy_min_roll = calc_min_roll(player_dict['attack'], enemy_dict['attack'])
        damage = player_turn(player_dict, enemy_dict['name'], player_options, player_min_roll)
        if damage is None:
            continue

        # 4. subtract hp from enemy
        enemy_dict['hp'] -= damage
        if enemy_dict['hp'] <= 0 or player_dict['hp'] <= 0:
            break

        # 5. Enemy's turn
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


def final_boss_loop(player_dict: dict, enemy_name: str) -> None:
    # Get dictionary of possible player attacks
    player_attacks = player_dict['attacks']
    current_level = player_dict['level']

    # Add attack to move list if player is high enough level
    player_options = dict(itertools.takewhile(lambda item: item[1] <= current_level, player_attacks.items()))
    player_options['inventory'] = 4

    # Set stage for final boss
    # TODO: Print scrolling text for final boss intro
    boss_dict = load_enemy(enemy_name)
    final_boss = level_final.Boss(boss_dict)
    board = make_board(5, 5, 4)
    # print_scrolling_text('final_boss_intro.txt')
    print_from_text_file('hunter_shoot_straight.txt')

    while True:
        # Resets the board if player dies
        if player_dict['turn'] == 1:
            final_boss = level_final.Boss(boss_dict)
            board = make_board(5, 5, 4)

        # Print the grid
        print_map(board, 5, 5, player_dict, final_boss.get_location())

        # 3. print attack options
        player_min_roll, enemy_min_roll = calc_min_roll(player_dict['attack'], final_boss.get_stats()['attack'])
        damage = player_turn(player_dict, final_boss.get_stats()['name'], player_options, player_min_roll)
        if damage is None:
            continue

        # 4. subtract hp from enemy
        final_boss.is_damaged(damage)
        if final_boss.is_dead() or player_dict['hp'] <= 0:
            break

        # 5. Final_boss turn
        final_boss.choose_move(player_dict)
        print_health(player_dict, final_boss.get_stats())
        if player_dict['hp'] <= 0:
            death_sequence(player_dict)
            break

        # 6. Check if player dies
        if player_dict['hp'] <= 0:
            death_sequence(player_dict)
            player_dict['turn'] = 1
            continue


def main():
    print('Please run game.py. This is a module.')


if __name__ == '__main__':
    main()
