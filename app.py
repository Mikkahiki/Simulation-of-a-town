from flask import Flask, render_template, send_from_directory
import os
import matplotlib
matplotlib.use('Agg')

app = Flask(__name__)

if not os.path.exists("co2_temp_graph.png"):
    open("co2_temp_graph.png","a").close()

if not os.path.exists("temp_graph.png"):
    open("temp_graph.png","a").close()

if not os.path.exists("results.json"):
    with open("results.json","w") as f:
        f.write("{}")

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/<path:path>')
def send_file(path):
    return send_from_directory('.', path)

if __name__ == "__main__":
    port = int(os.environ.get("PORT",10000))
    app.run(host="0.0.0.0",port=port)   