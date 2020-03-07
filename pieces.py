class Piece:
    """
    """
    def __init__(self, color, start_column, start_row):
        """
        """
        self._color  = color
        self._column = start_column
        self._row    = start_row

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

        return True

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

        #TODO add further move logic

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

        #TODO add further move logic

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

        #TODO add further move logic

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

        #TODO add further move logic

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

        #TODO add further move logic

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

        #TODO add further move logic
