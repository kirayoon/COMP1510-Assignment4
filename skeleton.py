import random
# TODO: use itertools


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


# player_location is a tuple with i and j coordinates (row, col)
def get_player_choice(command_map: dict) -> str:
    choices = list(command_map.keys())
    player_choice = input('\nEnter the number or first letter of an option: ')

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


def check_event(board: dict, player_dict: dict, level_events: dict) -> None:
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


def egg(player_dict: dict):
    print('egg!')


def main():
    print('Please run game.py. This is a module.')


if __name__ == '__main__':
    main()
