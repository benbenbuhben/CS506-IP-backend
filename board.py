class Board:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.xCoordinates = list()
        self.oCoordinates = list()

    def make_move(self, position, player):
        if self.is_valid_move(position):
            self.board[position] = player
            if player == 'X':
                self.xCoordinates.append(position)
            else:
                self.oCoordinates.append(position)
            return True
        return False

    def is_valid_move(self, position):
        return 0 <= position < 9 and self.board[position] == " "

    def check_winner(self):
        win_conditions = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],  # Horizontals
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],  # Verticals
            [0, 4, 8],
            [2, 4, 6],  # Diagonals
        ]
        for condition in win_conditions:
            if (
                self.board[condition[0]]
                == self.board[condition[1]]
                == self.board[condition[2]]
                != " "
            ):
                return True, condition  # Return the winning line
        return False, None

    def is_full(self):
        return " " not in self.board

    def get_board(self):
        return self.board
    
    def get_possible_moves(self):
        """
        This function purpose is get possible moves
        """
        possible_moves = list()
        for i in range(1, 10):
            if i not in self.xCoordinates and i not in self.oCoordinates:
                possible_moves.append(i)
        return possible_moves