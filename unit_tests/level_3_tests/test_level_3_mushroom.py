from unittest import TestCase
from unittest.mock import patch
from levels.level_3 import mushroom


class Mushroom_test(TestCase):
    @patch('builtins.input', side_effect=['y'])
    @patch('random.randint', side_effect=[1])
    def test_mushroom_not_poisonous_max_health(self, mock_input, mock_randint):
        player = {'hp': 10, 'max_hp': 10}
        mushroom(player)
        actual = player['hp']
        expected = 10
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['y'])
    @patch('random.randint', side_effect=[2])
    def test_mushroom_poisonous_max_health(self, mock_input, mock_randint):
        player = {'hp': 10, 'max_hp': 10}
        mushroom(player)
        actual = player['hp']
        expected = 5
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['y'])
    @patch('random.randint', side_effect=[1])
    def test_mushroom_not_poisonous_low_health(self, mock_input, mock_randint):
        player = {'hp': 1, 'max_hp': 10}
        mushroom(player)
        actual = player['hp']
        expected = 6
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['y'])
    @patch('random.randint', side_effect=[2])
    def test_mushroom_poisonous_low_health(self, mock_input, mock_randint):
        player = {'hp': 1, 'max_hp': 10}
        mushroom(player)
        actual = player['hp']
        expected = 1
        self.assertEqual(actual, expected)
