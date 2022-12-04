import time
import json
import random
from printer import print_scrolling_text
from skeleton import validate_yes_no


def player_sleep(player_dict: dict):
    player_dict['hp'] = player_dict['max_hp']
    print(f'''
    You sleep under the stars and dreamt of being full. 
    What a good night.

    Your health has recovered to {player_dict["max_hp"]}.
    ''')


def player_information(player_dict: dict):
    stats = ['name', 'hp', 'max_hp', 'level', 'attack', 'xp', 'max_xp']
    print(f'\n{" " * 7}{player_dict[stats[0]].title()} the Scary Bear',
          f'{stats[3].title():>12}: {player_dict[stats[3]]:>2} '
          f'{stats[5].upper():>7}: {player_dict[stats[5]]}/{player_dict[stats[6]]}',
          f'{stats[4].title():>13}: {player_dict[stats[4]]} '
          f'{stats[1].upper():>7}: {player_dict[stats[1]]}/{player_dict[stats[2]]}\n', sep='\n')


def show_inventory(player_dict: dict):
    with open('items.json') as file:
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


def use_item(player_dict: dict, item: str):
    with open('items.json') as file:
        item_json = json.load(file)
    item_dict = item_json[item]

    player_dict['hp'] += item_dict['hp']
    if player_dict['hp'] > player_dict['max_hp']:
        player_dict['hp'] = player_dict['max_hp']
    print(f'You eat the {item} and gain {item_dict["hp"]} hp. Your health is now {player_dict["hp"]}.\n')
    player_dict['inventory'][item] -= 1


def use_egg(player_dict: dict):
    choice = validate_yes_no('\n    Crack the egg? (y/n)')
    if choice == 'y':
        egg_select(player_dict)
        player_dict['inventory']['egg'] -= 1
    elif choice == 'n':
        print('''
        You leave the egg alone.''')


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


def level_up(player_dict: dict):
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
