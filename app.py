from flask import Flask, render_template, redirect, url_for
import os
import matplotlib
matplotlib.use('Agg')



# ✅ NEW ENGINE IMPORTS
from main import start_game, next_turn
import json

app = Flask(__name__)


import matplotlib.pyplot as plt
from flask import Response
import io

@app.route("/graph")
def graph():
    global game_state

    if game_state is None:
        return "No data"

    plt.figure()
    plt.plot(game_state["co2_history"])

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    return Response(img.getvalue(), mimetype='image/png')
# =========================
# GLOBAL GAME STATE
# =========================
game_state = None


# =========================
# HOME PAGE
# =========================
@app.route("/")
def home():
    state = start_game()


# =========================
# START GAME
# =========================
@app.route("/start")
def start():
    global game_state

    game_state = start_game()

    return redirect(url_for("game"))


# =========================
# GAME PAGE
# =========================
@app.route("/game")
def game():
    global game_state

    if game_state is None:
        return redirect(url_for("home"))

    scenario = game_state.get("current_scenario")

    return render_template(
        "game.html",
        state=game_state,
        scenario=scenario
    )


# =========================
# HANDLE DECISION
# =========================
@app.route("/decision/<choice>")
def decision(choice):
    global game_state

    if game_state is None:
        return redirect(url_for("home"))

    # Map choice to engine
    if choice == "1":
        game_state = next_turn(game_state, "good")
    elif choice == "2":
        game_state = next_turn(game_state, "neutral")
    else:
        game_state = next_turn(game_state, "bad")

    # END CONDITION
    if game_state["day"] > 15:
        return redirect(url_for("end"))

    return redirect(url_for("game"))


# =========================
# END PAGE
# =========================
@app.route("/end")
def end():
    global game_state

    if game_state is None:
        return redirect(url_for("home"))

    return render_template("end.html", state=game_state)


# =========================
# HEALTH CHECK (FOR RENDER)
# =========================
@app.route("/health")
def health():
    return "OK", 200


# =========================
# RUN LOCAL ONLY
# =========================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)