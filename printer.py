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
                print("  |  (P)", end="")
            else:
                print("  |     ", end="")
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


def main():
    print('Please run the game.py file. This is a module.')


if __name__ == '__main__':
    main()
