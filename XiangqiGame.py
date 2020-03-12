# Author: Matthew Yang
# Date: 03/01/2020
# Description: Implementation of the game Chinese Chess, or Xiangqi.  This file represents the game
#              class and imports the different piece classes from a separate file.

import copy
from pieces import Piece, Advisor, Cannon, Chariot, Elephant, General, Horse, Soldier

class XiangqiGame:
    """
    The overarching class representing the chess game and implementing the API for
    interacting with the game and getting the game state.
    """
    # A constant of a blank game board of nested dicts. Used when instantiating a game as well as
    # for testing.
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
    #
    # Constant containing the starting coordinates for the red and black pieces, used when
    # initializing a new game.
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

    # A constant helper that will return the opposite color to the key given
    OPPOSITE_COLOR_DICT = {
        "red": "black",
        "black": "red"
    }

    def __init__(self):
        """
        Initialization method that sets up the initial game state including instantiating
        red and black pieces and placing them in the game board
        """
        self._game_state   = "UNFINISHED"
        self._current_turn = "red"
        self._red_pieces   = self.initialize_pieces("red")
        self._black_pieces = self.initialize_pieces("black")
        self._board        = self.initialize_board()

    def get_game_state(self):
        """
        Returns the current game state string
        """
        return self._game_state

    def get_current_turn(self):
        """
        Returns the current colors turn as a string
        """
        return self._current_turn

    def toggle_turn(self):
        """
        Changes the current turn attribute to the opposite of current state
        """
        if self._current_turn == "red":
            self._current_turn = "black"
        else:
            self._current_turn = "red"

    def is_in_check(self, color, piece_to_ignore = None):
        """
        Method that takes a color string and checks the current state of the game,
        returning true if the given color is in a state of 'check' and false if
        not. Can also take a piece to ignore if checking whether a potential move
        would result in a check.
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
                # Can ignore a given piece, used when checking if a potential move would result in
                # a check by ignoring a piece that would otherwise be captured.
                if not piece_to_ignore or piece_to_ignore.get_coordinates() != piece.get_coordinates():
                    if piece.valid_move(generals_coords['column'], generals_coords['row'], self._board):
                        return True

        # If no piece has a valid move to the generals coordinates return false as the
        # player is not in check
        return False

    def make_move(self, from_coord, to_coord, alter_state = True):
        """
        Takes a from and to coordinate as a string of column and row (ex 'a1') and
        attempts to move the piece at the from coordinate to the to coordinate.  If
        the move is invalid it will return false, otherwise it will return true. If
        the alter state variable is true it will also execute the move and evaluate
        the current state of the game, updating as appropriate.
        """
        # Return false if game is over
        if self._game_state != "UNFINISHED":
            return False

        # Convert input to usable dicts
        from_coord_dict = self.convert_coord(from_coord)
        to_coord_dict   = self.convert_coord(to_coord)

        # Piece at from coordinates
        piece = self._board[from_coord_dict['row']][from_coord_dict['column']]

        # If there was no  piece at from coordinates or if the piece was the other players
        # color return false
        if piece == None or piece.get_color() != self._current_turn:
            return False

        # Return false if the move is not valid for the piece being moved
        if not piece.valid_move(to_coord_dict['column'], to_coord_dict['row'], self._board):
            return False

        # Check if the move exposes the general.  If the piece being moved is a General it
        # will check within it's own valid_move logic, otherwise check using the move_exposes_general
        # helper method.
        if piece.__class__.__name__ != "General" and self.move_exposes_general(from_coord_dict, to_coord_dict):
            return False

        # Return false if the move would put the current players general in check
        if self.move_puts_current_player_in_check(from_coord_dict, to_coord_dict):
            return False

        # Only change the game state and make the move if alter_state is true.  Allows for evaluating
        # a move without actually making the move.
        if alter_state:
            piece_at_destination = self._board[to_coord_dict['row']][to_coord_dict['column']]

            self._board[to_coord_dict['row']][to_coord_dict['column']] = piece
            self._board[from_coord_dict['row']][from_coord_dict['column']] = None

            piece.set_coordinates(to_coord_dict['column'], to_coord_dict['row'])

            if piece_at_destination:
                piece_at_destination.capture()

            self.toggle_turn()

            # Check if the last move ended the game by preventing the opposing player
            # from having any valid moves
            self.update_game_state(self._current_turn)

        return True

    def update_game_state(self, color):
        """
        Method that takes a color string and runs through all available moves for that color. If
        the color has no valid moves that would keep them out of check, it is either a stalemate
        or checkmate, and sets the other color as the winner in the game state
        """
        # Get the colors pieces to iterate
        pieces_to_check = getattr(self, f"_{color}_pieces")

        # Iterate all of the pieces of the given color, and if the piece is in play, try moving
        # that piece to every other spot on the board to see if there is a valid move.  If a valid
        # move is found the loops are exited and no further action is taken.
        for _key, piece in pieces_to_check.items():
            if  piece.is_in_play():
                piece_coords_dict = piece.get_coordinates()

                for row in range(1, 11):
                    for column in range(97, 106):
                        from_coord = piece_coords_dict['column'] + str(piece_coords_dict['row'])
                        to_coord   = chr(column) + str(row)

                        # Send false to the make move method to prevent the actual game state
                        # from being altered
                        if self.make_move(from_coord, to_coord, False):
                            return

        # If the check did not exit early, then there was no valid move and set the other color
        # as the winner.
        winning_color = self.OPPOSITE_COLOR_DICT[color]

        self._game_state = winning_color.upper() + "_WON"

    def move_puts_current_player_in_check(self, from_coord_dict, to_coord_dict):
        """
        This method takes from and to coordinates (as dicts) and checks if the given
        move puts the current player in a 'check' situation
        """
        # Backup the actual board so it can be restored after the check and create a copy
        board_backup = self._board
        board_copy   = copy.deepcopy( self._board )

        # Complete the move in the copy of the board and set the copy to the current
        # games board.
        piece_to_move = board_copy[from_coord_dict['row']][from_coord_dict['column']]
        board_copy[from_coord_dict['row']][from_coord_dict['column']] = None

        captured_piece = board_copy[to_coord_dict['row']][to_coord_dict['column']]
        board_copy[to_coord_dict['row']][to_coord_dict['column']] = piece_to_move

        self._board = board_copy

        # Checks if current state of the board would be a check for the current player. Sends
        # either a potentially captured piece or None to be ignored when checking
        result = self.is_in_check(self._current_turn, captured_piece)

        # Restore the board to the current state
        self._board = board_backup

        return result

    def move_exposes_general(self, from_coord_dict, to_coord_dict):
        """
        Checks if the given move causes the two generals to face each other. Assumes that the piece
        being moved is not a general, as they have their own logic for that situation.
        """
        black_general_coords = self._black_pieces['G'].get_coordinates()
        red_general_coords   = self._red_pieces['G'].get_coordinates()

        # If the generals columns do not line up return false
        if black_general_coords['column'] != red_general_coords['column']:
            return False

        column = black_general_coords['column']

        red_general_row   = red_general_coords['row']
        black_general_row = black_general_coords['row']

        # If the destination column is the same as the two generals and if the destination row
        # is between the two generals return False
        if to_coord_dict['column'] == column and (red_general_row <= to_coord_dict['row'] <= black_general_row):
            return False

        # Iterate through all the rows between the 2 generals checking if there is currently
        # a piece between
        for row in range(red_general_row + 1, black_general_row):
            piece_at_current = self._board[row][column]

            if piece_at_current:
                # If there is a piece at the current coordinates being checked, and that piece
                # is not the piece being moved return false. If it is the piece being moved
                # we know it is not moving to a blocking position since that was already checked
                # so continue checking coordinates as if it was not there.
                if piece_at_current.get_coordinates() != from_coord_dict:
                    return False

        return True

    def convert_coord(self, coord):
        """
        Converts a given string coordinate of column and row (ex 'a10') to a dictionary
        of the row as an integer and column a string
        """
        return { "row": int(coord[1:]), "column": coord[0] }

    def print_board(self):
        """
        Prints the current board
        """
        print('   a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i')
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
        Populates and returns a game board dict with red and black players
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
        Returns a hash of a full set of piece objects for the start of a game
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