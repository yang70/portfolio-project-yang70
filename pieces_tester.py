import unittest
from pieces import Piece, Advisor, Cannon, Chariot, Elephant, General, Horse, Soldier
from XiangqiGame import XiangqiGame

class PieceTester(unittest.TestCase):
    def setUp(self):
        self.board = XiangqiGame.BLANK_BOARD
        # Setting the class in the setUp method allows for other test classes to
        # inherit from this class and overrite this method to test their specific
        # class
        self.klass = Piece

    def test_valid_move(self):
        piece = self.klass('red', 'a', 1)

        self.assertTrue(
            piece.valid_move('a', 2, self.board)
        )

    def test_invalid_column_move_high(self):
        piece = self.klass('red', 'a', 1)

        self.assertFalse(
            piece.valid_move('j', 1, self.board)
        )

    def test_invalid_column_move_low(self):
        piece = self.klass('red', 'A', 1)

        self.assertFalse(
            piece.valid_move('j', 1, self.board)
        )

    def test_invalid_row_move_high(self):
        piece = self.klass('red', 'a', 1)

        self.assertFalse(
            piece.valid_move('a', 11, self.board)
        )

    def test_invalid_row_move_low(self):
        piece = self.klass('red', 'a', 1)

        self.assertFalse(
            piece.valid_move('a', 0, self.board)
        )

    def test_invalid_row_and_column_move(self):
        piece = self.klass('red', 'a', 1)

        self.assertFalse(
            piece.valid_move('j', 0, self.board)
        )

    def test_invalid_move_to_current_position(self):
        piece = self.klass('red', 'a', 1)

        self.assertFalse(
            piece.valid_move('a', 1, self.board)
        )

class AdvisorTester(PieceTester):
    def setUp(self):
        self.board = XiangqiGame.BLANK_BOARD
        self.klass = Advisor


class CannonTester(PieceTester):
    def setUp(self):
        self.board = XiangqiGame.BLANK_BOARD
        self.klass = Cannon

class ChariotTester(PieceTester):
    def setUp(self):
        self.board = XiangqiGame.BLANK_BOARD
        self.klass = Chariot

class ElephantTester(PieceTester):
    def setUp(self):
        self.board = XiangqiGame.BLANK_BOARD
        self.klass = Elephant

class GeneralTester(PieceTester):
    def setUp(self):
        self.board = XiangqiGame.BLANK_BOARD
        self.klass = General

class HorseTester(PieceTester):
    def setUp(self):
        self.board = XiangqiGame.BLANK_BOARD
        self.klass = Horse

class SoldierTester(PieceTester):
    def setUp(self):
        self.board = XiangqiGame.BLANK_BOARD
        self.klass = Soldier

if __name__ == '__main__':
    unittest.main()