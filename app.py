import pandas as pd
from flask import Flask, render_template, request

from application.func import get_weather_data

app = Flask(__name__, template_folder="templates", static_folder="static")


@app.route("/")
def home():
    return render_template("startsida.html")


@app.route("/weather", methods=["GET", "POST"])
def filter_data():

    # ==========================================
    # List of cities with their coordinates
    # ==========================================
    cities = {
        "Stockholm": {"lat": 59.33, "lon": 18.07},
        "Göteborg": {"lat": 57.71, "lon": 11.97},
        "Malmö": {"lat": 55.61, "lon": 13.00},
        "Umeå": {"lat": 63.83, "lon": 20.26},
        "Kiruna": {"lat": 67.86, "lon": 20.23},
    }

    # ==========================================
    # Select city from form submission and get its coordinates
    # ==========================================

    if request.method == "POST":
        selected_city = request.form.get(
            "city"
        )  # the variable that matches the form's id and name value.
    else:
        selected_city = "Stockholm"  # default city if no selection is made

    if selected_city is None:
        return "No city was chosen", 400

    # Look up coordinates
    city = cities.get(selected_city)

    if city is None:
        return "Not a city", 400

    # ==========================================
    # get weather data for selected city from the extrenal API using the coordinates
    # ==========================================

    weather_data = get_weather_data(lat=city["lat"], lon=city["lon"])

    if weather_data is None:
        return render_template("503.html"), 503

    # Check if API request failed before I continue to extract data and convert it to a DataFrame.
    if weather_data is None:
        return render_template("503.html"), 503

    # ==========================================
    # Convert JSON data to DataFrame and extract "daily" and "current" weather data
    # ==========================================

    # Extract daily weather data
    daily = weather_data["daily"]

    # Convert daily JSON data into DataFrame because "daily" is a list of dictionaries with multiple rows of entries.
    df = pd.DataFrame(
        {
            "date": daily["time"],
            "min_temp": daily["temperature_2m_min"],
            "max_temp": daily["temperature_2m_max"],
            "precipitation": daily["precipitation_sum"],
        }
    )
    # Extract current weather data directly from the JSON response because "current" is a single dictionary with one row of entries.
    current = weather_data["current"]

    temperature = current["temperature_2m"]
    wind = current["wind_speed_10m"]

    # ==========================================
    # return the extracted data to the template for rendering
    # ==========================================

    return render_template(
        "prognossida.html",
        weather_data=df.to_dict("records"),
        selected_city=selected_city,
        temperature=temperature,
        wind=wind,
    )


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def server_error(e):
    return render_template("503.html"), 503


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
