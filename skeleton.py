import random
import json
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


def validate_yes_no(prompt: str) -> str:
    while True:
        choice = input(prompt).lower()
        try:
            choice = str(choice)
        except ValueError:
            print('\nPlease enter y or n.')
            continue
        if choice not in ('y', 'n'):
            print('\nPlease enter y or n.')
            continue
        else:
            break
    return choice


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
    choice = validate_yes_no('\n    Crack the egg? (y/n)')
    if choice == 'y':
        egg_select(player_dict)
        player_dict['inventory']['egg'] -= 1
    elif choice == 'n':
        print('egg left alone')


def egg_select(player_dict: dict):
    with open('egg.json') as file:
        egg_json = json.load(file)
    egg_dict = egg_json[random.choice(list(egg_json))]
    choice = validate_yes_no(f'''
        There's a little {egg_dict['name']} inside.
        {egg_dict['text']} (y/n)''')

    if choice == 'y':
        if egg_dict['name'] == 'chicky':
            player_dict['xp'] += egg_dict['xp']
            print(f'''
        How nice. You have gained {egg_dict["xp"]} xp.
        XP: {player_dict["xp"]}''')

        elif egg_dict['name'] == 'shard':
            player_dict['attack'] += egg_dict['attack']
            print(f'''
        You're stronger now. You gained {egg_dict["attack"]} attack points.
        Attack: {player_dict["attack"]}''')

        elif egg_dict['name'] == 'magic hat':
            player_dict['max_hp'] += egg_dict['max_hp']
            print(f'''
        You're healthier now. Your max-hp has been increased by {egg_dict["max_hp"]} points.
        Max HP: {player_dict["max_hp"]}''')

    elif choice == 'n' and egg_dict['name'] == 'chicky':
        player_dict['attack'] += egg_dict['attack']
        print(f'''
        You eat the chicky. It was delicious. You gained {egg_dict["attack"]} attack points.
        Attack: {player_dict["attack"]}''')

    else:
        print(f'''
        Your loss. The {egg_dict["name"]} evaporates into thin air.''')


def main():
    print('Please run game.py. This is a module.')


if __name__ == '__main__':
    main()
