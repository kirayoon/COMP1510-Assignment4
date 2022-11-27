import os
import random
import time
from pathlib import Path


# from levels import level_1, level_2, level_3, level_final


# TODO: use itertools


def print_map(board: dict, value_of_events: int, board_height: int) -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    board_width = board_height
    for row in range(board_height):
        print("  +-------+-------+-------+-------+-------+")
        for col in range(board_width):
            print("  | ", '(!)' if board[(row, col)] <= value_of_events else "   ", end="")
        print('  |', end="\n")
    print("  +-------+-------+-------+-------+-------+")


def make_board(num_row: int, num_col: int) -> dict:
    board_key = [(row, col) for row in range(num_row) for col in range(num_col)]
    board_values = [num for num in range(25)]
    random.shuffle(board_values)

    return dict(zip(board_key, board_values))


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

    move_idx, command_idx = 0, 5
    while command_idx < len(menu):
        print(
            f"{menu[move_idx][0]:8}: {menu[move_idx][1].title(): <15} {menu[command_idx][0]}: {menu[command_idx][1].title()}")
        move_idx += 1
        command_idx += 1

    print(f"{menu[4][0]:8}: {menu[4][1].title(): <15}\n")


# player_location is a tuple with i and j coordinates (row, col)
def get_player_choice(command_map: dict) -> str:
    choices = list(command_map.keys())
    player_choice = input('Enter the number or first letter of an option: ')

    if player_choice.isdigit() and 1 <= int(player_choice) <= 9:
        return choices[int(player_choice) - 1]

    # TODO: see if this can be reformatted
    valid_choice = list(filter(lambda choice: choice.startswith(player_choice.lower()), choices))

    if len(valid_choice) != 1:
        print_out = '*** Invalid choice. Please try again. ***'
        print_out_length = len(print_out)
        print(f'\n{print_out:^47}\n')
        return get_player_choice(command_map)

    return valid_choice[0]


def validate_move(player_input: str, player_coordinate: tuple, board: dict) -> bool:
    move_dictionary = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    direction = move_dictionary[player_input]
    new_loc = tuple(map(sum, zip(direction, player_coordinate)))

    if new_loc in board:
        return True

    return False


# Functions for each basic command
def up(player_location: tuple):
    print('Walking up...')
    time.sleep(1)
    return player_location[0] - 1, player_location[1]


def down(player_location: tuple):
    print('Walking down...')
    time.sleep(1)
    return player_location[0] + 1, player_location[1]


def left(player_location: tuple):
    print('Walking left...')
    time.sleep(1)
    return player_location[0], player_location[1] - 1


def right(player_location: tuple):
    print('Walking right...')
    time.sleep(1)
    return player_location[0], player_location[1] + 1


def player_sleep(player_dict: dict):
    player_dict['hp'] = player_dict['max_hp']
    print(f'''
    You sleep under the stars and dreamt of being full. 
    What a good night.
    
    Your health has recovered to {player_dict["max_hp"]}.
    ''')
    input('Press enter to continue...')


def player_information(player_dict: dict):
    stats = ['name', 'hp', 'max_hp', 'level', 'attack', 'xp', 'max_xp']
    print(f'\n{" "*7}{player_dict[stats[0]].title()} the Scary Bear',
          f'{stats[3].title():>12}: {player_dict[stats[3]]:>2} '
          f'{stats[5].upper():>7}: {player_dict[stats[5]]}/{player_dict[stats[6]]}',
          f'{stats[4].title():>13}: {player_dict[stats[4]]} '
          f'{stats[1].upper():>7}: {player_dict[stats[1]]}/{player_dict[stats[2]]}', sep='\n')


def show_inventory(player_dict: dict):
    pass


def game():
    # # TODO: store ascii art in a file
    # TODO: remove comment for production
    # # Print the title screen
    # print_from_text_file('title_screen.txt')
    char_name = input('Please input your character\'s name: ')
    # print(f'\nHello {char_name}! Welcome to the game!')
    # time.sleep(3)
    #
    # Initialize player board
    board = make_board(num_row=5, num_col=5)
    #
    # # Play intro text leading to level_1 text
    # print_scrolling_text('intro.txt')
    # print_from_text_file('ascii_bear.txt')
    # print_from_text_file('level_1.txt')

    # Initialize player information
    player = {'name': char_name,
              'location': (0, 0),
              'i-coord': 0,
              'j-coord': 0,
              'inventory': [],
              'hp': 25,
              'max_hp': 25,
              'attack': 5,
              'level': 1,
              'xp': 1000,
              'max_xp': 1000}

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
        # TODO: update second param for final
        print_map(board, 5, 5)

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
                print_from_text_file('goodbye.txt')
                quit()
            continue

        command = command_map[player_choice]
        # If player choice is not a movement command, execute the command
        if player_choice not in list(command_map.keys())[:4]:
            command(player)
            input('Press enter to continue...')
            continue

        # Check if player can move in the direction they chose
        valid_move = validate_move(player_choice, player['location'], board)
        if valid_move:
            # Change player location key to new location value
            player['location'] = command(player)
            continue

        time.sleep(1)
        # TODO: add random events and main game loop

        input('the end....')


def main():
    game()


if __name__ == '__main__':
    main()
