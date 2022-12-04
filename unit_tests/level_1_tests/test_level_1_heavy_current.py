from unittest import TestCase
from levels.level_1 import heavy_current


class Test(TestCase):
    def test_heavy_current_hp_is_max(self):
        player = {'hp': 100, 'max_hp': 100, 'useless_events': 0}
        heavy_current(player)
        actual = player['hp']
        expected = 100
        self.assertEqual(actual, expected)

    def test_heavy_current_hp_is_1(self):
        player = {'hp': 1, 'max_hp': 100, 'useless_events': 0}
        heavy_current(player)
        actual = player['hp']
        expected = 3
        self.assertEqual(actual, expected)
