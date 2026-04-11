import io
import json
import os

import matplotlib

from analysis import full_analysis
from endings import check_ending

matplotlib.use('Agg')

import matplotlib.pyplot as plt
from flask import Flask, Response, jsonify, redirect, render_template, url_for

# ✅ ENGINE IMPORTS
from main import create_state, next_turn, start_game

app = Flask(__name__)

# =========================
# GLOBAL GAME STATE
# =========================
game_state = None


# =========================
# GRAPH ROUTE
# =========================
@app.route("/graph")
def graph():
    global game_state

    if game_state is None or len(game_state["co2_history"]) == 0:
        return "No data"

    plt.figure()
    plt.plot(game_state["co2_history"])
    plt.title("CO2 Emissions Over Time")
    plt.xlabel("Day")
    plt.ylabel("CO2")

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    return Response(img.getvalue(), mimetype='image/png')


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
    global game_state

    print("START ROUTE HIT")   # 👈 add this

    game_state = start_game()

    print("GAME STATE CREATED:", game_state)  # 👈 add this

    return redirect(url_for("game"))


# =========================
# GAME PAGE
# =========================
@app.route("/game")
def game():
    global game_state

    print("GAME ROUTE HIT")

    if game_state is None:
        print("No game state → redirecting home")
        return redirect(url_for("home"))

    scenario = game_state.get("current_scenario")

    return render_template(
        "game.html",
        state=game_state,
        scenario=scenario
    )

#==========================
# GRAPHS MORE
#==========================
@app.route("/api/graphs")
def api_graphs():
    global game_state

    if game_state is None:
        return jsonify({"error": "No data"})

    return jsonify({
        "co2": game_state["co2_history"],
        "temp": game_state["temp_history"],
        "eco": game_state["eco_history"],
        "pub": game_state["public_history"]
    })
    
# =========================
# HANDLE DECISION (WEB PAGE)
# =========================
@app.route("/decision/<choice>")
def decision(choice):
    global game_state

    if game_state is None:
        return redirect(url_for("home"))

    if game_state.get("game_over"):
        return redirect(url_for("end"))

    # Apply decision
    if choice == "1":
        game_state = next_turn(game_state, "good")
    elif choice == "2":
        game_state = next_turn(game_state, "neutral")
    else:
        game_state = next_turn(game_state, "bad")

    # ✅ END CONDITION
    if game_state["day"] > 15:
        game_state["game_over"] = True
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
# HEALTH CHECK
# =========================
@app.route("/health")
def health():
    return "OK", 200


# =========================
# API: GET STATE
# =========================
@app.route("/api/state")
def api_state():
    global game_state

    if game_state is None:
        game_state = start_game()
        game_state["game_over"] = False

    if game_state["day"] > 15:
      game_state["game_over"] = True

    if "ending" not in game_state:
        game_state["ending"] = check_ending(game_state)
        game_state["analysis"] = full_analysis(game_state)

    scenario = game_state.get("current_scenario")

    if scenario is None and not game_state.get("game_over"):
        from scenarios import get_random_scenario
        scenario = get_random_scenario()
        game_state["current_scenario"] = scenario

    return jsonify({
        "state": game_state,
        "scenario": scenario,
        "game_over": game_state.get("game_over", False)
    })


# =========================
# API: DECISION
# =========================
@app.route("/api/decision/<choice>")
def api_decision(choice):
    global game_state

    if game_state is None:
        return jsonify({"error": "No game"})

    if game_state.get("game_over"):
        return jsonify({"error": "Game over"})

    # Apply decision
    if choice == "1":
        game_state = next_turn(game_state, "good")
    elif choice == "2":
        game_state = next_turn(game_state, "neutral")
    else:
        game_state = next_turn(game_state, "bad")

    # ✅ FINAL TURN HANDLING
    if game_state["day"] > 15:
        game_state["game_over"] = True

        # 🔥 THIS WAS MISSING
        game_state["ending"] = check_ending(game_state)
        game_state["analysis"] = full_analysis(game_state)

    return jsonify({
        "status": "ok",
        "game_over": game_state["game_over"]
    })


# =========================
# API: RESTART GAME
# =========================
@app.route("/api/restart")
def restart():
    global game_state

    game_state = start_game()
    game_state["game_over"] = False

    return jsonify({"status": "restarted"})


# =========================
# RUN LOCAL
# =========================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)