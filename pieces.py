class Piece:
    """
    """
    def __init__(self, color, start_column, start_row):
        """
        """
        self._color   = color
        self._column  = start_column
        self._row     = start_row
        self._in_play = True

    def __eq__(self, other):
        """
        Overrides the default equality method for easier testing
        """
        return (
            self._color == other._color and
            self._column == other._column and
            self._row == other._row
        )

    def get_color(self):
        """
        """
        return self._color

    def valid_move(self, dest_column, dest_row, board):
        """
        """
        if dest_row == self._row and dest_column == self._column:
            return False

        if dest_row > 10 or dest_row < 1:
            return False

        if dest_column > 'i' or dest_column < 'a':
            return False

        piece_at_destination = board[dest_row][dest_column]

        if piece_at_destination and piece_at_destination.get_color() == self._color:
            return False

        return True

    def get_coordinates(self):
        """
        """
        return (self._column, self._row)

    def set_coordinates(self, column, row):
        """
        """
        self._column = column
        self._row    = row

    def is_in_play(self):
        """
        """
        return self._in_play

    def capture(self):
        """
        """
        self._in_play = False

class Advisor(Piece):
    """
    """
    BOUNDARIES = {
        'red': {
            'row_high': 3,
            'row_low': 1
        },
        'black': {
            'row_high': 10,
            'row_low': 8
        }
    }

    def __init__(self, color, start_column, start_row):
        """
        """
        super().__init__(color, start_column, start_row)

    def valid_move(self, dest_column, dest_row, board):
        """
        """
        # Check parent logic for move validity
        precheck_valid = super(Advisor, self).valid_move(dest_column, dest_row, board)

        # Return false if parent logic returns invalid move
        if not precheck_valid:
            return False

        if dest_column > 'f' or dest_column < 'd':
            return False

        if dest_row > self.BOUNDARIES[self._color]['row_high'] or dest_row < self.BOUNDARIES[self._color]['row_low']:
            return False

        if abs(dest_row - self._row) != 1 or abs(ord(dest_column) - ord(self._column)) != 1:
            return False

        return True

    def __str__(self):
        """
        """
        return "A"

class Cannon(Piece):
    """
    """
    def __init__(self, color, start_column, start_row):
        """
        """
        super().__init__(color, start_column, start_row)

    def valid_move(self, dest_column, dest_row, board):
        """
        """
        # Check parent logic for move validity
        precheck_valid = super(Cannon, self).valid_move(dest_column, dest_row, board)

        # Return false if parent logic returns invalid move
        if not precheck_valid:
            return False

        # Return false if moving diagonally
        if abs(ord(dest_column) - ord(self._column)) > 0 and abs(dest_row - self._row) > 0:
            return False

        piece_at_destination = board[dest_row][dest_column]
        piece_in_between     = None

        # True if moving up/down column
        if dest_column == self._column:
            # Set current to the lowest row so can iterate up
            if dest_row < self._row:
                current = dest_row + 1
                end     = self._row
            else:
                current = self._row + 1
                end     = dest_row

            # Iterate rows up to but not including end, checking if there
            # is a piece along the way
            while current < end:
                if board[current][dest_column]:
                    # Immediately return false if there are 2 pieces inbetween
                    if piece_in_between:
                        return False
                    else:
                        piece_in_between = True

                current += 1
        # Moving across row
        else:
            # Must convert the column characters to their Unicode value in order to iterate
            # through, converting back to the character when checking the board
            if dest_column < self._column:
                current = ord(dest_column) + 1
                end     = ord(self._column)
            else:
                current = ord(self._column) + 1
                end     = ord(dest_column)

            while current < end:
                if board[dest_row][chr(current)]:
                    if piece_in_between:
                        return False
                    else:
                        piece_in_between = True

                current += 1

        # Return false if there is a pice in between the destination but no
        # piece at the destination
        if piece_in_between and not piece_at_destination:
            return False

        # Returning true as if there is a piece at the destination it must be
        # of the opposite color (precheck checked for same color)
        return True

    def __str__(self):
        """
        """
        return "C"

class Chariot(Piece):
    """
    """
    def __init__(self, color, start_column, start_row):
        """
        """
        super().__init__(color, start_column, start_row)

    def valid_move(self, dest_column, dest_row, board):
        """
        """
        # Check parent logic for move validity
        precheck_valid = super(Chariot, self).valid_move(dest_column, dest_row, board)

        # Return false if parent logic returns invalid move
        if not precheck_valid:
            return False


        # Return false if moving diagonally
        if abs(ord(dest_column) - ord(self._column)) > 0 and abs(dest_row - self._row) > 0:
            return False

        # True if moving up/down column
        if dest_column == self._column:
            # Set current to the lowest row so can iterate up
            if dest_row < self._row:
                current = dest_row + 1
                end     = self._row
            else:
                current = self._row + 1
                end     = dest_row

            # Iterate rows up to but not including end, checking if there
            # is a piece along the way
            while current < end:
                if board[current][dest_column]:
                    # Return false if there is a piece in the way
                    return False

                current += 1
        # Moving across row
        else:
            # Must convert the column characters to their Unicode value in order to iterate
            # through, converting back to the character when checking the board
            if dest_column < self._column:
                current = ord(dest_column) + 1
                end     = ord(self._column)
            else:
                current = ord(self._column) + 1
                end     = ord(dest_column)

            while current < end:
                if board[dest_row][chr(current)]:
                    return False

                current += 1

        return True

    def __str__(self):
        """
        """
        return "R"

class Elephant(Piece):
    """
    """
    def __init__(self, color, start_column, start_row):
        """
        """
        super().__init__(color, start_column, start_row)

    def valid_move(self, dest_column, dest_row, board):
        """
        """
        # Check parent logic for move validity
        precheck_valid = super(Elephant, self).valid_move(dest_column, dest_row, board)

        # Return false if parent logic returns invalid move
        if not precheck_valid:
            return False

        # Verify not crossing the river
        if self._color == "red":
            if dest_row > 5:
                return False
        else:
            if dest_row < 6:
                return False

        # Return false if moving diagonally and not two spaces
        if not (abs(ord(dest_column) - ord(self._column)) == 2 and abs(dest_row - self._row) == 2):
            return False

        # Check if another piece is blocking in the direction moving
        if dest_row > self._row:
            if ord(dest_column) > ord(self._column):
                if board[dest_row - 1][chr(ord(dest_column) - 1)]:
                    return False
            else:
                if board[dest_row - 1][chr(ord(dest_column) + 1)]:
                    return False
        else:
            if ord(dest_column) > ord(self._column):
                if board[dest_row + 1][chr(ord(dest_column) - 1)]:
                    return False
            else:
                if board[dest_row + 1][chr(ord(dest_column) + 1)]:
                    return False

        return True

    def __str__(self):
        """
        """
        return "E"

class General(Piece):
    """
    """
    def __init__(self, color, start_column, start_row):
        """
        """
        super().__init__(color, start_column, start_row)

    def valid_move(self, dest_column, dest_row, board):
        """
        """
        # Check parent logic for move validity
        precheck_valid = super(General, self).valid_move(dest_column, dest_row, board)

        # Return false if parent logic returns invalid move
        if not precheck_valid:
            return False

        column_change_value = abs(ord(dest_column) - ord(self._column))
        row_change_value    = abs(dest_row - self._row)

        # Return false if moving diagonally
        if column_change_value > 0 and row_change_value > 0:
            return False

        # Return false if moving more than one
        if column_change_value > 1 or row_change_value > 1:
            return False

        if self._color == "red":
            current_row = dest_row + 1

            while current_row < 11:
                piece_found = board[current_row][dest_column]

                if piece_found:
                    if piece_found.__class__.__name__ == "General":
                        return False
                    else:
                        return True

                current_row += 1
        else:
            current_row = dest_row - 1

            while current_row > 0:
                piece_found = board[current_row][dest_column]

                if piece_found:
                    if piece_found.__class__.__name__ == "General":
                        return False
                    else:
                        return True

                current_row -= 1

        return True

    def __str__(self):
        """
        """
        return "G"

class Horse(Piece):
    """
    """
    def __init__(self, color, start_column, start_row):
        """
        """
        super().__init__(color, start_column, start_row)

    def valid_move(self, dest_column, dest_row, board):
        """
        """
        # Check parent logic for move validity
        precheck_valid = super(Horse, self).valid_move(dest_column, dest_row, board)

        # Return false if parent logic returns invalid move
        if not precheck_valid:
            return False

        # Given the row and column difference, check and see if they are found, which will return
        # the spot at the board to check if there is a blocking piece.  If there is a combination
        # not present it means the move is not valid.
        valid_move_dict = {
            1: {
                2: (self._row, chr(ord(self._column) - 1)),
                -2: (self._row, chr(ord(self._column) + 1))
            },
            -1: {
                2: (self._row, chr(ord(self._column) - 1)),
                -2: (self._row, chr(ord(self._column) + 1))
            },
            2: {
                1: (self._row - 1, self._column),
                -1: (self._row - 1, self._column)
            },
            -2: {
                1: (self._row + 1, self._column),
                -1: (self._row + 1, self._column)
            }
        }

        row_difference = self._row - dest_row
        column_difference = ord(self._column) - ord(dest_column)

        try:
            coords_to_check = valid_move_dict[row_difference][column_difference]

            # Return false if a piece was found at the coordinates as it is blocking
            if board[coords_to_check[0]][coords_to_check[1]]:
                return False

        # If a KeyError is raised it was an invalid move, return False
        except KeyError:
            return False

        return True

    def __str__(self):
        """
        """
        return "H"

class Soldier(Piece):
    """
    """
    def __init__(self, color, start_column, start_row):
        """
        """
        super().__init__(color, start_column, start_row)

    def valid_move(self, dest_column, dest_row, board):
        """
        """
        # Check parent logic for move validity
        precheck_valid = super(Soldier, self).valid_move(dest_column, dest_row, board)

        # Return false if parent logic returns invalid move
        if not precheck_valid:
            return False

        # If the destination is more than 1 space away in any direction it is invalid
        if abs(self._row - dest_row) > 1 or abs(ord(self._column) - ord(dest_column)) > 1:
            return False

        if self._color == "red":
            # Check moving backwards
            if dest_row < self._row:
                return False

            # Check if moving sideways before the river
            if self._row <= 5 and ord(self._column) - ord(dest_column) != 0:
                return False

        else:
            # Check moving backwards
            if dest_row > self._row:
                return False

            # Check if moving sideways before the river
            if self._row >= 6 and ord(self._column) - ord(dest_column) != 0:
                return False

        return True

    def __str__(self):
        """
        """
        return "S"
