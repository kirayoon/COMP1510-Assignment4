from unittest import TestCase
from levels.level_3 import berry
from skeleton import create_player


class Berry_test(TestCase):
    def test_berry(self):
        player = create_player('test')
        berry(player)
        actual = player['inventory']['berry']
        expected = 1
        self.assertEqual(actual, expected)
