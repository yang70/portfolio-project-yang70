import unittest
from XiangqiGame import XiangqiGame
from pieces import Piece, Advisor, Cannon, Chariot, Elephant, General, Horse, Soldier

class XiangqiGameTester(unittest.TestCase):
    def setUp(self):
        self.game = XiangqiGame()

    def test_data_members(self):
        self.assertEqual(
            self.game._game_state,
            "UNFINISHED"
        )

        self.assertEqual(
            self.game._current_turn,
            "red"
        )

        self.assertEqual(
            self.game._red_pieces,
            {
                'G': General("red", None, None),
                'A1': Advisor("red", None, None),
                'A2': Advisor("red", None, None),
                'E1': Elephant("red", None, None),
                'E2': Elephant("red", None, None),
                'H1': Horse("red", None, None),
                'H2': Horse("red", None, None),
                'R1': Chariot("red", None, None),
                'R2': Chariot("red", None, None),
                'C1': Cannon("red", None, None),
                'C2': Cannon("red", None, None),
                'S1': Soldier("red", None, None),
                'S2': Soldier("red", None, None),
                'S3': Soldier("red", None, None),
                'S4': Soldier("red", None, None),
                'S5': Soldier("red", None, None),
            }
        )

        self.assertDictEqual(
            self.game._black_pieces,
            {
                'G': General("black", None, None),
                'A1': Advisor("black", None, None),
                'A2': Advisor("black", None, None),
                'E1': Elephant("black", None, None),
                'E2': Elephant("black", None, None),
                'H1': Horse("black", None, None),
                'H2': Horse("black", None, None),
                'R1': Chariot("black", None, None),
                'R2': Chariot("black", None, None),
                'C1': Cannon("black", None, None),
                'C2': Cannon("black", None, None),
                'S1': Soldier("black", None, None),
                'S2': Soldier("black", None, None),
                'S3': Soldier("black", None, None),
                'S4': Soldier("black", None, None),
                'S5': Soldier("black", None, None),
            }
        )


if __name__ == '__main__':
    unittest.main()