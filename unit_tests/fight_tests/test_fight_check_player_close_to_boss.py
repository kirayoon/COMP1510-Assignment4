from unittest import TestCase
from fight import check_player_close_to_boss


class Test_check_player_close_to_boss(TestCase):
    def test_check_player_close_to_boss_far(self):
        player_location = (0, 0)
        boss_location = (10, 10)
        actual = check_player_close_to_boss(player_location, boss_location)
        expected = False
        self.assertEqual(actual, expected)

    def test_check_player_close_to_boss_close(self):
        player_location = (0, 0)
        boss_location = (1, 1)
        actual = check_player_close_to_boss(player_location, boss_location)
        expected = True
        self.assertEqual(actual, expected)

    def test_check_player_close_to_boss_close_large_player(self):
        player_location = (10, 10)
        boss_location = (0, 0)
        actual = check_player_close_to_boss(player_location, boss_location)
        expected = False
        self.assertEqual(actual, expected)

    def test_check_player_close_to_boss_close_large_player_large_boss(self):
        player_location = (10, 10)
        boss_location = (9, 9)
        actual = check_player_close_to_boss(player_location, boss_location)
        expected = True
        self.assertEqual(actual, expected)

    def test_check_player_close_to_boss_close_on_boss(self):
        player_location = (0, 0)
        boss_location = (0, 0)
        actual = check_player_close_to_boss(player_location, boss_location)
        expected = True
        self.assertEqual(actual, expected)