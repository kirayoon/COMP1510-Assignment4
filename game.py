import time
from levels import level_1, level_2, level_3
from skeleton import make_board, get_player_choice, validate_move, up, down, left, right, egg, check_event, \
    create_player
from player import player_sleep, player_information, show_inventory, level_up
from printer import print_map, print_scrolling_text, print_from_text_file, print_choices_menu
from fight import death_sequence, final_boss_loop, final_boss_defeated


def game():
    start_time = time.time()

    # Print the title screen
    print_from_text_file('title_screen.txt')
    char_name = input('Please input your character\'s name: ')
    print(f'\nHello {char_name}! Welcome to the game!')

    # Initialize player information
    player = create_player(char_name)
    time.sleep(1)

    # Initialize player board
    board_height = 5
    board_width = 5
    board = dict()

    # Play intro text leading to level_1 text
    print_scrolling_text('intro.txt')
    print_from_text_file('ascii_bear.txt')
    print_from_text_file('level_1.txt')

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

        # check if player is dead
        death_sequence(player) if player['hp'] <= 0 else None

        # Print the grid
        print_map(board, board_height, board_width, player)

        # Need function to describe room

        # Print player choices menu and get player's choice
        print_choices_menu(command_map)
        player_choice = get_player_choice(command_map)

        # Print help if the player enters "help"
        if player_choice == 'help':
            print('''
            help documentation
            ''')
            print_from_text_file('help.txt')
            player['turn'] += 1
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
            player['turn'] += 1
            continue

        # Check if player can move in the direction they chose
        valid_move = validate_move(player_choice, player['location'], board_height, board_width)
        print(f'''
        Walking {player_choice}...
        ''')
        if valid_move:
            # Change player location key to new location value
            player['location'] = command(player['location'])
        else:
            print(f'''
            *** You cannot move {player_choice}. Please try again. ***
            ''')
            input('Press enter to continue...')
            continue
        time.sleep(0.5)


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
                          'event4': level_2.chair,
                          'egg': egg}
        elif player['level'] == 3:
            event_dict = {'event1': level_3.default,
                          'event2': level_3.deer,
                          'event3': level_3.berry,
                          'event4': level_3.nut,
                          'event5': level_3.mushroom,
                          'egg': egg}

        # Check if there is an event at the player's location
        check_event(board, player, event_dict)
        level_up(player) if player['xp'] >= player['max_xp'] else None
        player['turn'] += 1
        if player['level'] == 4:
            final_boss_loop(player, 'mama')
            game_is_won = True

        input('\n\nPress enter to continue...')

    end_time = time.time()
    total_time = end_time - start_time
    final_boss_defeated(player, total_time)


def main():
    """
    Drive the program
    """
    game()


if __name__ == '__main__':
    main()
