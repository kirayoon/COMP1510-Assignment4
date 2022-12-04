from unittest import TestCase
from fight import calc_min_roll


class Test_calc_min_roll(TestCase):
    def test_calc_min_roll_player_attack_low_enemy_attack_low(self):
        player_attack = 1
        enemy_attack = 1
        expected = (1, 1)
        actual = calc_min_roll(player_attack, enemy_attack)
        self.assertEqual(expected, actual)

    def test_calc_min_roll_player_attack_low_enemy_attack_high(self):
        player_attack = 1
        enemy_attack = 100
        expected = (1, 90)
        actual = calc_min_roll(player_attack, enemy_attack)
        self.assertEqual(expected, actual)

    def test_calc_min_roll_player_attack_high_enemy_attack_low(self):
        player_attack = 100
        enemy_attack = 1
        expected = (90, 1)
        actual = calc_min_roll(player_attack, enemy_attack)
        self.assertEqual(expected, actual)

    def test_calc_min_roll_player_both_high(self):
        player_attack = 100
        enemy_attack = 100
        expected = (90, 90)
        actual = calc_min_roll(player_attack, enemy_attack)
        self.assertEqual(expected, actual)
