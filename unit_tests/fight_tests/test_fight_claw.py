from unittest import TestCase
from skeleton import create_player
from fight import claw
from unittest.mock import patch


class Test_claw(TestCase):
    def setUp(self) -> None:
        self.player = create_player('test')

    @patch('random.randint', return_value=1)
    def test_claw_low_roll(self, random_number_generator):
        actual = claw(self.player, 'test_enemy', 1)
        expected = 1
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=5)
    def test_claw_high_roll(self, random_number_generator):
        actual = claw(self.player, 'test_enemy', 1)
        expected = self.player['attack']
        self.assertEqual(actual, expected)
