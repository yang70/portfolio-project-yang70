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
            self.piece.valid_move(self.valid_start_column, self.valid_start_row, self.board)
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

    def test_get_coordinates(self):
        self.assertEqual(
            self.piece.get_coordinates(),
            { "row": self.valid_start_row, "column": self.valid_start_column }
        )

    def test_is_in_play(self):
        self.assertTrue(
            self.piece.is_in_play()
        )

        self.piece._in_play = False

        self.assertFalse(
            self.piece.is_in_play()
        )

    def test_capture(self):
        self.assertTrue(
            self.piece._in_play
        )

        self.piece.capture()

        self.assertFalse(
            self.piece._in_play
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



class CannonTester(PieceTester):
    def setUp(self):
        self.board = copy.deepcopy( XiangqiGame.BLANK_BOARD )
        self.klass = Cannon
        self.valid_start_row    = 3
        self.valid_start_column = 'b'
        self.valid_end_row      = 3
        self.valid_end_column   = 'g'

        self.piece = self.klass('red', self.valid_start_column, self.valid_start_row)

    def test_valid_move_empty_row(self):
        self.assertTrue(
            self.piece.valid_move('e', 3, self.board)
        )

    def test_valid_move_empty_column(self):
        self.assertTrue(
            self.piece.valid_move('h', 3, self.board)
        )

    def test_invalid_move_row_not_empty(self):
        self.board[3]['c'] = Piece('red', 'c', 3)

        self.assertFalse(
            self.piece.valid_move('d', 3, self.board)
        )

    def test_invalid_move_row_not_empty_2(self):
        self.board[3]['c'] = Piece('red', 'c', 3)
        self.board[3]['d'] = Piece('red', 'd', 3)
        self.board[3]['e'] = Piece('black', 'e', 3)

        self.assertFalse(
            self.piece.valid_move('e', 3, self.board)
        )

    def test_valid_move_row_not_empty(self):
        self.board[3]['c'] = Piece('red', 'c', 3)
        self.board[3]['d'] = Piece('black', 'd', 3)

        self.assertTrue(
            self.piece.valid_move('d', 3, self.board)
        )

    def test_invalid_move_column_not_empty(self):
        self.board[4]['b'] = Piece('red', 'b', 4)

        self.assertFalse(
            self.piece.valid_move('b', 5, self.board)
        )

    def test_invalid_move_column_not_empty_2(self):
        self.board[4]['b'] = Piece('red', 'b', 4)
        self.board[5]['b'] = Piece('red', 'b', 5)
        self.board[6]['b'] = Piece('black', 'b', 6)

        self.assertFalse(
            self.piece.valid_move('b', 6, self.board)
        )

    def test_valid_move_column_not_empty(self):
        self.board[4]['b'] = Piece('red', 'b', 4)
        self.board[5]['b'] = Piece('black', 'b', 5)

        self.assertTrue(
            self.piece.valid_move('b', 5, self.board)
        )

    def test_invalid_diagonal_move(self):
        self.assertFalse(
            self.piece.valid_move('c', 4, self.board)
        )

class ChariotTester(PieceTester):
    def setUp(self):
        self.board = copy.deepcopy( XiangqiGame.BLANK_BOARD )
        self.klass = Chariot
        self.valid_start_row    = 1
        self.valid_start_column = 'a'
        self.valid_end_row      = 3
        self.valid_end_column   = 'a'

        self.piece = self.klass('red', self.valid_start_column, self.valid_start_row)

    def test_valid_move_empty_row(self):
        self.assertTrue(
            self.piece.valid_move('c', 1, self.board)
        )

    def test_valid_move_empty_column(self):
        self.assertTrue(
            self.piece.valid_move('a', 5, self.board)
        )

    def test_invalid_move_row_not_empty(self):
        self.board[1]['b'] = Piece('red', 'b', 1)

        self.assertFalse(
            self.piece.valid_move('d', 1, self.board)
        )

    def test_invalid_move_column_not_empty(self):
        self.board[2]['a'] = Piece('red', 'a', 2)

        self.assertFalse(
            self.piece.valid_move('a', 3, self.board)
        )

    def test_invalid_diagonal_move(self):
        self.assertFalse(
            self.piece.valid_move('b', 2, self.board)
        )

class ElephantTester(PieceTester):
    def setUp(self):
        self.board = copy.deepcopy( XiangqiGame.BLANK_BOARD )
        self.klass = Elephant
        self.valid_start_row    = 1
        self.valid_start_column = 'c'
        self.valid_end_row      = 3
        self.valid_end_column   = 'a'

        self.piece = self.klass('red', self.valid_start_column, self.valid_start_row)

    def test_invalid_move_too_short(self):
        self.assertFalse(
            self.piece.valid_move('b', 2, self.board)
        )

    def test_invalid_move_too_long(self):
        self.assertFalse(
            self.piece.valid_move('f', 4, self.board)
        )

    def test_invalid_move_straight(self):
        self.assertFalse(
            self.piece.valid_move('c', 3, self.board)
        )

    def test_invalid_move_piece_in_the_way_1(self):
        self.board[2]['b'] = Piece('red', 'b', 2)

        self.assertFalse(
            self.piece.valid_move('a', 3, self.board)
        )

    def test_invalid_move_piece_in_the_way_2(self):
        self.board[2]['d'] = Piece('red', 'd', 2)

        self.assertFalse(
            self.piece.valid_move('e', 3, self.board)
        )

    def test_invalid_move_piece_in_the_way_3(self):
        piece              = self.klass('black', 'c', 10)
        self.board[9]['d'] = Piece('black', 'd', 9)

        self.assertFalse(
            piece.valid_move('e', 8, self.board)
        )

    def test_invalid_move_piece_in_the_way_4(self):
        piece              = self.klass('black', 'c', 10)
        self.board[9]['b'] = Piece('black', 'b', 9)

        self.assertFalse(
            piece.valid_move('a', 8, self.board)
        )

    def test_invalid_move_across_river_red(self):
        self.piece.set_coordinates('c', 5)

        self.assertFalse(
            self.piece.valid_move('a', 7, self.board)
        )

    def test_invalid_move_across_river_black(self):
        piece = self.klass('black', 'c', 6)

        self.assertFalse(
            self.piece.valid_move('a', 4, self.board)
        )

    def test_valid_move_black(self):
        piece = self.klass('black', 'c', 10)

        self.assertTrue(
            piece.valid_move('e', 8, self.board)
        )

class GeneralTester(PieceTester):
    def setUp(self):
        self.board = copy.deepcopy( XiangqiGame.BLANK_BOARD )
        self.klass = General
        self.valid_start_row    = 1
        self.valid_start_column = 'e'
        self.valid_end_row      = 2
        self.valid_end_column   = 'e'

        self.piece = self.klass('red', self.valid_start_column, self.valid_start_row)

    def test_invalid_move_diagonal(self):
        self.assertFalse(
            self.piece.valid_move('d', 2, self.board)
        )

    def test_invalid_move_straight_more_than_one(self):
        self.assertFalse(
            self.piece.valid_move('e', 3, self.board)
        )

    def test_invalid_move_to_see_other_general_red(self):
        self.board[10]['d'] = self.klass('black', 'd', 9)

        self.assertFalse(
            self.piece.valid_move('d', 1, self.board)
        )

    def test_valid_move_to_see_other_general_red(self):
        self.board[10]['d'] = self.klass('black', 'd', 9)
        self.board[9]['d']  = Piece('black', 'd', 9)

        self.assertTrue(
            self.piece.valid_move('d', 1, self.board)
        )

    def test_invalid_move_to_see_other_general_black(self):
        self.piece.set_coordinates('f', 2)
        self.board[2]['f'] = self.piece
        black_general      = self.klass('black', 'e', 10)

        self.assertFalse(
            black_general.valid_move('f', 10, self.board)
        )

    def test_valid_move_to_see_other_general_black(self):
        self.piece.set_coordinates('f', 2)
        self.board[2]['f'] = self.piece
        self.board[3]['f'] = Piece('red', 'f', 3)
        black_general      = self.klass('black', 'e', 10)

        self.assertTrue(
            black_general.valid_move('f', 10, self.board)
        )

class HorseTester(PieceTester):
    def setUp(self):
        self.board = copy.deepcopy( XiangqiGame.BLANK_BOARD )
        self.klass = Horse
        self.valid_start_row    = 1
        self.valid_start_column = 'b'
        self.valid_end_row      = 3
        self.valid_end_column   = 'a'

        self.piece = self.klass('red', self.valid_start_column, self.valid_start_row)

    def test_invalid_move_too_far(self):
        self.assertFalse(
            self.piece.valid_move('c', 4, self.board)
        )

    def test_invalid_move_down_left(self):
        self.piece.set_coordinates('e', 7)
        self.board[8]['e'] = Piece('red', 'e', 8)

        self.assertFalse(
            self.piece.valid_move('d', 9, self.board)
        )

    def test_invalid_move_down_right(self):
        self.piece.set_coordinates('e', 7)
        self.board[8]['e'] = Piece('red', 'e', 8)

        self.assertFalse(
            self.piece.valid_move('f', 9, self.board)
        )

    def test_invalid_move_up_left(self):
        self.piece.set_coordinates('e', 7)
        self.board[6]['e'] = Piece('red', 'e', 6)

        self.assertFalse(
            self.piece.valid_move('d', 5, self.board)
        )

    def test_invalid_move_up_right(self):
        self.piece.set_coordinates('e', 7)
        self.board[6]['e'] = Piece('red', 'e', 6)

        self.assertFalse(
            self.piece.valid_move('f', 5, self.board)
        )

    def test_invalid_move_left_up(self):
        self.piece.set_coordinates('e', 7)
        self.board[7]['d'] = Piece('red', 'd', 7)

        self.assertFalse(
            self.piece.valid_move('c', 6, self.board)
        )

    def test_invalid_move_left_down(self):
        self.piece.set_coordinates('e', 7)
        self.board[7]['d'] = Piece('red', 'd', 7)

        self.assertFalse(
            self.piece.valid_move('c', 8, self.board)
        )

    def test_invalid_move_right_up(self):
        self.piece.set_coordinates('e', 7)
        self.board[7]['f'] = Piece('red', 'f', 7)

        self.assertFalse(
            self.piece.valid_move('g', 6, self.board)
        )

    def test_invalid_move_right_down(self):
        self.piece.set_coordinates('e', 7)
        self.board[7]['f'] = Piece('red', 'f', 7)

        self.assertFalse(
            self.piece.valid_move('g', 8, self.board)
        )

class SoldierTester(PieceTester):
    def setUp(self):
        self.board = copy.deepcopy( XiangqiGame.BLANK_BOARD )
        self.klass = Soldier
        self.valid_start_row    = 4
        self.valid_start_column = 'a'
        self.valid_end_row      = 5
        self.valid_end_column   = 'a'

        self.piece = self.klass('red', self.valid_start_column, self.valid_start_row)

    def test_invalid_move_too_far(self):
        self.assertFalse(
            self.piece.valid_move('a', 6, self.board)
        )

    def test_invalid_move_sideways_before_river_red(self):
        self.assertFalse(
            self.piece.valid_move('b', 4, self.board)
        )

    def test_valid_move_sideways_after_river_red(self):
        self.piece.set_coordinates('a', 6)

        self.assertTrue(
            self.piece.valid_move('b', 6, self.board)
        )

    def test_invalid_move_sideways_before_river_black(self):
        piece = self.klass('black', 'a', 7)

        self.assertFalse(
            piece.valid_move('b', 7, self.board)
        )

    def test_valid_move_sideways_after_river_black(self):
        piece = self.klass('black', 'a', 5)

        self.assertTrue(
            piece.valid_move('b', 5, self.board)
        )

if __name__ == '__main__':
    unittest.main()