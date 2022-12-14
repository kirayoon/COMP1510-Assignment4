"""
This module contains the basic fight sequence and the functions that are used in the fight sequence.
"""

import itertools
import json
import random
import time
from pathlib import Path
from printer import print_health, print_attack_menu, print_enemy_picture, print_from_text_file, print_map
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

    >>> load_enemy('test')
    {'name': 'test'}
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
    min_roll = max(1, int(player_attack/3))
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
        player_dict['soup_counter'] = 0
        player_dict['chair_counter'] = 0
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
    :precondition: player_dict must contain 'xp' and 'inventory' and 'kills' keys
    :precondition: player_dict['xp'], and player_dict['kills'] must be integers
    :precondition: player_dict['inventory'] must be a dictionary with string keys and integer values
    :precondition: enemy_dict must contain 'name', 'drop', and 'xp_gain' keys
    :precondition: enemy_dict['name'] must be a string
    :precondition: enemy_dict['drop'] must be a string
    :precondition: enemy_dict['xp_gain'] must be an integer
    :postcondition: add kill to player_dict['kills']
    :postcondition: add xp to player_dict['xp']
    :postcondition: add loot to player_dict['inventory']

    Too difficult to test.
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
    if enemy_drop_name in player_dict['inventory']:
        player_dict['inventory'][enemy_drop_name] += 1
    else:
        player_dict['inventory'][enemy_drop_name] = 1
    player_dict['kills'] += 1


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
    self_damage = random.randint(player_min_roll, int(player_dict['attack']/2))
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
    """
    Return the amount of damage player will deal.

    Amount of damage is random between 0 and twice the player's attack points.

    :param player_dict: dictionary of the player's stats
    :param enemy_name: the enemy's name as a string
    :precondition: player_dict must contain 'attack' key
    :precondition: player_dict['attack'] must be an integer
    :precondition: enemy_name must be a string
    :postcondition: return an integer of the amount of damage the player will deal
    :return: an integer of the amount of damage the player will deal
    """
    player_damage = random.randint(0, 2 * player_dict['attack'])
    if player_damage == 0:
        print('''\n\tYou haven't had food in too long!\n\tYou forgot how to bite and you missed!
                
        ''')
    else:
        print(f'''\n\tYou bit the {enemy_name}! It did {player_damage} damage!\n\tWhat a yummy taste!
        
        ''')
    return player_damage


def enemy_turn(player_dict: dict, enemy_dict: dict, enemy_min_roll: int) -> None:
    """
    Deal damage to the player.

    Amount of damage is random between enemy's minimum damage and enemy's attack points.

    :param player_dict: dictionary of the player's stats
    :param enemy_dict: dictionary of the enemy's stats
    :param enemy_min_roll: an integer of the minimum damage the enemy can deal
    :precondition: player_dict must be a dictionary containing 'hp' as key
    :precondition: player_dict['hp'] must be an integer
    :precondition: enemy_dict must be a dictionary containing 'attack' and 'attack_flavour_text' as keys
    :precondition: enemy_dict['attack'] must be an integer
    :precondition: enemy_dict['attack_flavour_text'] must be a list of strings
    :postcondition: deal damage to the player
    :postcondition: print a random enemy's attack flavour text

    Too difficult to test.
    """
    enemy_damage = random.randint(enemy_min_roll, enemy_dict['attack'])
    player_dict['hp'] -= enemy_damage
    print('      ', random.choice(enemy_dict['attack_flavour_text']), '\n\n')


def player_turn(player_dict: dict, enemy_name: str, player_attacks: dict, player_min_roll: int) -> int or None:
    """
    Return the result of player's selected move.

    :param player_dict: dictionary of the player's stats
    :param enemy_name: the enemy's name as a string
    :param player_attacks: dictionary of the player's attacks
    :param player_min_roll: minimum damage the player can deal
    :precondition: player_dict must be a dictionary
    :precondition: enemy_name must be a string
    :precondition: player_attacks must be a dictionary
    :precondition: player_min_roll must be an integer
    :postcondition: execute the player's move and return the amount of damage the player deals
    :postcondition: execute show_inventory if player chooses 'inventory' and return None
    :return: integer of the damage the player will deal with their move or None if 'inventory' is chosen

    Too difficult to test.
    """
    print_attack_menu(player_attacks)
    move = get_player_choice(player_attacks)

    if move == 'inventory':
        show_inventory(player_dict)
        input('Press enter to continue...')
        return None
    elif move == 'charge':
        return charge(player_dict, enemy_name, player_min_roll)
    elif move == 'claw':
        return claw(player_dict, enemy_name, player_min_roll)
    elif move == 'bite':  # move is bite
        return bite(player_dict, enemy_name)


def final_boss_defeated(player_dict: dict, time_played: float) -> None:
    """
    Print the final boss defeated message.

    :param player_dict: dictionary of the player's stats
    :param time_played: the time the player has played the game
    :precondition: player_dict must be a dictionary
    :precondition: player_dict must contain the keys 'damage_dealt', 'kills', 'deaths', and 'egg_count'
    :precondition: the values of the keys must be integers
    :precondition: time_played must be a float
    :postcondition: print the final boss defeated message

    Too difficult to test.
    """
    print_from_text_file('hunter_dead.txt')
    minutes = int(time_played // 60)
    print(f'''
    You have defeated the final boss!
    You have won the game!
    ''')

    print(f''' 
    Stats:
    You played for {minutes:.2f} minutes!
    In total, you did {player_dict['damage_dealt']} damage!
    You killed {player_dict['kills']} enemies!
    You died {player_dict['deaths']} times!
    Overall, you did {player_dict['useless_events']} useless events!
    
    You found {player_dict['eggs_found']}/9 eggs!
    ''')
    if player_dict['eggs_found'] == 9:
        print('''\n\tYou found all the eggs! You are the best!
        ''')
    else:
        print('''\n\tYou did not find all the eggs. Better luck next time!
        ''')

    exit()


def fight_sequence(enemy: str, player_dict: dict) -> None:
    """
    Fight with the enemy until enemy or player dies.

    :param enemy: string of the enemy's name
    :param player_dict: dictionary of the player's stats
    :precondition: enemy must be a string
    :precondition: enemy must be a valid enemy
    :precondition: player_dict must be a dictionary containing 'attacks', 'level', 'attack', and 'hp' as keys
    :precondition: player_dict['attacks'] must be a dictionary containing 'charge', 'claw', and 'bite' as keys
    :precondition: values of 'level', 'attack', and 'hp' must be integers
    :postcondition: fight with the enemy until enemy or player dies
    :postcondition: execute victory function if enemy dies
    :postcondition: execute death_sequence function if player dies

    Too difficult to test.
    """
    enemy_dict = load_enemy(enemy)
    # Get dictionary of possible player attacks
    player_attacks = player_dict['attacks']
    current_level = player_dict['level']

    # Add attack to move list if player is high enough level
    player_options = dict(itertools.takewhile(lambda item: item[1] <= current_level, player_attacks.items()))
    player_options['inventory'] = 4
    print(f'{"FIGHT!":^56}')
    time.sleep(1)
    input('Press enter to continue...')

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
        player_dict['damage_dealt'] += damage
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


def check_player_close_to_boss(player_location: tuple, boss_location: tuple) -> bool:
    """
    Return True if player is close to boss.

    :param player_location: tuple of the player's location
    :param boss_location: tuple of the boss's location
    :precondition: player_location must be a tuple of two integers
    :precondition: boss_location must be a tuple of two integers
    :postcondition: return True if player is close to boss
    :return: True if player is close to boss

    >>> check_player_close_to_boss((1, 1), (2, 2))
    True
    >>> check_player_close_to_boss((1, 1), (3, 3))
    False
    """
    if abs(player_location[0] - boss_location[0]) <= 1 and abs(player_location[1] - boss_location[1]) <= 1:
        return True
    return False


# move the player 1 square closer to the boss
def move_player_towards_boss(player_location: tuple, boss_location: tuple) -> tuple:
    """
    Move the player 1 square closer to the boss.

    :param player_location: tuple of the player's location
    :param boss_location: tuple of the boss's location
    :precondition: player_location must be a tuple of two positive integers
    :precondition: boss_location must be a tuple of two positive integers
    :postcondition: move the player 1 square closer to the boss
    :return: tuple of the player's new location

    >>> move_player_towards_boss((1, 1), (3, 3))
    (2, 2)
    >>> move_player_towards_boss((1, 1), (1, 3))
    (1, 2)
    >>> move_player_towards_boss((1, 1), (3, 1))
    (2, 1)
    """
    distance_between = [boss_location[0] - player_location[0], boss_location[1] - player_location[1]]
    try:
        distance_between[0] //= abs(distance_between[0])
    except ZeroDivisionError:
        distance_between[0] = 0
    try:
        distance_between[1] //= abs(distance_between[1])
    except ZeroDivisionError:
        distance_between[1] = 0

    return player_location[0] + distance_between[0], player_location[1] + distance_between[1]


def final_boss_loop(player_dict: dict, enemy_name: str) -> None:
    """
    Fight with the final boss until player or boss dies.

    :param player_dict: dictionary of the player's stats
    :param enemy_name: string of the final boss's name
    :precondition: player_dict must be a dictionary containing 'attacks', 'level', 'turn', 'attack', and 'hp' as keys
    :precondition: player_dict['attacks'] must be a dictionary containing 'charge', 'claw', and 'bite' as keys
    :precondition: values of 'level', 'turn', 'attack', and 'hp' must be integers
    :precondition: enemy_name must be a string and must be a valid enemy
    :postcondition: fight with the final boss until player or boss dies
    :postcondition: execute death_sequence function if player dies

    Too difficult to test.
    """
    # Get dictionary of possible player attacks
    player_attacks = player_dict['attacks']
    current_level = player_dict['level']

    # Add attack to move list if player is high enough level
    player_options = dict(itertools.takewhile(lambda item: item[1] <= current_level, player_attacks.items()))
    player_options['inventory'] = 4

    # Set stage for final boss
    boss_dict = load_enemy(enemy_name)
    final_boss = level_final.Boss(boss_dict)
    board = make_board(5, 5, 4)

    while True:
        # Resets the board if player dies
        if player_dict['turn'] == 1:
            final_boss = level_final.Boss(boss_dict)
            board = make_board(5, 5, 4)

        # Print the grid
        print_map(board, 5, 5, player_dict, final_boss.get_location())

        is_close = check_player_close_to_boss(player_dict['location'], final_boss.get_location())
        if is_close:
            # 3. print attack options
            player_min_roll, enemy_min_roll = calc_min_roll(player_dict['attack'], final_boss.get_stats()['attack'])
            damage = player_turn(player_dict, final_boss.get_stats()['name'], player_options, player_min_roll)
            if damage is None:
                continue

            # 4. subtract hp from enemy
            player_dict['damage_dealt'] += damage
            final_boss.is_damaged(damage)
            print_health(player_dict, final_boss.get_stats())
            if final_boss.is_dead() or player_dict['hp'] <= 0:
                break

        else:
            # Print command options for player (only one move: Close the gap!)
            far_choices = {'close the gap!': '', 'inventory': ''}
            print_attack_menu(far_choices)
            choice = get_player_choice(far_choices)
            if choice == 'close the gap!':
                player_dict['location'] = move_player_towards_boss(player_dict['location'], final_boss.get_location())
            if choice == 'inventory':
                show_inventory(player_dict)
                continue

        player_dict['turn'] += 1

        # 5. Final_boss turn
        final_boss.choose_move(player_dict)
        print_health(player_dict, final_boss.get_stats())

        # 6. Check if player dies
        if player_dict['hp'] <= 0:
            death_sequence(player_dict)
            player_dict['turn'] = 1
            continue

        input('Press enter to continue...')


def main():
    """
    Drive the program
    """
    print('Please run game.py. This is a module.')


if __name__ == '__main__':
    main()
