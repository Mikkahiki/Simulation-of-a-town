from flask import Flask, render_template, send_from_directory, jsonify
import os
import matplotlib
matplotlib.use('Agg')

# IMPORT YOUR GAME
from main import run_game
from export_data import export_results

app = Flask(__name__)

# =========================
# ENSURE FILES EXIST
# =========================

def ensure_files():
    files = ["co2_temp_graph.png", "temp_graph.png", "results.json"]
    
    for file in files:
        if not os.path.exists(file):
            with open(file, "w") as f:
                if file.endswith(".json"):
                    f.write("{}")

ensure_files()

# =========================
# ROUTES
# =========================

# HOME DASHBOARD
@app.route("/")
def home():
    return render_template("index.html")


# GAME PAGE (NEW)
@app.route("/game")
def game():
    return render_template("game.html")


# RUN SIMULATION (BUTTON CALL)
@app.route("/run")
def run():
    state = run_game()  # <-- MAKE SURE run_game RETURNS state
    export_results(state)
    return jsonify({"status": "Simulation completed"})


# LIVE DATA (for charts)
@app.route("/results")
def results():
    if os.path.exists("results.json"):
        with open("results.json") as f:
            return jsonify(eval(f.read()))
    return jsonify({})


# SERVE FILES (graphs, images)
@app.route('/files/<path:path>')
def files(path):
    return send_from_directory('.', path)


# =========================
# START SERVER
# =========================

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)