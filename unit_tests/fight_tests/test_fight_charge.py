from unittest import TestCase
from skeleton import create_player
from fight import charge
from unittest.mock import patch

class Test_charge(TestCase):
    def setUp(self) -> None:
        self.player = create_player('test')

    @patch('random.randint', return_value=1)
    def test_charge_low_roll(self, random_number_generator):
        actual = charge(self.player, 'test_enemy', 1)
        expected = self.player['attack'] * 2
        self.assertEqual(self.player['hp'], 19)
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=9)
    def test_charge_high_roll(self, random_number_generator):
        actual = charge(self.player, 'test_enemy', 1)
        expected = self.player['attack'] * 2
        self.assertEqual(self.player['hp'], 11)
        self.assertEqual(actual, expected)
