from unittest import TestCase
from skeleton import validate_move


class test_skeleton_validate_move(TestCase):
    def setUp(self) -> None:
        self.board_width = 5
        self.board_height = 5

    def test_validate_move_up_valid(self):
        direction = 'up'
        player_coordinates = (2, 2)
        expected = True
        actual = validate_move(direction, player_coordinates, self.board_width, self.board_height)
        self.assertEqual(expected, actual)

    def test_validate_move_up_not_valid(self):
        direction = 'up'
        player_coordinates = (0, 0)
        expected = False
        actual = validate_move(direction, player_coordinates, self.board_width, self.board_height)
        self.assertEqual(expected, actual)

    def test_validate_move_down_valid(self):
        direction = 'down'
        player_coordinates = (2, 2)
        expected = True
        actual = validate_move(direction, player_coordinates, self.board_width, self.board_height)
        self.assertEqual(expected, actual)

    def test_validate_move_down_not_valid(self):
        direction = 'down'
        player_coordinates = (4, 0)
        expected = False
        actual = validate_move(direction, player_coordinates, self.board_width, self.board_height)
        self.assertEqual(expected, actual)

    def test_validate_move_left_valid(self):
        direction = 'left'
        player_coordinates = (2, 2)
        expected = True
        actual = validate_move(direction, player_coordinates, self.board_width, self.board_height)
        self.assertEqual(expected, actual)

    def test_validate_move_left_not_valid(self):
        direction = 'left'
        player_coordinates = (0, 0)
        expected = False
        actual = validate_move(direction, player_coordinates, self.board_width, self.board_height)
        self.assertEqual(expected, actual)

    def test_validate_move_right_valid(self):
        direction = 'right'
        player_coordinates = (2, 2)
        expected = True
        actual = validate_move(direction, player_coordinates, self.board_width, self.board_height)
        self.assertEqual(expected, actual)

    def test_validate_move_right_not_valid(self):
        direction = 'right'
        player_coordinates = (0, 5)
        expected = False
        actual = validate_move(direction, player_coordinates, self.board_width, self.board_height)
        self.assertEqual(expected, actual)
