from unittest import TestCase
from levels.level_2 import soup
from skeleton import create_player


class soup_test(TestCase):
    def test_soup_counter_is_0(self):
        player = create_player('test')
        soup(player)
        actual = player['soup_counter']
        expected = 1
        self.assertEqual(actual, expected)

    def test_soup_counter_is_1(self):
        player = create_player('test')
        player['soup_counter'] = 1
        soup(player)
        actual = player['soup_counter']
        expected = 2
        self.assertEqual(actual, expected)

    def test_xp_gain(self):
        player = create_player('test')
        soup(player)
        actual = player['xp']
        expected = 200
        self.assertEqual(actual, expected)

