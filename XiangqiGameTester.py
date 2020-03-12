import unittest
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

    def test_integration(self):
        self.assertTrue(
            self.game.make_move('h3', 'h10')
        )

        self.assertFalse(
            self.game.make_move('f10', 'e9')
        )

    def test_convert_coord(self):
        self.assertEqual(
            self.game.convert_coord('a10'),
            { "row": 10, "column": 'a' }
        )

if __name__ == '__main__':
    unittest.main()