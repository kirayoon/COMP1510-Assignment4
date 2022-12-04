from unittest import TestCase
from levels.level_1 import slippery_rock


class Test(TestCase):
    def test_slippery_rock_hp_is_max(self):
        player = {'hp': 100}
        slippery_rock(player)
        actual = player['hp']
        expected = 99
        self.assertEqual(actual, expected)

    def test_slippery_rock_hp_is_1(self):
        player = {'hp': 1}
        slippery_rock(player)
        actual = player['hp']
        expected = 1
        self.assertEqual(actual, expected)
