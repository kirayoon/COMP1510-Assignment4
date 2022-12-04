import random
from skeleton import make_board
import json
import os
from printer import print_health, print_enemy_picture


# def randomize_boss_movement(current_boss_location: tuple, board_width: int, board_height: int) -> tuple:
#     pass


def print_map(board: dict, board_height: int, board_width: int, player_loc: tuple, boss_loc=None) -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in range(board_height):
        print('  +-------+-------+-------+-------+-------+')
        print('  ', end='')
        for col in range(board_width):
            if board[(row, col)] == 'event2':
                print('|  (!)  ', end='')
            elif (row, col) == player_loc:
                print('|ʕ•`ᴥ´•ʔ', end='')
            elif (row, col) == boss_loc:
                print('| •`_´• ', end='')
            elif board[(row, col)] == 'clear' or board[(row, col)] == 'start':
                print('|       ', end='')
            else:
                print('|   ?   ', end='')
        print('|', end='\n')
    print('  +-------+-------+-------+-------+-------+')


def load_enemy(enemy: str) -> dict:
    with open('..\\enemy.json') as file:
        enemy_json = json.load(file)
    return enemy_json[enemy]


class Boss:
    def __init__(self, enemy_dict: dict):
        self.location = (2, 2)
        self.hp = 100
        self.max_hp = 100
        self.attack = 10
        self.name = 'Mama Lob'
        self.abilities = enemy_dict['abilities']
        self.ability_names = list(enemy_dict['abilities'].keys())
        self.shot_count = 3
        # self.board_width = board_width
        # self.board_height = board_height

    # test
    def remove_hp(self):
        self.hp -= 20

    def get_hp(self):
        return self.hp

    def get_location(self):
        return self.location

    def get_stats(self):
        return {'hp': self.hp, 'max_hp': self.max_hp, 'name': self.name}

    def choose_move_randomly(self, player_dict) -> str:
        current_move = random.choice(self.ability_names)
        eval(f'self.{current_move}')(player_dict)

    def shoot(self, player_dict) -> None:
        accuracy = 60
        if random.randint(1, 100) <= accuracy:
            self.shot_count -= 1
            print(f'''
        {self.abilities["shoot"]["flavour_text"]}
        It does {self.abilities["shoot"]["damage"]} damage!
        
        Mama Lob has {self.shot_count} shot(s) left!
        ''')
            # return self.abilities['shoot']['damage']
            player_dict['hp'] -= self.abilities['shoot']['damage']
        else:
            print(f'''
            {self.abilities["shoot"]["flavour_text_miss"]} 
            ''')
            player_dict['hp'] -= 0

    def bomb(self, player_dict: dict) -> None:
        min_damage = int(self.abilities['bomb']['damage'] / 2)
        max_damage = self.abilities['bomb']['damage']
        damage = random.randint(min_damage, max_damage)
        print(f'''
        {self.abilities["bomb"]["flavour_text"]} 
        It does {damage} damage!
        ''')
        player_dict['hp'] -= damage

    def move(self, player_dict: dict) -> None:
        x_direction = random.randint(-1, 1)
        y_direction = random.randint(-1, 1)
        player_loc = player_dict['location']
        new_location = (self.location[0] + x_direction, self.location[1] + y_direction)
        if 0 <= new_location[0] <= 4 and 0 <= new_location[1] <= 4 and new_location != player_loc:
            self.location = new_location
            print(f'''{self.abilities['move']['flavour_text']}''')
        else:
            self.move(player_dict)

    # def randomize_attack(self):


def main():
    player = {'name': 'abc',
              'location': (0, 0),
              'i-coord': 0,
              'j-coord': 0,
              'inventory': {'fish': 3, 'deer': 1, 'honey': 2, 'egg': 2},
              'hp': 20,
              'max_hp': 20,
              'attack': 5,
              'level': 4,
              'xp': 0,
              'max_xp': 1000,
              'turn': 1}
    board = make_board(5, 5, 4)
    boss = Boss(load_enemy('mama'))

    while boss.get_hp() > 0:
        print_map(board, 5, 5, player['location'], boss.get_location())
        # boss.do_damage(player)
        # boss_move = boss.choose_move_randomly()
        # if boss_move == 'shoot':
        #     damage = boss.shoot()
        #     player['hp'] -= damage
        #     print_health(player, boss.get_stats())
        # elif boss_move == 'bomb':
        #     boss.bomb(player)
        #     print_health(player, boss.get_stats())
        # else:
        #     boss.move(player)

        # boss.eval_bomb(player)
        boss.choose_move_randomly(player)
        print_health(player, boss.get_stats())
        boss.remove_hp()



if __name__ == '__main__':
    main()
