from unittest import TestCase
from fight import move_player_towards_boss


class Test_fight_move_player_towards_boss(TestCase):
    def test_move_player_towards_boss_horizontal_positive(self):
        player_location = (0, 0)
        boss_location = (0, 10)
        actual = move_player_towards_boss(player_location, boss_location)
        expected = (0, 1)
        self.assertEqual(actual, expected)

    def test_move_player_towards_boss_horizontal_negative(self):
        player_location = (0, 10)
        boss_location = (0, 0)
        actual = move_player_towards_boss(player_location, boss_location)
        expected = (0, 9)
        self.assertEqual(actual, expected)

    def test_move_player_towards_boss_vertical_positive(self):
        player_location = (0, 0)
        boss_location = (10, 0)
        actual = move_player_towards_boss(player_location, boss_location)
        expected = (1, 0)
        self.assertEqual(actual, expected)

    def test_move_player_towards_boss_vertical_negative(self):
        player_location = (10, 0)
        boss_location = (0, 0)
        actual = move_player_towards_boss(player_location, boss_location)
        expected = (9, 0)
        self.assertEqual(actual, expected)

    def test_move_player_towards_boss_diagonal_positive(self):
        player_location = (0, 0)
        boss_location = (10, 10)
        actual = move_player_towards_boss(player_location, boss_location)
        expected = (1, 1)
        self.assertEqual(actual, expected)

    def test_move_player_towards_boss_diagonal_negative(self):
        player_location = (10, 10)
        boss_location = (0, 0)
        actual = move_player_towards_boss(player_location, boss_location)
        expected = (9, 9)
        self.assertEqual(actual, expected)
