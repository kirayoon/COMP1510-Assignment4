import time


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