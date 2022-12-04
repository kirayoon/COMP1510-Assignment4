"""
This module contains functions that are responsible for the player to interact with the game.
"""


import time
import json
import random
from pathlib import Path
from printer import print_scrolling_text
from skeleton import validate_yes_no


def player_sleep(player_dict: dict) -> None:
    """
    Recover to max hp after waiting 3 seconds.

    :param player_dict: dictionary of player stats
    :precondition: player_dict must be a dictionary containing 'hp' and 'max_hp' keys
    :precondition: player_dict['hp'] and player_dict['max_hp'] must be positive integers
    :postcondition: recover to max hp after waiting 3 seconds
    :postcondition: player_dict['hp'] will be set to player_dict['max_hp']
    """
    player_dict['hp'] = player_dict['max_hp']
    print('''
    You sleep under the stars and dreamt of being full. 
    What a good night.
    ''')
    time.sleep(1)
    print('\tzzz....')
    time.sleep(1)
    print('\tzzz....zzz......')
    time.sleep(1)
    print(f'''
    Your health has recovered to {player_dict["max_hp"]}.''')


def player_information(player_dict: dict) -> None:
    """
    Print out the player's information.

    :param player_dict: dictionary of player stats
    :precondition: player_dict must be a dictionary
    :precondition: player_dict must contain 'name', 'hp', 'max_hp', 'level', 'attack', 'xp', and 'max_xp' keys
    :precondition: value of 'name' must be a string
    :precondition: values of 'hp', 'max_hp', 'level', 'attack', 'xp', and 'max_xp' must be positive integers
    :postcondition: print out the player's information in a formatted way
    """
    stats = ['name', 'hp', 'max_hp', 'level', 'attack', 'xp', 'max_xp']
    print(f'\n{" " * 7}{player_dict[stats[0]].title()} the Scary Bear',
          f'{stats[3].title():>12}: {player_dict[stats[3]]:>2} '
          f'{stats[5].upper():>7}: {player_dict[stats[5]]}/{player_dict[stats[6]]}',
          f'{stats[4].title():>13}: {player_dict[stats[4]]} '
          f'{stats[1].upper():>7}: {player_dict[stats[1]]}/{player_dict[stats[2]]}\n', sep='\n')


def show_inventory(player_dict: dict) -> None:
    """
    Print out the player's inventory if inventory is not empty.

    :param player_dict: dictionary of player stats
    :precondition: player_dict must be a dictionary containing 'inventory' key
    :precondition: player_dict['inventory'] must be a dictionary
    :postcondition: print out a special message if the player's inventory is empty
    :postcondition: print out the player's inventory in a formatted way if the player's inventory is not empty
    :postcondition: printed inventory includes item name, quantity, and possible effects
    :postcondition: execute choose_item function if the player's inventory is not empty
    """
    with open(Path('json/') / 'items.json') as file:
        item_json = json.load(file)
    player_inventory = player_dict['inventory'].items()
    heading = "\033[4mInventory\033[0m"
    print(f'\n{heading:>25}')
    if len(player_inventory) == 0:
        print('\tnothing here\n')
    else:
        for count, (item, amount) in enumerate(player_inventory):
            item_dict = item_json[item]
            if 'hp' in item_dict:
                print(f'\t{count}) {item}: {amount} [+{item_dict["hp"]} hp]')
            else:
                print(f'\t{count}) {item}: {amount} [{item_dict["?"]}]')

        choose_item(player_dict)


def choose_item(player_dict: dict):
    """
    Execute the use_item or use_egg function if the player chooses to use a valid item or the egg.

    :param player_dict: dictionary of player stats
    :precondition: player_dict must be a dictionary containing 'inventory' key
    :precondition: player_dict['inventory'] must be a dictionary containing at least one item
    :postcondition: exits the inventory menu if the player's input is an empty string
    :postcondition: prints out a special message if the player chooses an invalid item and execute the function again
    :postcondition: executes use_item function if the player chooses to use a valid item
    :postcondition: executes use_egg function if the player chooses to use the egg
    :postcondition: deletes the item from the player's inventory if the item's quantity is 0
    """
    choice = input('\nType the number of a item you want to use or press enter to continue: ')
    if choice == '':
        return
    elif choice.isalpha() or len(player_dict['inventory']) - 1 < int(choice):
        print_out = '*** Invalid choice. Please try again. ***'
        print(f'\n{print_out:^47}\n')
        choose_item(player_dict)
    else:
        item = list(player_dict['inventory'].keys())[int(choice)]
        print(f'You chose {item}.\n')
        if item == 'egg':
            use_egg(player_dict)
        else:
            use_item(player_dict, item)

        if player_dict['inventory'][item] == 0:
            del player_dict['inventory'][item]


def use_item(player_dict: dict, item: str) -> None:
    """
    Apply the item's effect to the player.

    Item effects are stored in items.json and are hp gains.

    :param player_dict: dictionary of player stats
    :param item: chosen item to use as a string
    :precondition: player_dict must be a dictionary containing 'hp', 'max_hp', and 'inventory' keys
    :precondition: player_dict['hp'] and player_dict['max_hp'] must be positive integers
    :precondition: player_dict['inventory'] must be a dictionary containing at least one item
    :precondition: item must be a string that is a key in player_dict['inventory']
    :postcondition: adds the item's hp gain to the player's hp
    :postcondition: sets player's hp to max_hp if the item's hp gain is greater than the player's missing hp
    :postcondition: subtracts one from the item's quantity in the player's inventory
    """
    with open(Path('json/') / 'items.json') as file:
        item_json = json.load(file)
    item_dict = item_json[item]

    player_dict['hp'] += item_dict['hp']
    if player_dict['hp'] > player_dict['max_hp']:
        player_dict['hp'] = player_dict['max_hp']
    print(f'You eat the {item} and gain {item_dict["hp"]} hp. Your health is now {player_dict["hp"]}.\n')
    player_dict['inventory'][item] -= 1


def use_egg(player_dict: dict) -> None:
    """
    Execute the hatch_egg function if the player chooses to use the egg.

    :param player_dict: dictionary of player stats
    :precondition: player_dict must be a dictionary containing 'inventory' key
    :precondition: player_dict['inventory'] must be a dictionary containing 'egg' key
    :postcondition: executes hatch_egg function if the player chooses to hatch the egg
    :postcondition: subtracts one egg from the player's inventory if the player hatches the egg
    :postcondition: exit the inventory menu if the player chooses not to hatch the egg
    """
    choice = validate_yes_no('\n    Crack the egg? (y/n)')
    if choice == 'y':
        hatch_egg(player_dict)
        player_dict['inventory']['egg'] -= 1
    elif choice == 'n':
        print('''
        You leave the egg alone.''')


def hatch_egg(player_dict: dict) -> None:
    """
    Add random stats to the player's stats.

    :param player_dict: dictionary of player stats
    :precondition: player_dict must be a dictionary
    :precondition: player_dict must contain 'xp', 'attack', and 'max_hp' keys
    :precondition: values of 'xp', 'attack', and 'max_hp' must be positive integers
    :precondition: egg.json must be a valid json file containing a list of dictionaries
    :precondition: egg.json must contain dictionaries with 'name' and 'text' keys
    :precondition: egg.json must contain dictionaries with possible items hatched from the egg and their effects
    :postcondition: chooses a random dictionary of hatched item from egg.json
    :postcondition: applies the hatched item's effect to the player
    """
    with open(Path('json/') / 'egg.json') as file:
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
        XP: {player_dict["xp"]}
        ''')

        elif egg_dict['name'] == 'shard':
            player_dict['attack'] += egg_dict['attack']
            print(f'''
        You're stronger now. You gained {egg_dict["attack"]} attack points.
        Attack: {player_dict["attack"]}
        ''')

        elif egg_dict['name'] == 'magic hat':
            player_dict['max_hp'] += egg_dict['max_hp']
            print(f'''
        You're healthier now. Your max-hp has been increased by {egg_dict["max_hp"]} points.
        Max HP: {player_dict["max_hp"]}
        ''')

    elif choice == 'n' and egg_dict['name'] == 'chicky':
        player_dict['attack'] += egg_dict['attack']
        print(f'''
        You eat the chicky. It was delicious. You gained {egg_dict["attack"]} attack points.
        Attack: {player_dict["attack"]}
        ''')

    else:
        print(f'''
        Your loss. The {egg_dict["name"]} evaporates into thin air.''')


def level_up(player_dict: dict) -> None:
    """
    Increase the player's level and stats if the player chooses to level up.

    :param player_dict: dictionary of player stats
    :precondition: player_dict must be a dictionary
    :precondition: player_dict must contain 'level', 'xp', 'max_hp', 'hp', 'attack', 'turn', and 'location' keys
    :precondition: values of 'level', 'xp', 'max_hp', 'hp', 'attack', and 'turn' must be positive integers
    :precondition: values of 'location' must be a tuple of two positive integers
    :postcondition: increases the player's level by 1, max_hp by 20, and attack by 10
    :postcondition: sets the player's hp to max_hp, xp to 0, turn to 0, and location to (0, 0)
    :postcondition: prints the player's new stats
    :postcondition: prints the intro text for the new level
    """
    print("\nYou're ready to level up.")
    answer = validate_yes_no('Would you like to move to the next level (y/n)?')
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
        player_information(player_dict)
        input('Press enter to continue...')
        if player_dict['level'] == 2:
            print_scrolling_text('level_2.txt')
        elif player_dict['level'] == 3:
            print_scrolling_text('level_3.txt')
        elif player_dict['level'] == 4:
            print_scrolling_text('level_final.txt')


def main():
    print('Please run game.py. This is a module.')


if __name__ == '__main__':
    main()
