import os
import random
import time
from pathlib import Path


from levels import level_1, level_2, level_3, level_final


# TODO: use itertools


def print_map(board: dict, board_height: int, board_width: int) -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    board_width = board_height
    for row in range(board_height):
        print("  +-------+-------+-------+-------+-------+")
        for col in range(board_width):
            print("  | ", '(!)' if board[(row, col)] == 'event2' else "   ", end="")
        print('  |', end="\n")
    print("  +-------+-------+-------+-------+-------+")


def make_board(num_row: int, num_col: int, current_level: int) -> dict:
    board_key = [(row, col) for row in range(num_row) for col in range(num_col)]
    board_values = []
    # TODO: Change for live
    level_events = {1: {'start': 1, 'event1': 10, 'event2': 5, 'event3': 3, 'event4': 3, 'egg': 3},
                    2: {'start': 1, 'event1': 8, 'event2': 3, 'event3': 10, 'egg': 3},
                    3: {'start': 1, 'event1': 4, 'event2': 3, 'event3': 1, 'event4': 16},
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

    if player_choice.isdigit() and 1 <= int(player_choice) <= 9:
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
        player_dict['max_xp'] += 10
        player_dict['xp'] = 0
        player_dict['max_hp'] += 25
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


def egg():
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
    board_height = 5
    board_width = 5
    board = dict()

    # # Play intro text leading to level_1 text
    # print_scrolling_text('intro.txt')
    # print_from_text_file('ascii_bear.txt')
    # print_from_text_file('level_1.txt')

    # Initialize player information
    player = {'name': char_name,
              'location': (0, 0),
              'i-coord': 0,
              'j-coord': 0,
              'inventory': {'rabbit': 3, 'deer': 1},
              'hp': 25,
              'max_hp': 25,
              'attack': 10,
              'level': 1,
              'xp': 0,
              'max_xp': 1000,
              'turn': 1}

    command_map = {'up': up,
                   'down': down,
                   'left': left,
                   'right': right,
                   'sleep': player_sleep,
                   'player': player_information,
                   'inventory': show_inventory,
                   'help': '',
                   'quit': ''}
    event_dict = {}

    game_is_won = False
    while not game_is_won:
        if player['turn'] == 1:
            board = make_board(board_height, board_width, player['level'])

        # Print the grid
        # TODO: update second param for final
        print(player['location'])
        print_map(board, board_height, board_width)

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
            print_from_text_file('help.txt')
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
        valid_move = validate_move(player_choice, player['location'], board_height, board_width)
        print(f'Walking {player_choice}...')
        time.sleep(1)
        if valid_move:
            # Change player location key to new location value
            player['location'] = command(player['location'])
        else:
            print(f'*** You cannot move {player_choice}. Please try again. ***')
            input('Press enter to continue...')
            continue
        time.sleep(1)
        # TODO: add random events and main game loop

        # Set events for a players' level
        if player['level'] == 1:
            event_dict = {'event1': level_1.default,
                          'event2': level_1.fish,
                          'event3': level_1.slippery_rock,
                          'event4': level_1.heavy_current,
                          'egg': egg}
        elif player['level'] == 2:
            event_dict = {'event1': level_2.default,
                          'event2': level_2.soup,
                          'event3': level_2.scraps,
                          'event4': level_2.egg}
        elif player['level'] == 3:
            event_dict = {}

        # Check if there is an event at the player's location
        check_event(board, player, event_dict)

        input('the end....')
        level_up(player) if player['xp'] >= player['max_xp'] else None
        player['turn'] += 1


def main():
    """
    Drive the program.
    """
    game()


if __name__ == '__main__':
    main()
