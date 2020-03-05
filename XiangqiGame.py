# Author: Matthew Yang
# Date: 03/01/2020
# Description:

from pieces import Piece, Advisor, Cannon, Chariot, Elephant, General, Horse, Soldier

class XiangqiGame:
    """
    """
    BLANK_BOARD = {
            # a    b    c    d    e    f    g    h    i
        10: ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
        9:  ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
        8:  ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
        7:  ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
        6:  ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
        # RIVER #########################################
        5:  ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
        4:  ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
        3:  ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
        2:  ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
        1:  ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    }

    def __init__(self):
        """
        """
        self._game_state   = "UNFINISHED"
        self._current_turn = "red"
        self._red_pieces   = self.initialize_pieces("red")
        self._black_pieces = self.initialize_pieces("black")
        self._board        = self.initialize_board(self._red_pieces, self._black_pieces)

    def get_game_state(self):
        """
        """
        return self._game_state

    def get_current_turn(self):
        """
        """
        return self._current_turn

    def toggle_turn(self):
        """
        """
        if self._current_turn == "red":
            self._current_turn = "black"
        else:
            self._current_turn = "red"

    def is_in_check(self, color):
        """
        """

    def make_move(self, from_coord, to_coord):
        """
        """

    def initialize_board(self, red_pieces, black_pieces):
        """
        """


    def initialize_pieces(self, color):
        """
        """
        # Piece Abbreviations #
        #######################
        # A -> Advisor
        # C -> Cannon
        # R -> Chariot
        # E -> Elephant
        # G -> General
        # H -> Horse
        # S -> Soldier
        return {
            'G': General(color, None, None),
            'A1': Advisor(color, None, None),
            'A2': Advisor(color, None, None),
            'E1': Elephant(color, None, None),
            'E2': Elephant(color, None, None),
            'H1': Horse(color, None, None),
            'H2': Horse(color, None, None),
            'R1': Chariot(color, None, None),
            'R2': Chariot(color, None, None),
            'C1': Cannon(color, None, None),
            'C2': Cannon(color, None, None),
            'S1': Soldier(color, None, None),
            'S2': Soldier(color, None, None),
            'S3': Soldier(color, None, None),
            'S4': Soldier(color, None, None),
            'S5': Soldier(color, None, None),
        }