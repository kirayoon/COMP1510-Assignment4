import random


class Boss:
    def __init__(self, enemy_dict: dict):
        """
        Initialize a boss object

        :param enemy_dict: A dictionary containing the boss's stats
        :precondition: enemy_dict must be a dictionary
        :precondition: enemy_dict must contain the following keys: 'hp', 'max_hp', 'name', 'attack', 'abilities'
        :precondition: enemy_dict['abilities'] must contain the following keys: 'shoot', 'bomb', 'move'
        :precondition: enemy_dict['abilities']['shoot'] must contain the following keys: 'damage', 'flavour_text', 'flavour_text_miss'
        :precondition: enemy_dict['abilities']['bomb'] must contain the following keys: 'damage', 'flavour_text'
        :precondition: enemy_dict['abilities']['move'] must contain the following keys: 'flavour_text'
        :postcondition: A boss object is created
        """
        self.location = (2, 2)
        self.hp = 100
        self.max_hp = 100
        self.attack = 10
        self.name = 'Mama Lob'
        self.abilities = enemy_dict['abilities']
        self.ability_names = list(enemy_dict['abilities'].keys())
        self.shot_count = 3
        self.turn_count = 1

    def get_hp(self):
        """
        Get the boss's current hp

        :return: The boss's current hp as an int
        """
        return self.hp

    def get_location(self):
        """
        Get the boss's current location

        :return: the boss's current location as a tuple
        """
        return self.location

    def get_stats(self):
        """
        Get the boss's stats

        :return: A dictionary containing the boss's stats for hp, max_hp, attack, and name
        """
        return {'hp': self.hp, 'max_hp': self.max_hp, 'name': self.name, 'attack': self.attack}

    def choose_move(self, player_dict) -> None:
        """
        Choose a move for the boss to make

        :param player_dict: a dictionary containing the player's stats
        :precondition: player_dict must be a dictionary
        :precondition: player_dict must contain the following keys: 'hp', 'max_hp', 'name', 'attack', 'location'
        :postcondition: a move is chosen for the boss to make based on a loop
        """
        move_loop = ['shoot', 'move', 'bomb', 'move']
        current_move = move_loop[self.turn_count % 4]
        eval(f'self.{current_move}')(player_dict)

    def shoot(self, player_dict) -> None:
        """
        Calculate the amount of damage done to player, print flavour text, and subtract damage from player's hp

        :param player_dict: a dictionary containing the player's stats
        :precondition: player_dict must be a dictionary
        :precondition: player_dict must contain the following keys: 'hp'
        :postcondition: calculates the damage done to the player and prints the flavour text
        :postcondition: subtracts the damage done to the player from their hp
        :postcondition: player_dict is modified
        """
        accuracy = 60
        if random.randint(1, 100) <= accuracy:
            self.shot_count -= 1
            print(f'''
            {self.abilities["shoot"]["flavour_text"]}
            \b\b\b\bIt does {self.abilities["shoot"]["damage"]} damage!
        
            \b\b\b\bMama Lob has {self.shot_count} shot(s) left!
            ''')
            # return self.abilities['shoot']['damage']
            player_dict['hp'] -= self.abilities['shoot']['damage']
        else:
            print(f'''
            {self.abilities["shoot"]["flavour_text_miss"]} 
            ''')
            player_dict['hp'] -= 0

    def bomb(self, player_dict: dict) -> None:
        """
        Calculate the amount of damage done to player, print flavour text, and subtract damage from player's hp

        :param player_dict: a dictionary containing the player's stats
        :precondition: player_dict must be a dictionary
        :precondition: player_dict must contain the following keys: 'hp'
        :postcondition: calculates the damage done to the player and prints the flavour text
        :postcondition: subtracts the damage done to the player from their hp
        :postcondition: player_dict is modified
        """
        min_damage = int(self.abilities['bomb']['damage'] / 2)
        max_damage = self.abilities['bomb']['damage']
        damage = random.randint(min_damage, max_damage)
        print(f'''
        {self.abilities["bomb"]["flavour_text"]} 
        It does {damage} damage!
        ''')
        player_dict['hp'] -= damage

    def move(self, player_dict: dict) -> None:
        """
        Move the boss to a random location

        :param player_dict: a dictionary containing the player's stats
        :precondition: player_dict must be a dictionary
        :precondition: player_dict must contain the following keys: 'location'
        :postcondition: check if boss' new location is a valid location
        :postcondition: the boss's location is changed to a random location
        :postcondition: player_dict is modified
        :postcondition: Prints the flavour text for the move
        """
        x_direction = random.randint(-1, 1)
        y_direction = random.randint(-1, 1)
        player_loc = player_dict['location']
        new_location = (self.location[0] + x_direction, self.location[1] + y_direction)
        if 0 <= new_location[0] <= 4 and 0 <= new_location[1] <= 4 and new_location != player_loc:
            self.location = new_location
            print(f'''{self.abilities['move']['flavour_text']}''')
        else:
            self.move(player_dict)

    def is_damaged(self, damage: int) -> None:
        """
        Subtract the player's attack from the boss's hp

        :param damage: the amount of damage to be done to the boss
        :precondition: damage must be an int
        :precondition: damage must be greater than 0
        :postcondition: the boss's hp is subtracted by the damage
        """
        self.hp -= damage

    def is_dead(self) -> bool:
        """
        Check if the boss is dead

        :postcondition: evaluate if the boss's hp is less than or equal to 0
        :return: true if the boss's hp is less than or equal to 0, false otherwise
        """
        return self.hp <= 0


def main():
    """
    Drive the program
    """
    print('Please run the game.py file. This is a module.')


if __name__ == '__main__':
    main()
