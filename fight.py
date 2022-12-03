import json
import random
import time
from printer import print_health, print_attack_menu, print_enemy_picture, print_from_text_file
from skeleton import get_player_choice
from player import show_inventory


def load_enemy(enemy: str) -> dict:
    with open('enemy.json') as file:
        enemy_json = json.load(file)
    return enemy_json[enemy]


def calc_min_roll(player_dict: dict, enemy_dict: dict) -> tuple[int, int]:
    min_roll = max(1, player_dict['attack'] - 10)
    enemy_min_roll = max(1, enemy_dict['attack'] - 10)
    return min_roll, enemy_min_roll


def death_sequence(player_dict: dict) -> None:
    print('''
    You died.
    That was unfortunate.
    
    You can start again from the beginning of the level with your inventory intact.
    ''')
    restart = input(input('Restart the level? (y/n)').lower())
    if restart == 'y':
        player_dict['turns'] = 0
        player_dict['hp'] = player_dict['max_hp']
        player_dict['xp'] = 0
        player_dict['location'] = (0, 0)
    elif restart == 'n':
        if input('Quit the game? (y/n)').lower() == 'y':
            print_from_text_file('goodbye.txt')
            exit()
        else:
            return death_sequence(player_dict)
    else:
        print('Please enter y or n.')
        return death_sequence(player_dict)


def victory(player_dict: dict, enemy_dict: dict) -> None:
    print_health(player_dict, enemy_dict)
    print(f'''
        You defeated the {enemy_dict['name']}!
        You gained {enemy_dict['xp_gain']} xp!
        ''')
    player_dict['xp'] += enemy_dict['xp_gain']
    input('Press enter to continue...')


def charge(player_dict: dict, enemy_dict: dict, player_min_roll: int) -> None:
    player_damage = 2 * player_dict['attack']
    enemy_dict['hp'] -= player_damage
    self_damage = random.randint(player_min_roll, player_dict['attack'])
    player_dict['hp'] -= self_damage

    print(f'''
    You feel your power increasing!
    You rush at the enemy and do {player_damage} damage!

    However, in your rage, you also did {self_damage} damage to yourself.
    
    The enemy is stunned.
    ''')
    input('Press enter to continue...')


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
    print(type(enemy_dict['hp']))
    while enemy_dict['hp'] > 0 and player_dict['hp'] > 0:
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
            charge(player_dict, enemy_dict, player_min_roll)
            continue
        elif move == 'claw':
            damage = claw(player_dict, enemy_dict, player_min_roll)
        else:  # move is bite
            damage = bite(player_dict, enemy_dict)

        # 6. subtract hp from enemy
        enemy_dict['hp'] -= damage
        if enemy_dict['hp'] <= 0:
            print_health(player_dict, enemy_dict)
            victory(player_dict, enemy_dict)

        # 7. Enemy's turn
        enemy_turn(player_dict, enemy_dict, enemy_min_roll)
        if player_dict['hp'] <= 0:
            death_sequence(player_dict)

        print_health(player_dict, enemy_dict)
        input('Press enter to continue...')


def main():
    print('Please run game.py. This is a module.')


if __name__ == '__main__':
    main()
