from unittest import TestCase
from unittest.mock import patch
from skeleton import get_player_choice


class Test_get_player_choice(TestCase):
    def setUp(self):
        self.command_map = {'up': '',
                            'down': '',
                            'left': '',
                            'right': '',
                            'sleep': '',
                            'player': '',
                            'inventory': '',
                            'help': '',
                            'quit': ''}

    @patch('builtins.input', return_value='up')
    def test_get_player_word_in_command_map(self, mock_input):
        expected = 'up'
        actual = get_player_choice(self.command_map)
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='d')
    def test_get_player_first_letter_in_command_map(self, mock_input):
        expected = 'down'
        actual = get_player_choice(self.command_map)
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='3')
    def test_get_player_number_in_command_map(self, mock_input):
        expected = 'left'
        actual = get_player_choice(self.command_map)
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='DOWN')
    def test_get_player_upper_word_in_command_map(self, mock_input):
        expected = 'down'
        actual = get_player_choice(self.command_map)
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='H')
    def test_get_player_upper_first_letter_in_command_map(self, mock_input):
        expected = 'help'
        actual = get_player_choice(self.command_map)
        self.assertEqual(expected, actual)
