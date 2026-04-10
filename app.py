from flask import Flask, render_template, request, jsonify
import json

from main import start_game, next_turn

app = Flask(__name__)

# store game state (simple version)
game_state = {}

# =========================
# PAGES
# =========================

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/game")
def game():
    return render_template("game.html")


# =========================
# API
# =========================

@app.route("/start", methods=["POST"])
def start():
    global game_state
    game_state = start_game()
    game_state = next_turn(game_state, None)  # load first scenario
    return jsonify(game_state)


@app.route("/choice", methods=["POST"])
def choice():
    global game_state
    data = request.json
    choice = data["choice"]   # "good", "neutral", "bad"

    game_state = next_turn(game_state, choice)

    return jsonify(game_state)


# =========================
# RUN
# =========================

if __name__ == "__main__":
    app.run(debug=True)