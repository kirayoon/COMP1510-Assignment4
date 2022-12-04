from unittest import TestCase
from levels.level_3 import nut
from skeleton import create_player
from unittest.mock import patch


class Nut_test(TestCase):
    @patch('builtins.input', side_effect=['y'])
    def test_nut(self, mock_input):
        player = create_player('test')
        nut(player)
        actual = [player['inventory']['hazelnut'], player['xp']]
        expected = [1, 10]
        self.assertEqual(actual, expected)
