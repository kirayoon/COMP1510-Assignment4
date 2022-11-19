import os
import random
import time
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


# The next thing we do in the loop is ask the user where they wish to go. Create a function called
# get_user_choice. This function must print an enumerated list of directions and ask the user to enter
# the letter ot number corresponding to the direction they wish to travel, and return the direction.
# Choose a system and stick to it, i.e., North-East-South-West, or Up-Down-Left-Right. Don’t let me
# enter junk. If I enter something that is not a number from the list, make me choose again. Reject all
# user input that is not correct. Tell me to try again. And again. And again. Keep looping while my
# input is not correct. Also I hate typing, so make my choices single letter choices


# user_location is a tuple with i and j coordinates (row, col)
def get_user_choice() -> str:
    valid_directions = ['Up', 'Down', 'Left', 'Right', 'Help', 'Quit']
    print('', 'OPTIONS', sep='\n')
    for number, move in enumerate(valid_directions, start=1):
        print(f"{number}: {move}")

    print('')
    user_choice = input('Enter the number or first letter of an action: ')

    if user_choice.isdigit() and 1 <= int(user_choice) <= 6:
        return valid_directions[int(user_choice) - 1]

    # TODO: see if this can be reformatted
    valid_choice = list(filter(lambda x: x.startswith(user_choice.upper()), valid_directions))
    if len(valid_choice) == 1:
        return valid_choice[0]

    print('', 'Invalid choice. Please try again.', sep='\n')
    return get_user_choice()


def validate_move(direction: str, player_location: tuple, board: list[list]) -> tuple or bool:
    move_dictionary = {'Up': (-1, 0), 'Down': (1, 0), 'Left': (0, -1), 'Right': (0, 1)}
    new_location = tuple(map(sum, zip(player_location, move_dictionary[direction])))

    if new_location[0] in range(len(board)) and new_location[1] in range(len(board)):
        return new_location

    return None


def game():
    # TODO: store ascii art in a file
    print('+~~~~~~~~~~~~~~~~~~~~~~~~+',
          '| Assignment 4: The Game |',
          '| Joseph Chun, Kira Yoon |',
          '+~~~~~~~~~~~~~~~~~~~~~~~~+', sep='\n')
    time.sleep(5)

    board = make_board(row=10, col=10)
    # Put user location inside make user function
    # TODO: store user location in dictionary as x and y not tuple?
    user_location = (0, 9)

    game_is_won = False
    while not game_is_won:
        # Print the grid
        print_grid(board)

        # Need function to describe board

        # Get the user's move
        direction = get_user_choice()

        # Quit the game if the user enters "quit"
        if direction == 'Quit':
            print()
            if input("Are you sure you want to quit? (y/n): ").lower() == 'y':
                # TODO: store ascii art in a file
                print('',
                      '+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+',
                      '|   ____               ____ _          _     _  |',
                      '|  / ___|   _  __ _   / ___| |__  _ __(_)___| | |',
                      '| | |  | | | |/ _` | | |   | \'_ \| \'__| / __| | |',
                      '| | |__| |_| | (_| | | |___| | | | |  | \__ \_| |',
                      '|  \____\__, |\__,_|  \____|_| |_|_|  |_|___(_) |',
                      '|       |___/                                   |',
                      '+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+', sep='\n')

                break
            continue

        # Print help if the user enters "help"
        if direction == 'Help':
            # TODO: create help documentation
            print('''
            help documentation
            Type "quit" to quit the game, or "help" for help.
            ''')
            input('Press enter to continue...')
            continue

        # Validate movement
        valid_move = validate_move(direction, user_location, board)
        print(valid_move)
        if valid_move:
            user_location = valid_move
            print(f'Walking {direction.lower()}...')

        else:
            print(f'Walking {direction.lower()}...')
            time.sleep(1)
            print('', 'Bam! You smacked your nose on a wall. Please try again.', '', sep='\n')
            input('Press enter to continue...')
            continue

        time.sleep(1)
        # TODO: add random events and main game loop

        input('the end....')


def main():
    game()


if __name__ == '__main__':
    main()
