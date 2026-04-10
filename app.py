from flask import Flask, render_template, request, redirect, url_for
import os
import matplotlib
matplotlib.use('Agg')

from main import create_state, apply_choice, daily_update
from scenarios import get_random_scenario, initialize_scenarios

app = Flask(__name__)

# =========================
# GLOBAL GAME STATE
# =========================
game_state = None
current_scenario = None


# =========================
# HOME PAGE
# =========================
@app.route("/")
def home():
    return render_template("index.html")


# =========================
# START GAME
# =========================
@app.route("/start")
def start():
    global game_state, current_scenario

    game_state = create_state()
    initialize_scenarios()
    current_scenario = get_random_scenario()

    return redirect(url_for("game"))


# =========================
# GAME PAGE
# =========================
@app.route("/game")
def game():
    global game_state, current_scenario

    if game_state is None:
        return redirect(url_for("home"))

    return render_template(
        "game.html",
        state=game_state,
        scenario=current_scenario
    )


# =========================
# HANDLE DECISION
# =========================
@app.route("/decision/<choice>")
def decision(choice):
    global game_state, current_scenario

    if game_state is None:
        return redirect(url_for("home"))

    # Map choice
    if choice == "1":
        selected = current_scenario["good"]
    elif choice == "2":
        selected = current_scenario["neutral"]
    else:
        selected = current_scenario["bad"]

    # Apply effects
    apply_choice(game_state, selected)
    daily_update(game_state)

    game_state["day"] += 1

    # Next scenario
    current_scenario = get_random_scenario()

    # End condition
    if game_state["day"] > 15:
        return redirect(url_for("end"))

    return redirect(url_for("game"))


# =========================
# END PAGE
# =========================
@app.route("/end")
def end():
    global game_state

    return render_template("end.html", state=game_state)


# =========================
# RUN
# =========================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)