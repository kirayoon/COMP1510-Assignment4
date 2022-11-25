import os
import random
import time
from pathlib import Path
# from levels import level_1, level_2, level_3, level_final


# TODO: use itertools


def print_grid(board: list[list]) -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in range(10):
        print(" +---+---+---+---+---+---+---+---+---+---+")
        for col in range(10):
            print(" |", board[row][col], end="")
        print(' |', end="\n")
    print(" +---+---+---+---+---+---+---+---+---+---+")


def make_board(row: int, col: int) -> list[list]:
    return [[u"\u25A1" for _ in range(row)] for _ in range(col)]


def print_scrolling_text(text_file: str) -> None:
    folder = Path("text/")
    text_file = folder / text_file
    with open(text_file, 'r') as file:
        script = [line.rstrip('\n') for line in file]

    height = len(script)
    num = 0
    while height:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n' * height)
        for line in script[:num + 1]:
            print(line)
        # TODO: change this for final
        time.sleep(.5)

        height -= 1
        num += 1
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

    move, info = 0, 5
    while info < len(menu):
        print(f"{menu[move][0]:8}: {menu[move][1].title(): <15} {menu[info][0]}: {menu[info][1].title()}")
        move += 1
        info += 1

    print(f"{menu[4][0]:8}: {menu[4][1]: <15}\n")


# player_location is a tuple with i and j coordinates (row, col)
def get_player_choice(command_map: dict) -> str:
    choices = list(command_map.keys())
    player_choice = input('Enter the number or first letter of an option: ')

    if player_choice.isdigit() and 1 <= int(player_choice) <= 9:
        return choices[int(player_choice) - 1]

    # TODO: see if this can be reformatted
    valid_choice = list(filter(lambda choice: choice.startswith(player_choice.lower()), choices))

    if len(valid_choice) != 1:
        print('', 'Invalid choice. Please try again.', sep='\n')
        return get_player_choice(command_map)

    return valid_choice[0]


def validate_move(player_input: str, i_coord: int, j_coord: int, board_height: int) -> bool:
    move_dictionary = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    board_width = board_height
    if player_input in move_dictionary:
        direction = move_dictionary[player_input]
    else:
        return False
    new_loc = (i_coord + direction[0], j_coord + direction[1])
    if 0 <= new_loc[0] < board_height and 0 <= new_loc[1] < board_width:
        return True
    return False


# Functions for each basic command
def up(player_dict):
    print('Walking up...')
    time.sleep(1)
    player_dict['i-coord'] -= 1


def down(player_dict):
    print('Walking down...')
    time.sleep(1)
    player_dict['i-coord'] += 1


def left(player_dict):
    print('Walking left...')
    time.sleep(1)
    player_dict['j-coord'] -= 1


def right(player_dict):
    print('Walking right...')
    time.sleep(1)
    player_dict['j-coord'] += 1


def player_sleep(player_dict):
    player_dict['hp'] = player_dict['max_hp']
    print(f'''
    You sleep under the stars and dreamt of being full. 
    What a good night.
    
    Your health has recovered to {player_dict["max_hp"]}.
    ''')
    input('Press enter to continue...')


def player_information():
    pass


def show_inventory():
    pass


def game():
    # TODO: store ascii art in a file
    # Print the title screen
    print_from_text_file('title_screen.txt')
    char_name = input('Please input your character\'s name:')
    print(f'\nHello {char_name}! Welcome to the game!')
    time.sleep(3)

    # Initialize player board
    board = make_board(row=10, col=10)

    # Play intro text leading to level_1 text
    print_scrolling_text('intro.txt')
    print_from_text_file('ascii_bear.txt')
    print_from_text_file('level_1.txt')

    # Initialize player information
    player = {'name': char_name,
              'location': 0,
              'i-coord': 0,
              'j-coord': 0,
              'inventory': [],
              'hp': 25,
              'max_hp': 25,
              'attack': 5,
              'defense': 5,
              'level': 1,
              'exp': 0,
              'max_exp': 1000}

    command_map = {'up': up,
                   'down': down,
                   'left': left,
                   'right': right,
                   'sleep': player_sleep,
                   'player': player_information,
                   'inventory': show_inventory,
                   'help': '',
                   'quit': ''}

    game_is_won = False
    while not game_is_won:
        # Print the grid
        print_grid(board)

        # Need function to describe room

        # Print player choices menu and get player's choice
        print_choices_menu(command_map)
        player_choice = get_player_choice(command_map)

        # just for test
        input(f'You chose {player_choice}. Press enter to continue.')

        # Print help if the player enters "help"
        if player_choice == 'help':
            # TODO: create help documentation
            print('''
            help documentation
            Type "quit" to quit the game, or "help" for help.
            ''')
            input('Press enter to continue...')
            continue
        # Quit the game if the player enters "quit"
        elif player_choice == 'quit':
            print()
            if input("Are you sure you want to quit? (y/n): ").lower() == 'y':
                os.system('cls' if os.name == 'nt' else 'clear')
                print('',
                      '+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+',
                      '|   ____               ____ _          _     _  |',
                      '|  / ___|   _  __ _   / ___| |__  _ __(_)___| | |',
                      '| | |  | | | |/ _` | | |   | \'_ \\| \'__| / __| | |',
                      '| | |__| |_| | (_| | | |___| | | | |  | \\__ \\_| |',
                      '|  \\____\\__, |\\__,_|  \\____|_| |_|_|  |_|___(_) |',
                      '|       |___/                                   |',
                      '+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+', sep='\n')
                quit()
            continue

        # Validate player movement
        valid_move = validate_move(player_choice, player['i-coord'], player['j-coord'], len(board))
        if valid_move:
            command = command_map[player_choice]
            command(valid_move)




        time.sleep(1)
        # TODO: add random events and main game loop

        input('the end....')


def main():
    game()


if __name__ == '__main__':
    main()
