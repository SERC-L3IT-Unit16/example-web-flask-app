from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!\nUnit 16 demo flask app."
