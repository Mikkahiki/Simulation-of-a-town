from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/<path:path>')
def send_file(path):
    return send_from_directory('', path)

if __name__ == "__main__":
    app.run()