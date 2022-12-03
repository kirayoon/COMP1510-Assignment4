import os
import random
import time
from pathlib import Path


from levels import level_1, level_2, level_3, level_final


# TODO: use itertools


def print_map(board: dict, board_height: int, board_width: int, player_loc: tuple) -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    board_width = board_height
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


def make_board(num_row: int, num_col: int, current_level: int) -> dict:
    board_key = [(row, col) for row in range(num_row) for col in range(num_col)]
    board_values = []
    # TODO: Change for live
    level_events = {1: {'start': 1, 'event1': 10, 'event2': 5, 'event3': 3, 'event4': 3, 'egg': 3},
                    2: {'start': 1, 'event1': 5, 'event2': 3, 'event3': 10, 'event4': 3, 'egg': 3},
                    3: {'start': 1, 'event1': 7, 'event2': 3, 'event3': 3, 'event4': 3, 'event5': 5, 'egg': 3},
                    4: {'empty': 25}}
    for event, occurrence in level_events[current_level].items():
        board_values.extend([event] * occurrence)
    copy = board_values[2:]
    random.shuffle(copy)
    board_values[2:] = copy

    return dict(zip(board_key, board_values))


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


# player_location is a tuple with i and j coordinates (row, col)
def get_player_choice(command_map: dict) -> str:
    choices = list(command_map.keys())
    player_choice = input('Enter the number or first letter of an option: ')

    if player_choice.isdigit() and 1 <= int(player_choice) <= len(choices):
        return choices[int(player_choice) - 1]

    # TODO: see if this can be reformatted
    valid_choice = list(filter(lambda choice: choice.startswith(player_choice.lower()), choices))

    if len(valid_choice) != 1:
        print_out = '*** Invalid choice. Please try again. ***'
        print(f'\n{print_out:^47}\n')
        return get_player_choice(command_map)

    return valid_choice[0]


def validate_move(player_input: str, player_coordinate: tuple, board_width: int, board_height: int) -> bool:
    move_dictionary = {'up': player_coordinate[0] > 0,
                       'down': player_coordinate[0] < board_height - 1,
                       'left': player_coordinate[1] > 0,
                       'right': player_coordinate[1] < board_width - 1}
    return move_dictionary[player_input]


# Functions for each basic command
def up(player_location: tuple):
    return player_location[0] - 1, player_location[1]


def down(player_location: tuple):
    return player_location[0] + 1, player_location[1]


def left(player_location: tuple):
    return player_location[0], player_location[1] - 1


def right(player_location: tuple):
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
    print(f'\n{" " * 7}{player_dict[stats[0]].title()} the Scary Bear',
          f'{stats[3].title():>12}: {player_dict[stats[3]]:>2} '
          f'{stats[5].upper():>7}: {player_dict[stats[5]]}/{player_dict[stats[6]]}',
          f'{stats[4].title():>13}: {player_dict[stats[4]]} '
          f'{stats[1].upper():>7}: {player_dict[stats[1]]}/{player_dict[stats[2]]}\n', sep='\n')


def show_inventory(player_dict: dict):
    heading = "\033[4mInventory\033[0m"
    print(f'{heading:>25}')
    for count, (item, amount) in enumerate(player_dict['inventory'].items()):
        print(f'\t{count}) {item}: {amount}')

    choose_item(player_dict)


def choose_item(player_dict: dict):
    choice = input('Type the number of a item you want to use or press enter to continue: ')
    if choice == '':
        return
    elif choice.isalpha() or len(player_dict['inventory']) < int(choice):
        print_out = '*** Invalid choice. Please try again. ***'
        print(f'\n{print_out:^47}\n')
        choose_item(player_dict)

    else:
        item = list(player_dict['inventory'].keys())[int(choice)]
        print(f'You chose {item}.\n')
        time.sleep(1)
        use_item(player_dict, choice)
    pass


def use_item(player_dict: dict, choice: str):
    item = list(player_dict['inventory'].keys())[int(choice)]
    # TODO: make dictionary of items and their effects
    if item == 'fish':
        player_dict['hp'] += 5
        if player_dict['hp'] > player_dict['max_hp']:
            player_dict['hp'] = player_dict['max_hp']
        print(f'You eat the fish and feel better. Your health is now {player_dict["hp"]}.\n')
        player_dict['inventory'][item] -= 1
    elif item == 'rabbit':
        player_dict['hp'] += 10
        if player_dict['hp'] > player_dict['max_hp']:
            player_dict['hp'] = player_dict['max_hp']
        print(f'You eat the rabbit and feel better. Your health is now {player_dict["hp"]}.\n')
        player_dict['inventory'][item] -= 1
    elif item == 'deer':
        player_dict['hp'] += 25
        if player_dict['hp'] > player_dict['max_hp']:
            player_dict['hp'] = player_dict['max_hp']
        print(f'You eat the deer and feel better. Your health is now {player_dict["hp"]}.\n')
        player_dict['inventory'][item] -= 1
    pass


def level_up(player_dict: dict):
    answer = input('\nWould you like to move to the next level (y/n)?: ').lower()
    if answer == 'y':
        player_dict['level'] += 1
        player_dict['xp'] = 0
        player_dict['max_hp'] += 20
        player_dict['hp'] = player_dict['max_hp']
        player_dict['attack'] += 10
        player_dict['turn'] = 1
        player_dict['location'] = (0, 0)
        print('\nYou have leveled up, and moved onto the next zone')
        print(f'You are now level {player_dict["level"]}')
        input('Press enter to continue...')


def check_event(board: dict, player_dict: dict, level_events: dict) -> None:
    location = player_dict['location']
    current_event = board[location]
    if current_event == 'clear':
        print('You have already been here. Try a different spot.')
        input('Press enter to continue... ')
    else:
        # Clear the event from the board
        board[location] = 'clear'
        event_func = level_events[current_event]
        event_func(player_dict)


def egg(player_dict: dict):
    print('egg!')



def main():
    """
    Drive the program.
    """
    game()


if __name__ == '__main__':
    main()
