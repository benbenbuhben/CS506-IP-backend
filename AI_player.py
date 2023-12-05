import random


class ArtificialPlayer:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self, board):
        """
        This function purpose is get move
        """
        possible_moves = board.get_possible_moves()
        best_move = self.best_move(board, possible_moves)
        return best_move
    
    def best_move(self, board, possible_moves):
        """
        This function purpose is best move
        """
        # get moves of AI player and opponent player
        if self.symbol == 'X':
            ai_moves = board.xCoordinates
            opponent_moves = board.oCoordinates
        else:
            ai_moves = board.oCoordinates
            opponent_moves = board.xCoordinates
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
        win_possibility = 0
        for condition in win_conditions:
            for con in condition:
                if con in ai_moves:
                    win_possibility += 1
            if win_possibility == 4:
                for con in condition:
                    if con in possible_moves:
                        return con
            win_possibility = 0
        for condition in win_conditions:
            for con in condition:
                if con in opponent_moves:
                    win_possibility += 1
            if win_possibility == 4:
                for con in condition:
                    if con in possible_moves:
                        return con
            win_possibility = 0        
        return random.choice(possible_moves)