from unittest import TestCase
from skeleton import create_player
from fight import bite
from unittest.mock import patch


class Test_bite(TestCase):
    def setUp(self) -> None:
        self.player = create_player('test')

    @patch('random.randint', return_value=0)
    def test_bite_low_roll(self, random_number_generator):
        actual = bite(self.player, 'test_enemy')
        expected = 0
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=10)
    def test_bite_high_roll(self, random_number_generator):
        actual = bite(self.player, 'test_enemy')
        expected = self.player['attack'] * 2
        self.assertEqual(actual, expected)