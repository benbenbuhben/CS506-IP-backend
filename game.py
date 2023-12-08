import random
from board import Board
from AI_player import ArtificialPlayer


class Game:
    def __init__(self, game_id, is_ai=False):
        self.game_id = game_id
        self.board = Board()
        self.players = {}
        self.is_ai = is_ai
        self.current_player = 'X'
        self.moves = []
        self.ai_player = ArtificialPlayer('O')

    def add_player(self, player_id):
        """Assigns a symbol to the new player."""
        if len(self.players) == 0:
            self.players[player_id] = "X"
        elif len(self.players) == 1:
            self.players[player_id] = "O"
        return self.players[player_id]

    @property
    def game_status(self):
        """Return the current status of the game."""
        if len(self.players) == 1:
            return "Waiting for other player"
        elif len(self.players) == 2:
            return "Active"
        else:
            return "Not started"

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def make_move(self, position):
        if self.board.make_move(position, self.current_player):
            self.moves.append(f"{self.current_player}:{position}")
            self.switch_player()
            return True
        return False

    def reset_game(self):
        self.board = Board()
        self.current_player = 'X'
        self.moves = []

    def get_game_state(self):
        winner, winning_line = self.board.check_winner()
        if winning_line and winning_line[0] in self.board.xCoordinates:
            winnerPlayer = 'X'
        elif winning_line and winning_line[0] in self.board.oCoordinates:
            winnerPlayer = 'O'
        else:
            winnerPlayer = None
        return {
            "game_id": self.game_id,
            "board": self.board.get_board(),
            "current_player": self.current_player,
            "winner": winner,
            "winning_line": winning_line,
            "draw": self.board.is_full() and not winner,
            "moves": self.moves,
            "game_status": self.game_status,
            'winnerPlayer': winnerPlayer
        }