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

        lenOfAiMoves = len(ai_moves)
        lenOfOpponentMoves = len(opponent_moves)


        # find winning options
        if lenOfAiMoves >= 2:
            if 0 in ai_moves and 1 in ai_moves and 2 in possible_moves:
                return 2
            if 3 in ai_moves and 4 in ai_moves and 5 in possible_moves:
                return 5
            if 6 in ai_moves and 7 in ai_moves and 8 in possible_moves:
                return 8
            # check vertical
            if 0 in ai_moves and 3 in ai_moves and 6 in possible_moves:
                return 6
            if 1 in ai_moves and 4 in ai_moves and 7 in possible_moves:
                return 7
            if 2 in ai_moves and 5 in ai_moves and 8 in possible_moves:
                return 8
            # check diagonal
            if 0 in ai_moves and 4 in ai_moves and 8 in possible_moves:
                return 8
            if 2 in ai_moves and 4 in ai_moves and 6 in possible_moves:
                return 6
        elif lenOfAiMoves == 1:
            if 0 in ai_moves and 8 in ai_moves and 4 in possible_moves:
                return 4
            if 2 in ai_moves and 6 in ai_moves and 4 in possible_moves:
                return 4
            if 1 in ai_moves and 7 in ai_moves and 4 in possible_moves:
                return 4
            if 3 in ai_moves and 5 in ai_moves and 4 in possible_moves:
                return 4
            if 0 in ai_moves and 2 in ai_moves and 1 in possible_moves:
                return 1
            if 0 in ai_moves and 6 in ai_moves and 3 in possible_moves:
                return 3
            if 2 in ai_moves and 8 in ai_moves and 5 in possible_moves:
                return 5
            if 6 in ai_moves and 8 in ai_moves and 7 in possible_moves:
                return 7
        else:
            if 0 in possible_moves and 1 in possible_moves and 2 in possible_moves:
                return 0
            if 3 in possible_moves and 4 in possible_moves and 5 in possible_moves:
                return 3
            if 6 in possible_moves and 7 in possible_moves and 8 in possible_moves:
                return 6
            # check vertical
            if 0 in possible_moves and 3 in possible_moves and 6 in possible_moves:
                return 0
            if 1 in possible_moves and 4 in possible_moves and 7 in possible_moves:
                return 1
            if 2 in possible_moves and 5 in possible_moves and 8 in possible_moves:
                return 2
            # check diagonal
            if 0 in possible_moves and 4 in possible_moves and 8 in possible_moves:
                return 0
            if 2 in possible_moves and 4 in possible_moves and 6 in possible_moves:
                return 2
        # find blocking options
        if lenOfOpponentMoves >= 2:
            if 0 in opponent_moves and 1 in opponent_moves and 2 in possible_moves:
                return 2
            if 3 in opponent_moves and 4 in opponent_moves and 5 in possible_moves:
                return 5
            if 6 in opponent_moves and 7 in opponent_moves and 8 in possible_moves:
                return 8
            # check vertical
            if 0 in opponent_moves and 3 in opponent_moves and 6 in possible_moves:
                return 6
            if 1 in opponent_moves and 4 in opponent_moves and 7 in possible_moves:
                return 7
            if 2 in opponent_moves and 5 in opponent_moves and 8 in possible_moves:
                return 8
            # check diagonal
            if 0 in opponent_moves and 4 in opponent_moves and 8 in possible_moves:
                return 8
            if 2 in opponent_moves and 4 in opponent_moves and 6 in possible_moves:
                return 6
        elif lenOfOpponentMoves == 1:
            if 0 in opponent_moves and 8 in opponent_moves and 4 in possible_moves:
                return 4
            if 2 in opponent_moves and 6 in opponent_moves and 4 in possible_moves:
                return 4
            if 1 in opponent_moves and 7 in opponent_moves and 4 in possible_moves:
                return 4
            if 3 in opponent_moves and 5 in opponent_moves and 4 in possible_moves:
                return 4
            if 0 in opponent_moves and 2 in opponent_moves and 1 in possible_moves:
                return 1
            if 0 in opponent_moves and 6 in opponent_moves and 3 in possible_moves:
                return 3
            if 2 in opponent_moves and 8 in opponent_moves and 5 in possible_moves:
                return 5
            if 6 in opponent_moves and 8 in opponent_moves and 7 in possible_moves:
                return 7
        return random.choice(possible_moves)