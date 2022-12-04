from unittest import TestCase
from levels.level_final import Boss
from unittest.mock import patch
from skeleton import create_player
import json
from pathlib import Path


class TestBoss(TestCase):
    def setUp(self) -> None:
        with open(Path('../json/') / 'enemy.json') as file:
            boss_data = json.load(file)
        enemy_dict = boss_data['mama']
        self.test_boss = Boss(enemy_dict)

    def test_get_hp(self):
        expected = 100
        actual = self.test_boss.get_hp()
        self.assertEqual(expected, actual)

    def test_get_location(self):
        expected = (2, 2)
        actual = self.test_boss.get_location()
        self.assertEqual(expected, actual)

    def test_get_stats(self):
        expected = {'hp': 100, 'max_hp': 100, 'name': 'Mama Lob', 'attack': 10}
        actual = self.test_boss.get_stats()
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[50])
    def test_shoot_success(self, mock_randint):
        player = create_player('test')
        self.test_boss.shoot(player)
        expected = 10
        actual = player['hp']
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[80])
    def test_shoot_fail(self, mock_randint):
        player = create_player('test')
        self.test_boss.shoot(player)
        expected = 20
        actual = player['hp']
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[5])
    def test_bomb(self, mock_randint):
        player = create_player('test')
        self.test_boss.bomb(player)
        expected = 15
        actual = player['hp']
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1, 1])
    def test_move_1_1(self, mock_randint):
        player = create_player('test')
        self.test_boss.move(player)
        expected = (3, 3)
        actual = self.test_boss.get_location()
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[-1, -1])
    def test_move_neg1_neg1(self, mock_randint):
        player = create_player('test')
        self.test_boss.move(player)
        expected = (1, 1)
        actual = self.test_boss.get_location()
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[-1, 1])
    def test_move_pos_neg(self, mock_randint):
        player = create_player('test')
        self.test_boss.move(player)
        expected = (1, 3)
        actual = self.test_boss.get_location()
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[0, 0])
    def test_move_zero(self, mock_randint):
        player = create_player('test')
        self.test_boss.move(player)
        expected = (2, 2)
        actual = self.test_boss.get_location()
        self.assertEqual(expected, actual)

    def test_is_damaged(self):
        self.test_boss.is_damaged(10)
        expected = 90
        actual = self.test_boss.get_hp()
        self.assertEqual(expected, actual)

    def test_boss_is_dead(self):
        self.test_boss.is_damaged(100)
        expected = True
        actual = self.test_boss.is_dead()
        self.assertEqual(expected, actual)