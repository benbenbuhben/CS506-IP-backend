class Board:
    def __init__(self):
        self.board = [" " for _ in range(25)]
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
        return 0 <= position < 25 and self.board[position] == " "

    def check_winner(self):
        win_conditions = [
            [0, 1, 2, 3, 4],
            [5, 6, 7, 8, 9],
            [10, 11, 12, 13, 14],
            [15, 16, 17, 18, 19],
            [20, 21, 22, 23, 24],  # Horizontals
            [0, 5, 10, 15, 20],
            [1, 6, 11, 16, 21],
            [2, 7, 12, 17, 22],
            [3, 8, 13, 18, 23],
            [4, 9, 14, 19, 24],  # Verticals
            [0, 6, 12, 18, 24],
            [4, 8, 12, 16, 20],  # Diagonals
        ]
        for condition in win_conditions:
            if (
                self.board[condition[0]]
                == self.board[condition[1]]
                == self.board[condition[2]]
                == self.board[condition[3]]
                == self.board[condition[4]]
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
        for i in range(25):
            if i not in self.xCoordinates and i not in self.oCoordinates:
                possible_moves.append(i)
        return possible_moves