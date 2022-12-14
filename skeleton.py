import random
import winsound


def create_player(player_name: str) -> dict:
    """
    Create a dictionary for important player information

    :param player_name: string representing the player's name
    :precondition: player_name must be a string
    :postcondition: creates a dictionary
    :return: a dictionary containing player information
    """
    return {'name': player_name,
            'location': (0, 0),
            'inventory': {},
            'hp': 20,
            'max_hp': 20,
            'attack': 10,
            'level': 1,
            'xp': 0,
            'max_xp': 1000,
            'turn': 1,
            'attacks': {'claw': 1, 'bite': 2, 'charge': 3},
            'deaths': 0,
            'kills': 0,
            'damage_dealt': 0,
            'eggs_found': 0,
            'useless_events': 0,
            'soup_counter': 0,
            'chair_counter': 0}


def make_board(num_row: int, num_col: int, current_level: int) -> dict:
    """
    Create a dictionary with keys as tuples of coordinates and values as strings of events at those coordinates.

    :param num_row: integer representing number of rows in board
    :param num_col: integer representing number of columns in board
    :param current_level: integer representing player's current level
    :precondition: num_row must be an integer greater than 0
    :precondition: num_col must be an integer greater than 0
    :precondition: current_level must be an integer between [1, 4]
    :postcondition: creates a dictionary
    :postcondition: keys are tuples of integers representing the coordinates
    :postcondition: values are strings representing the events at those coordinates
    :postcondition: keys are paired with random values
    :return: dictionary with keys as tuples of coordinates and values as strings of events at those coordinates

    Too difficult to test.
    """
    board_key = [(row, col) for row in range(num_row) for col in range(num_col)]
    board_values = []
    level_events = {1: {'start': 1, 'event1': 10, 'event2': 5, 'event3': 3, 'event4': 3, 'egg': 3},
                    2: {'start': 1, 'event1': 5, 'event2': 3, 'event3': 10, 'event4': 3, 'egg': 3},
                    3: {'start': 1, 'event1': 5, 'event2': 5, 'event3': 4, 'event4': 4, 'event5': 3, 'egg': 3},
                    4: {'clear': 25}}
    for event, occurrence in level_events[current_level].items():
        board_values.extend([event] * occurrence)
    copy = board_values[1:]
    random.shuffle(copy)
    board_values[1:] = copy

    board_dict = dict(zip(board_key, board_values))
    return board_dict


def get_player_choice(command_map: dict) -> str:
    """
    Get player's choice of command.

    :param command_map: a dictionary containing the commands and their corresponding functions
    :precondition: command_map must be a dictionary
    :precondition: keys must be strings
    :postcondition: player's choice is validated
    :return: a string representing the player's choice of command

    Testing callback is outside of scope. Only tested with valid input.
    """
    choices = list(command_map.keys())
    player_choice = input('\nEnter the number or first letter of an option: ')

    if player_choice.isdigit() and 1 <= int(player_choice) <= len(choices):
        return choices[int(player_choice) - 1]

    valid_choice = list(filter(lambda choice: choice.startswith(player_choice.lower()), choices))

    if len(valid_choice) != 1:
        print(f'''
        *** Invalid choice. Please try again. ***
        ''')
        return get_player_choice(command_map)

    return valid_choice[0]


def validate_yes_no(prompt: str) -> str:
    """
    Validate user input for yes or no.

    Input is valid if it is 'y', 'Y', 'n', or 'N'.

    :param prompt: string representing the prompt to the user
    :precondition: prompt must be a string
    :postcondition: user input is validated
    :return: 'y' or 'n'

    Too difficult to test.
    """
    while True:
        choice = input(prompt + ':  ').lower()
        if choice not in ('y', 'n'):
            print('\nPlease enter y or n.')
            continue
        else:
            break
    return choice


def validate_move(player_input: str, player_coordinate: tuple, board_width: int, board_height: int) -> bool:
    """
    Validate player input for movement.

    Input is valid if movement is in the range of the board.

    :param player_input: string representing the player's input
    :param player_coordinate: tuple representing the player's current location
    :param board_width: integer representing the width of the board
    :param board_height: integer representing the height of the board
    :precondition: player_input must be a string 'up', 'down', 'left', or 'right'
    :precondition: player_coordinate must be a tuple of integers
    :precondition: board_width must be an integer greater than 0
    :precondition: board_height must be an integer greater than 0
    :postcondition: player's move is validated
    :return: True if player's input for movement is valid, False otherwise
    """
    move_dictionary = {'up': player_coordinate[0] > 0,
                       'down': player_coordinate[0] < board_height - 1,
                       'left': player_coordinate[1] > 0,
                       'right': player_coordinate[1] < board_width - 1}
    return move_dictionary[player_input]


# Functions for each basic command
def up(player_location: tuple):
    """
    Move player up one space.

    :param player_location: a tuple containing the x and y coordinates of the player
    :precondition: player_location must be a tuple of integers
    :precondition: integers must be >= 0
    :postcondition: player_location is moved down one space
    :return: a tuple containing new x and y coordinates of the player

    >>> up((2, 0))
    (1, 0)
    >>> up((4, 4))
    (3, 4)
    """
    return player_location[0] - 1, player_location[1]


def down(player_location: tuple):
    """
    Move player down one space.

    :param player_location: a tuple containing the x and y coordinates of the player
    :precondition: player_location must be a tuple of integers
    :precondition: integers must be >= 0
    :postcondition: player_location is moved down one space
    :return: a tuple containing new x and y coordinates of the player

    >>> down((2, 0))
    (3, 0)
    >>> down((3, 4))
    (4, 4)
    """
    return player_location[0] + 1, player_location[1]


def left(player_location: tuple):
    """
    Move player left one space.

    :param player_location: a tuple containing the x and y coordinates of the player
    :precondition: player_location must be a tuple of integers
    :precondition: integers must be >= 0
    :postcondition: player_location is moved down one space
    :return: a tuple containing new x and y coordinates of the player

    >>> left((2, 1))
    (2, 0)
    >>> left((3, 4))
    (3, 3)
    """
    return player_location[0], player_location[1] - 1


def right(player_location: tuple):
    """
    Move player left one space.

    :param player_location: a tuple containing the x and y coordinates of the player
    :precondition: player_location must be a tuple of integers
    :precondition: integers must be >= 0
    :postcondition: player_location is moved down one space
    :return: a tuple containing new x and y coordinates of the player

    >>> right((2, 1))
    (2, 2)
    >>> right((3, 3))
    (3, 4)
    """
    return player_location[0], player_location[1] + 1


def check_event(board: dict, player_dict: dict, level_events: dict) -> None:
    """
    Check if player is on an event space.

    :param board: a dictionary containing the board
    :param player_dict: a dictionary containing the player's information
    :param level_events: a dictionary containing the events for the current level
    :precondition: parameters must be dictionaries
    :precondition: board must have tuples for keys corresponding to the board's x and y coordinates
    :precondition: board must have strings for values corresponding to level_events keys
    :precondition: player_dict must have strings for keys corresponding to the functions in level_events
    :precondition: level_events must have strings for keys corresponding to the events for the current level
    :precondition: level_events must have functions for values
    :postcondition: player's event is executed
    :postcondition: player's event is removed from the board
    :postcondition: player_dict is updated

    Too difficult to test.
    """
    location = player_dict['location']
    current_event = board[location]
    if current_event == 'clear':
        print('\nYou have already been here. Try a different spot.')
    elif current_event == 'start':
        print('\nYou started here! Why are you back?')
    else:
        # Clear the event from the board
        board[location] = 'clear'
        event_func = level_events[current_event]
        event_func(player_dict)


def egg(player_dict: dict) -> None:
    """
    Add an egg to the player's inventory.

    :param player_dict: a dictionary containing the player's information
    :precondition: player_dict must be a dictionary
    :precondition: player_dict must have a key 'inventory' with a list as a value
    :postcondition: player_dict['egg'] is incremented by 1
    """
    player_dict['eggs_found'] += 1
    if 'egg' in player_dict['inventory']:
        print('\nYou found another egg! \nIt has been added to your inventory.')
        player_dict['inventory']['egg'] += 1
    else:
        print('\nYou found a mysterious egg! \nEgg has been added to your inventory.')
        player_dict['inventory']['egg'] = 1


def level_up_sound() -> None:
    """
    Play the sound for when the player levels up.

    :postcondition: level up sound is played
    """
    start_frequency = 600
    end_frequency = 1000
    duration = 50
    while start_frequency <= end_frequency:
        winsound.Beep(start_frequency, duration)
        start_frequency += 100


def main():
    """
    Drive the program
    """
    print('Please run game.py. This is a module.')


if __name__ == '__main__':
    main()
