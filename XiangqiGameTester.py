# Author: Matthew Yang
# Date: 03/01/2020
# Description: Tests for the XiangqiGame class.

import unittest, copy
from XiangqiGame import XiangqiGame
from pieces import Piece, Advisor, Cannon, Chariot, Elephant, General, Horse, Soldier

class XiangqiGameTester(unittest.TestCase):
    def setUp(self):
        self.game = XiangqiGame()

    def test_move_exposes_general(self):
        red_soldier = self.game._board[4]['e']
        self.game._board[4]['e'] = None
        self.game._board[7]['e'] = red_soldier
        red_soldier.set_coordinates('e', 7)

        self.assertTrue(
            self.game.move_exposes_general(
                { "row": 7, "column": 'e' },
                { "row": 7, "column": 'd'}
            )
        )

    def test_move_puts_current_player_in_check(self):
        red_soldier = self.game._board[4]['e']
        self.game._board[4]['e'] = None
        self.game._board[7]['e'] = red_soldier
        red_soldier.set_coordinates('e', 7)

        black_rook = self.game._board[10]['a']
        self.game._board[10]['a'] = None
        self.game._board[8]['e'] = black_rook
        black_rook.set_coordinates('e', 8)

        self.assertFalse(
            self.game.is_in_check('red')
        )

        self.assertTrue(
            self.game.move_puts_current_player_in_check(
                { "row": 7, "column": 'e' },
                { "row": 7, "column": 'd'}
            )
        )

        self.assertFalse(
            self.game.is_in_check('red')
        )

    def test_basic_integration(self):
        self.assertTrue(
            self.game.make_move('h3', 'h10')
        )

        self.assertFalse(
            self.game.make_move('f10', 'e9')
        )

    def test_black_check_1(self):
        self.game._board = copy.deepcopy( XiangqiGame.BLANK_BOARD )
        red_general = General('red', 'e', 1)
        red_advisor = Advisor('red', 'd', 1)

        black_chariot = Chariot('black', 'd', 8)
        black_general = General('black', 'd', 10)

        self.game._board[1]['e'] = red_general
        self.game._board[1]['d'] = red_advisor
        self.game._board[8]['d'] = black_chariot
        self.game._board[10]['d'] = black_general

        self.game._red_pieces = {
            'G': red_general,
            'A1': red_advisor
        }

        self.game._black_pieces = {
            'G': black_general,
            'R1': black_chariot
        }

        self.game._current_turn = "black"

        self.assertFalse(
            self.game.is_in_check('red')
        )

        self.assertTrue(
            self.game.make_move('d8', 'd1')
        )

        self.assertTrue(
            self.game.is_in_check('red')
        )

        self.assertEqual(
            self.game.get_game_state(),
            "UNFINISHED"
        )

    def test_black_check_2(self):
        self.game._board = copy.deepcopy( XiangqiGame.BLANK_BOARD )
        red_general = General('red', 'e', 2)

        black_soldier = Soldier('black', 'e', 4)
        black_general = General('black', 'e', 10)

        self.game._board[2]['e'] = red_general
        self.game._board[4]['e'] = black_soldier
        self.game._board[10]['e'] = black_general

        self.game._red_pieces = {
            'G': red_general
        }

        self.game._black_pieces = {
            'G': black_general,
            'S1': black_soldier
        }

        self.game._current_turn = "black"

        self.assertFalse(
            self.game.is_in_check('red')
        )

        self.game.make_move('e4', 'e3')

        self.assertTrue(
            self.game.is_in_check('red')
        )

        self.assertEqual(
            self.game.get_game_state(),
            "UNFINISHED"
        )

    def test_black_win_stalemate_1(self):
        self.game._board = copy.deepcopy( XiangqiGame.BLANK_BOARD )
        red_general   = General('red', 'e', 1)
        red_advisor_1 = Advisor('red', 'f', 1)
        red_advisor_2 = Advisor('red', 'e', 2)

        black_soldier = Soldier('black', 'c', 2)
        black_general = General('black', 'e', 10)

        self.game._board[1]['e'] = red_general
        self.game._board[1]['f'] = red_advisor_1
        self.game._board[2]['e'] = red_advisor_2
        self.game._board[2]['c'] = black_soldier
        self.game._board[10]['e'] = black_general

        self.game._red_pieces = {
            'G': red_general,
            'A1': red_advisor_1,
            'A2': red_advisor_2
        }

        self.game._black_pieces = {
            'G': black_general,
            'S1': black_soldier
        }

        self.game._current_turn = "black"

        self.assertFalse(
            self.game.is_in_check('red')
        )

        self.game.make_move('c2', 'd2')

        self.assertFalse(
            self.game.is_in_check('red')
        )

        self.assertEqual(
            self.game.get_game_state(),
            "BLACK_WON"
        )

    def test_black_win_checkmate_1(self):
        self.game._board = copy.deepcopy( XiangqiGame.BLANK_BOARD )
        red_general   = General('red', 'd', 1)

        black_chariot = Chariot('black', 'c', 6)
        black_general = General('black', 'e', 8)

        self.game._board[1]['d'] = red_general
        self.game._board[6]['c'] = black_chariot
        self.game._board[8]['e'] = black_general

        self.game._red_pieces = {
            'G': red_general
        }

        self.game._black_pieces = {
            'G': black_general,
            'R1': black_chariot
        }

        self.game._current_turn = "black"

        self.assertFalse(
            self.game.is_in_check('red')
        )

        self.game.make_move('c6', 'd6')

        self.assertTrue(
            self.game.is_in_check('red')
        )

        self.assertEqual(
            self.game.get_game_state(),
            "BLACK_WON"
        )

    def test_convert_coord(self):
        self.assertEqual(
            self.game.convert_coord('a10'),
            { "row": 10, "column": 'a' }
        )

if __name__ == '__main__':
    unittest.main()