from unittest import TestCase
from player import player_sleep


class Test_player_sleep(TestCase):
    def test_player_sleep(self):
        player = {'hp': 10, 'max_hp': 20}
        player_sleep(player)
        self.assertEqual(player['hp'], 20)
