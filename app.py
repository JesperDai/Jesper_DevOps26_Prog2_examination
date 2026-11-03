
from datetime import date

import pandas as pd
import plotly.express as px
from flask import Flask, jsonify, render_template, request

from application.func import get_weather_data, convert_weather_data_to_list

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route("/")
def home():
    return render_template("startsida.html")

weather_data = get_weather_data(lat=59.33, lon=18.07)
resultat = convert_weather_data_to_list(weather_data)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def server_error(e):
    return render_template("503.html"), 503

if __name__ == "__main__":
    app.run(host='127.0.0.1', port = 5000, debug=True)