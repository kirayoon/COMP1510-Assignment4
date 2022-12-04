"""
This module contains functions that print to the screen.
"""


import os
from pathlib import Path
import time
import json


def print_map(board: dict, board_height: int, board_width: int, player_dict: dict, boss_loc=None) -> None:
    """
    Print the map to the screen.

    :param board: dictionary of the board with the keys as coordinates and values as event names
    :param board_height: integer of the height of the board
    :param board_width: integer of the width of the board
    :param player_dict: dictionary of the player's stats
    :param boss_loc: tuple of the boss's location for the boss fight
    :precondition: board must be a dictionary with the keys as tuples of coordinates and values as strings
    :precondition: board_height must be an integer
    :precondition: board_width must be an integer
    :precondition: player_dict must be a dictionary containing 'level' and 'location' keys
    :precondition: values of 'level' must be an integer and 'location' must be a tuple of integers of coordinates
    :precondition: boss_loc must be a tuple of integers of coordinates
    :postcondition: prints the map to the screen
    :postcondition: each coordinate is filled depending on the event at that coordinate
    :postcondition: prints player's level and level goal at the top of the map
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    with open('level_desc.json') as file:
        level_json = json.load(file)
    level_dict = level_json[str(player_dict['level'])]
    print(f'''
            Level {player_dict['level']}: {level_dict["name"]}
            Goal: {level_dict["goal"]}''')
    for row in range(board_height):
        print("  +-------+-------+-------+-------+-------+")
        print("  ", end="")
        for col in range(board_width):
            if board[(row, col)] == 'event2':
                print("|  (!)  ", end="")
            elif (row, col) == player_dict['location']:
                print("|ʕ•`ᴥ´•ʔ", end="")
            elif (row, col) == boss_loc:
                print("| •`_´• ", end="")
            elif board[(row, col)] == 'clear' or board[(row, col)] == 'start':
                print("|       ", end="")
            else:
                print("|   ?   ", end="")
        print('|', end="\n")
    print("  +-------+-------+-------+-------+-------+")


def print_scrolling_text(text_file: str) -> None:
    """
    Print the text from a text file to the screen one line at a time.

    :param text_file: a string of the name of the text file to be printed
    :precondition: text_file must be a string
    :precondition: text_file must be a valid file name in the text folder
    :postcondition: prints the text from the text file to the screen one line at a time
    :postcondition: prints a line of text every 0.5 seconds
    """
    text_file = Path('text/') / text_file
    with open(text_file, 'r') as file:
        script = [line.rstrip('\n') for line in file]

    height = len(script)
    num_lines = 0
    while height:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n' * height)
        for line in script[:num_lines + 1]:
            print(line)
        # TODO: change this for final
        time.sleep(.5)

        height -= 1
        num_lines += 1
    input('\nPress enter to continue...')
    os.system('cls' if os.name == 'nt' else 'clear')


def print_from_text_file(text_file: str) -> None:
    """
    Print the text from a text file to the screen.

    :param text_file: a string of the name of the text file to be printed
    :precondition: text_file must be a string
    :precondition: text_file must be a valid file name in the text folder
    :postcondition: prints the text from the text file to the screen
    """
    folder = Path("text/")
    text_file = folder / text_file
    with open(text_file, 'r', encoding='utf-8') as text_file:
        script = [line.rstrip('\n') for line in text_file]
    for line in script:
        print(line)
    input('\nPress enter to continue...')
    os.system('cls' if os.name == 'nt' else 'clear')


def print_choices_menu(command_map: dict) -> None:
    """
    Print the choices menu to the screen.

    Choices menu contains commands that the player can use.

    :param command_map: dictionary of the commands and their functions
    :precondition: command_map must be a dictionary with the keys as strings and values as functions or empty strings
    :postcondition: prints the choices menu to the screen
    :postcondition: prints the commands and their corresponding numbers
    :postcondition: prints movement commands in the first column and other commands in the second column
    """
    menu = list(enumerate(command_map.keys(), 1))
    headings = ["\033[4mMovement\033[0m", "\033[4mCommands\033[0m"]

    print(f'\n{headings[0]:>23}{headings[1]:>27}')

    move_idx, command_idx = 0, 5
    while command_idx < len(menu):
        print(
            f"{menu[move_idx][0]:8}: {menu[move_idx][1].title(): <15} "
            f"{menu[command_idx][0]}: {menu[command_idx][1].title()}")
        move_idx += 1
        command_idx += 1

    print(f"{menu[4][0]:8}: {menu[4][1].title(): <15}\n")


def print_attack_menu(command_map: dict) -> None:
    """
    Print the attack menu to the screen.

    :param command_map: dictionary of the commands and their functions
    :precondition: command_map must be a dictionary with the keys as strings and values as integers
    :precondition: keys must be the names of the attack move and values must be the damages
    :postcondition: prints the attack menu with possible moves to the screen
    """
    attack_menu = list(enumerate(command_map.keys(), 1))
    headings = ["\033[4mMoves\033[0m"]

    print(f'\n{headings[0]:^62}')
    for move in attack_menu:
        print(f'{move[0]:2}. {move[1].title()}', end='    ')
    print()


def convert_health_to_bars(health: int, max_health: int) -> tuple[str, str]:
    """
    Convert the health of the player or enemy to a tuple of strings.

    :param health: an integer of the health of the player or enemy
    :param max_health: an integer of the maximum health of the player or enemy
    :precondition: health must be an integer
    :precondition: max_health must be an integer
    :precondition: health must be less than or equal to max_health
    :postcondition: calculates the number of bars to be filled and empty
    :postcondition: calculates the percentage of health remaining
    :postcondition: converts the health bar and percentage to a tuple of strings
    :postcondition: the first string is the health in bars and the second string is the percentage of health in numbers
    :return: a tuple of strings
    """
    health = max(health, 0)
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
    print(f'|{player_health_bar}|{" " * 10}|{enemy_health_bar}|')
    print(f'{player_health_percentage:^22} {enemy_health_percentage:^40}')


def print_enemy_picture(text_file: str):
    os.system('cls' if os.name == 'nt' else 'clear')
    folder = Path("text/")
    text_file = folder / text_file
    with open(text_file, 'r') as text_file:
        script = [line.rstrip('\n') for line in text_file]
    for line in script:
        print(line)


def main():
    print('Please run the game.py file. This is a module.')


if __name__ == '__main__':
    main()
