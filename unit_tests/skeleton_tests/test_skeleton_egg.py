from unittest import TestCase
from skeleton import egg

class Test_egg(TestCase):
    def test_egg_not_in_dict(self):
        player = {'inventory': {'egg': 0}}
        egg(player)
        self.assertEqual(player['inventory']['egg'], 1)

    def test_egg_in_dict(self):
        player = {'inventory': {'egg': 1}}
        egg(player)
        self.assertEqual(player['inventory']['egg'], 2)