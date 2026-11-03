
from flask import Flask, request

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route("/")
def home():
    return "index.html"
