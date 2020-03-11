# Author: Matthew Yang
# Date: 03/01/2020
# Description:

import copy
from pieces import Piece, Advisor, Cannon, Chariot, Elephant, General, Horse, Soldier

class XiangqiGame:
    """
    """
    BLANK_BOARD = {

         1: { 'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None, 'g': None, 'h': None, 'i': None},
         2: { 'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None, 'g': None, 'h': None, 'i': None},
         3: { 'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None, 'g': None, 'h': None, 'i': None},
         4: { 'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None, 'g': None, 'h': None, 'i': None},
         5: { 'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None, 'g': None, 'h': None, 'i': None},
         # RIVER ###############################################################################################
         6: { 'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None, 'g': None, 'h': None, 'i': None},
         7: { 'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None, 'g': None, 'h': None, 'i': None},
         8: { 'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None, 'g': None, 'h': None, 'i': None},
         9: { 'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None, 'g': None, 'h': None, 'i': None},
        10: { 'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None, 'g': None, 'h': None, 'i': None},
    }

    # Piece Abbreviations #
    #######################
    # A -> Advisor
    # C -> Cannon
    # R -> Chariot
    # E -> Elephant
    # G -> General
    # H -> Horse
    # S -> Soldier
    STARTING_COORDINATES = {
        'red': {
            'G': ('e', 1),
            'A1': ('d', 1),
            'A2': ('f', 1),
            'E1': ('c', 1),
            'E2': ('g', 1),
            'H1': ('b', 1),
            'H2': ('h', 1),
            'R1': ('a', 1),
            'R2': ('i', 1),
            'C1': ('b', 3),
            'C2': ('h', 3),
            'S1': ('a', 4),
            'S2': ('c', 4),
            'S3': ('e', 4),
            'S4': ('g', 4),
            'S5': ('i', 4),
        },
        'black': {
            'G': ('e', 10),
            'A1': ('d', 10),
            'A2': ('f', 10),
            'E1': ('c', 10),
            'E2': ('g', 10),
            'H1': ('b', 10),
            'H2': ('h', 10),
            'R1': ('a', 10),
            'R2': ('i', 10),
            'C1': ('b', 8),
            'C2': ('h', 8),
            'S1': ('a', 7),
            'S2': ('c', 7),
            'S3': ('e', 7),
            'S4': ('g', 7),
            'S5': ('i', 7),
        }
    }

    OPPOSITE_COLOR_DICT = {
        "red": "black",
        "black": "red"
    }

    def __init__(self):
        """
        """
        self._game_state   = "UNFINISHED"
        self._current_turn = "red"
        self._red_pieces   = self.initialize_pieces("red")
        self._black_pieces = self.initialize_pieces("black")
        self._board        = self.initialize_board()

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
        # Find the coordinates of the general of the given color
        generals_coords = getattr(self, f"_{color}_pieces")["G"].get_coordinates()
        # Get the opposing colors pieces
        opposite_color  = self.OPPOSITE_COLOR_DICT[color]
        opposing_pieces = getattr(self, f"_{opposite_color}_pieces")

        # Iterate the opposing colors pieces and if the piece is still in play, check if
        # the generals coordinates are a valid move for the given piece and return True if so.
        for piece in opposing_pieces.values():
            if piece.is_in_play():
                if piece.valid_move(generals_coords[0], generals_coords[1], self._board):
                    return True

        return False

    def make_move(self, from_coord, to_coord):
        """
        """
        if self._game_state != "UNFINISHED":
            return False

        from_coord    = convert_coord(from_coord)
        to_coord      = convert_coord(to_coord)

        piece = self._board[from_coord[1]][from_coord[0]]

        if piece == None or piece.get_color() != self._current_turn:
            return False

        if not piece.valid_move(to_coord[1], to_coord[0], self._board):
            return False

        #TODO Does move expose General?

        #TODO Does move put current turn in check?

        #TODO Complete move and capture piece if necessary

        #TODO Check if winner and update game state if so

        #TODO Toggle turn

        return True

    def convert_coord(self, coord):
        """
        """
        coord = list(coord)
        coord[1] = int(coord[1])

        return coord

    def print_red(text):
        """
        """
        print("\033[91m {}\033[00m" .format(text))

    def print_black(text):
        """
        """
        print("\033[98m {}\033[00m" .format(text))

    def print_board(self):
        """
        """
        print('   a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i')
        row_counter = 0
        for row_num, row in self._board.items():
            if row_num == 10:
                current_row = str(row_num)
            else:
                current_row = ' ' + str(row_num)

            for column in range(97,106):
                piece = row[chr(column)] or '-'
                current_row += ' ' + str(piece)

            print(current_row)

    def initialize_board(self):
        """
        """
        board = copy.deepcopy(self.BLANK_BOARD)
        for key, piece in self._red_pieces.items():
            coords = self.STARTING_COORDINATES['red'][key]
            piece.set_coordinates(*coords)
            board[coords[1]][coords[0]] = piece

        for key, piece in self._black_pieces.items():
            coords = self.STARTING_COORDINATES['black'][key]
            piece.set_coordinates(*coords)
            board[coords[1]][coords[0]] = piece

        return board

    def initialize_pieces(self, color):
        """
        """
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