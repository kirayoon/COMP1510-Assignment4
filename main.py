import os
import random
import time


def print_grid(board: list[list]) -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in range(10):
        print(" +---+---+---+---+---+---+---+---+---+---+")
        for col in range(10):
            print(" |", board[row][col], end="")
        print(' |', end="\n")
    print(" +---+---+---+---+---+---+---+---+---+---+")


def create_board() -> list[list]:
    return [[u"\u25A1" for _ in range(10)] for _ in range(10)]


# The next thing we do in the loop is ask the user where they wish to go. Create a function called
# get_user_choice. This function must print an enumerated list of directions and ask the user to enter
# the letter ot number corresponding to the direction they wish to travel, and return the direction.
# Choose a system and stick to it, i.e., North-East-South-West, or Up-Down-Left-Right. Don’t let me
# enter junk. If I enter something that is not a number from the list, make me choose again. Reject all
# user input that is not correct. Tell me to try again. And again. And again. Keep looping while my
# input is not correct. Also I hate typing, so make my choices single letter choices


# user_location is a tuple with i and j coordinates (row, col)
def get_user_choice() -> str:
    directions = enumerate(["Up", "Down", "Left", "Right"])
    print('', 'Type "quit" to quit the game, or "help" for help.', '', 'Directions:', sep='\n')
    for number, move in directions:
        print(f"{number + 1}: {move}")

    user_choice = input('Enter the number of the direction you wish to go: ')

    return user_choice


def check_user_choice(user_choice: str or int) -> str:
    valid_choices = ['up', 'down', 'left', 'right', 'quit', 'help']
    valid_numbers = ['1', '2', '3', '4']
    if user_choice in valid_numbers:
        return valid_choices[int(user_choice) - 1]

    elif user_choice in valid_choices:
        return user_choice

    else:
        print('', 'Invalid choice. Please try again.', sep='\n')
        return check_user_choice(get_user_choice())


# def move_player(user_choice: str, player_location: tuple, board: list[list]) -> tuple:
#     move_dictionary = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
#     player_location = tuple(map(sum, zip(player_location, move_dictionary[user_choice])))
#     if player_location in board:
#         print(f'Moving {user_choice}...')
#         time.sleep(1)
#         return player_location
#     else:


def main():
    board = create_board()
    user_location = (0, 0)

    game_is_won = False
    while not game_is_won:
        # Print the grid
        print_grid(board)

        # Get the user's move
        user_input = get_user_choice()
        valid_user_input = check_user_choice(user_input)

        # Quit the game if the user enters "quit"
        if valid_user_input == 'quit':
            if input("Are you sure you want to quit? (y/n): ").lower() == 'y':
                break
            continue

        # Print help if the user enters "help"
        if valid_user_input == 'help':
            print('''
            help documentation
            Type "quit" to quit the game, or "help" for help.
            ''')
            input('Press enter to continue...')
            continue

        # Move the player
        # move_player(valid_input, user_location, board)

        print(valid_user_input)
        input('reached the end')


if __name__ == '__main__':
    main()
