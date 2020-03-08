import unittest, copy
from pieces import Piece, Advisor, Cannon, Chariot, Elephant, General, Horse, Soldier
from XiangqiGame import XiangqiGame

class PieceTester(unittest.TestCase):
    def setUp(self):
        self.board = copy.deepcopy( XiangqiGame.BLANK_BOARD )
        # Setting the class in the setUp method allows for other test classes to
        # inherit from this class and overrite this method to test their specific
        # class
        self.klass = Piece
        self.valid_start_row    = 1
        self.valid_start_column = 'a'
        self.valid_end_row      = 2
        self.valid_end_column   = 'a'

        self.piece = self.klass('red', self.valid_start_column, self.valid_start_row)

    def test_valid_move(self):
        self.assertTrue(
            self.piece.valid_move(self.valid_end_column, self.valid_end_row, self.board)
        )

    def test_invalid_column_move_high(self):
        self.assertFalse(
            self.piece.valid_move('j', self.valid_end_row, self.board)
        )

    def test_invalid_column_move_low(self):
        self.assertFalse(
            self.piece.valid_move('j', self.valid_end_row, self.board)
        )

    def test_invalid_row_move_high(self):
        self.assertFalse(
            self.piece.valid_move(self.valid_start_column, 11, self.board)
        )

    def test_invalid_row_move_low(self):
        self.assertFalse(
            self.piece.valid_move(self.valid_start_column, 0, self.board)
        )

    def test_invalid_row_and_column_move(self):
        self.assertFalse(
            self.piece.valid_move('j', 0, self.board)
        )

    def test_invalid_move_to_current_position(self):
        self.assertFalse(
            self.piece.valid_move('a', 1, self.board)
        )

    def test_invalid_move_to_position_with_same_color(self):
        piece_2 = self.klass('red', self.valid_end_column, self.valid_end_row)
        self.board[self.valid_end_row][self.valid_end_column] = piece_2

        self.assertFalse(
            self.piece.valid_move(self.valid_end_column, self.valid_end_row, self.board)
        )

    def test_set_coordinates(self):
        self.piece.set_coordinates('b', 1)

        self.assertEqual(
            self.piece._column,
            'b'
        )

        self.assertEqual(
            self.piece._row,
            1
        )

class AdvisorTester(PieceTester):
    def setUp(self):
        self.board = copy.deepcopy( XiangqiGame.BLANK_BOARD )
        self.klass = Advisor
        self.valid_start_row    = 1
        self.valid_start_column = 'd'
        self.valid_end_row      = 2
        self.valid_end_column   = 'e'

        self.piece = self.klass('red', self.valid_start_column, self.valid_start_row)

    def test_valid_column(self):
        self.assertTrue(
            self.piece.valid_move('e', 2, self.board)
        )

    def test_invalid_column_low(self):
        self.assertFalse(
            self.piece.valid_move('c', 2, self.board)
        )

    def test_invalid_column_high(self):
        self.assertFalse(
            self.piece.valid_move('g', 2, self.board)
        )

    def test_invalid_row_low_red(self):
        self.assertFalse(
            self.piece.valid_move('d', 0, self.board)
        )

    def test_invalid_row_high_red(self):
        piece = self.klass('red', 'd', 3)

        self.assertFalse(
            piece.valid_move('d', 4, self.board)
        )

    def test_invalid_row_low_black(self):
        piece = self.klass('black', 'd', 8)

        self.assertFalse(
            piece.valid_move('d', 7, self.board)
        )

    def test_invalid_row_high_black(self):
        piece = self.klass('black', 'd', 8)

        self.assertFalse(
            piece.valid_move('d', 11, self.board)
        )

    def test_invalid_non_diagonal(self):
        self.assertFalse(
            self.piece.valid_move('d', 2, self.board)
        )

    def test_valid_move(self):
        self.assertTrue(
            self.piece.valid_move('e', 2, self.board)
        )



# class CannonTester(PieceTester):
#     def setUp(self):
#         self.board = copy.deepcopy( XiangqiGame.BLANK_BOARD )
#         self.klass = Cannon

# class ChariotTester(PieceTester):
#     def setUp(self):
#         self.board = copy.deepcopy( XiangqiGame.BLANK_BOARD )
#         self.klass = Chariot

# class ElephantTester(PieceTester):
#     def setUp(self):
#         self.board = copy.deepcopy( XiangqiGame.BLANK_BOARD )
#         self.klass = Elephant

# class GeneralTester(PieceTester):
#     def setUp(self):
#         self.board = copy.deepcopy( XiangqiGame.BLANK_BOARD )
#         self.klass = General

# class HorseTester(PieceTester):
#     def setUp(self):
#         self.board = copy.deepcopy( XiangqiGame.BLANK_BOARD )
#         self.klass = Horse

# class SoldierTester(PieceTester):
#     def setUp(self):
#         self.board = copy.deepcopy( XiangqiGame.BLANK_BOARD )
#         self.klass = Soldier

if __name__ == '__main__':
    unittest.main()