from unittest import TestCase
from unittest.mock import patch
from fight import death_sequence


class Test_death_sequence(TestCase):
    def setUp(self) -> None:
        self.player = {'name': 'Test',
                       'hp': 0,
                       'max_hp': 100,
                       'turn': 10,
                       'xp': 100,
                       'soup_counter': 10,
                       'chair_counter': 10,
                       'location': (10, 10)}

    @patch('builtins.input', side_effect=['y'])
    def test_death_sequence(self, mock_input):
        death_sequence(self.player)
        self.assertEqual(self.player['hp'], 100)
        self.assertEqual(self.player['turn'], 0)
        self.assertEqual(self.player['xp'], 0)
        self.assertEqual(self.player['soup_counter'], 0)
        self.assertEqual(self.player['chair_counter'], 0)
        self.assertEqual(self.player['location'], (0, 0))

