import os
from flask import Flask, jsonify, request
from flask_socketio import SocketIO, emit, join_room
from flask_cors import CORS
from game import Game
from gevent import monkey
from dotenv import load_dotenv
import json

# Apply gevent monkey patching
monkey.patch_all()

# Load environment variables
load_dotenv()

host = os.environ.get("HOST", "localhost")
port = int(os.environ.get("PORT", 5001))

# Initialize Flask app
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

# Enable CORS for all routes
CORS(app)

# Initialize SocketIO with gevent
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="gevent")

# Dictionary to store games
games = {}


# Routes
@app.route("/")
def hello():
    return "Hello, World!"


@socketio.on("test_connection")
def handle_test_connection(data):
    print("Test Connection Received:", data)
    emit("connection_response", {"message": "Connection Successful"})


@app.route("/new_game", methods=["POST"])
def new_game():
    game_id = generate_unique_game_id()
    is_ai = request.json.get("ai")
    games[game_id] = Game(game_id, is_ai=is_ai)
    return jsonify({"game_id": game_id}), 200


@socketio.on("join_game")
def handle_join_game(data):
    player_id = request.sid
    game_id = data.get("game_id")
    join_room(game_id)
    game = games.get(game_id)

    if game:
        # Add player and get their assigned symbol
        symbol = game.add_player(player_id)

        # Get the general game state
        general_game_state = game.get_game_state()

        # Emit the general game state to the room (without player_symbol)
        emit("game_state", general_game_state, room=game_id, include_self=False)

        # Emit personalized game state to the player who just joined
        personalized_game_state = general_game_state.copy()
        personalized_game_state["player_symbol"] = symbol
        emit("game_state", personalized_game_state, to=player_id)

        if game.is_ai and len(game.players) == 1:
            # Add AI player
            symbol = game.add_player("ai")
            # Emit personalized game state to the AI player
            personalized_game_state = general_game_state.copy()
            personalized_game_state["player_symbol"] = symbol
            emit("game_state", personalized_game_state, to="ai")
        else:
            # Emit personalized game state to other players
            for pid in game.players:
                if pid != player_id:  # Skip the player who just joined
                    personalized_game_state = general_game_state.copy()
                    personalized_game_state["player_symbol"] = game.players[pid]
                    emit("game_state", personalized_game_state, to=pid)
    else:
        emit("game_error", {"error": "Game not found"}, to=player_id)


@socketio.on("make_move")
def handle_make_move(data):
    print("Received move:", data)
    game_id = data.get("game_id")
    position = data.get("position")

    game = games.get(game_id)
    if not game:
        print("Game not found")
        emit("game_error", {"error": "Game not found"})
        return

    if game.make_move(position):
        for pid, symbol in game.players.items():
            personalized_game_state = game.get_game_state()
            personalized_game_state["player_symbol"] = symbol
            emit("game_state", personalized_game_state, to=pid)
            print(game.get_game_state())
    if game.is_ai and game.current_player == "O":
        # AI player move
        position = game.ai_player.get_move(game.board)
        game.make_move(position)
        for pid, symbol in game.players.items():
            personalized_game_state = game.get_game_state()
            personalized_game_state["player_symbol"] = symbol
            emit("game_state", personalized_game_state, to=pid)
    else:
        print("Invalid move")
        emit("game_error", {"error": "Invalid move"})


@socketio.on("reset_game")
def handle_reset_game(data):
    game_id = data.get("game_id")
    game = games.get(game_id)
    if game:
        game.reset_game()
        updated_game_state = game.get_game_state()
        for pid, symbol in game.players.items():
            personalized_game_state = updated_game_state.copy()
            personalized_game_state["player_symbol"] = symbol
            emit("game_state", personalized_game_state, to=pid)
    else:
        emit("game_error", {"error": "Game not found"}, room=game_id)


# Helper function to generate a unique game ID
def generate_unique_game_id():
    import uuid

    return str(uuid.uuid4())


# Main entry point
if __name__ == "__main__":
    socketio.run(app, host=host, debug=False, port=port)
