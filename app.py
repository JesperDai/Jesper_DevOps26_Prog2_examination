
from datetime import date

import pandas as pd
import plotly.express as px
from flask import Flask, jsonify, render_template, request

from application.func import get_weather_data, convert_weather_data_to_list

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route("/")
def home():
    return render_template("home.html")

weather_data = get_weather_data(lat=59.33, lon=18.07)
resultat = convert_weather_data_to_list(weather_data)

print(resultat)