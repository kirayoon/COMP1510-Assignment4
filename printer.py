import os
from pathlib import Path
import time


def print_map(board: dict, board_height: int, board_width: int, player_loc: tuple) -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in range(board_height):
        print("  +-------+-------+-------+-------+-------+")
        for col in range(board_width):
            if board[(row, col)] == 'event2':
                print("  |  (!)", end="")
            elif (row, col) == player_loc:
                print("  |  [X]", end="")
            elif board[(row, col)] == 'clear' or board[(row, col)] == 'start':
                print("  |     ", end="")
            else:
                print("  |   ? ", end="")
        print('  |', end="\n")
    print("  +-------+-------+-------+-------+-------+")


def print_scrolling_text(text_file: str) -> None:
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
    folder = Path("text/")
    text_file = folder / text_file
    with open(text_file, 'r') as text_file:
        script = [line.rstrip('\n') for line in text_file]
    for line in script:
        print(line)
    input('\nPress enter to continue...')
    os.system('cls' if os.name == 'nt' else 'clear')


def print_choices_menu(command_map: dict) -> None:
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


def print_attack_menu(command_map: dict):
    attack_menu = list(enumerate(command_map.keys(), 1))
    headings = ["\033[4mMoves\033[0m"]

    print(f'\n{headings[0]:^62}')
    for move in attack_menu:
        print(f'{move[0]:2}. {move[1].title()}', end='    ')
    print()


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
    print(f'|{player_health_bar}|{" " * 10}|{enemy_health_bar}|')
    print(f'{player_health_percentage:^22} {enemy_health_percentage:^40}')


def main():
    print('Please run the game.py file. This is a module.')


if __name__ == '__main__':
    main()
