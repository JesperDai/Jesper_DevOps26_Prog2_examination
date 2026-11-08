import requests

URL = "https://api.open-meteo.com/v1/forecast"


def get_weather_data(
    lat=59.33, lon=18.07
):  # Funktion som hämtar data, lat och lon är koordinater till stockholm, start och slut är datum

    params = {
        "latitude": lat,
        "longitude": lon,
        "current": ["temperature_2m", "wind_speed_10m"],
        "daily": [
            "temperature_2m_min",
            "temperature_2m_max",
            "precipitation_sum",
        ],  # mäter temperatur, medelvärde  och  nederbörd och summan av nederbördet
        "timezone": "auto",
        "forecast_days": 3,
    }

    try:
        weather_data = requests.get(
            URL, params=params, timeout=10
        )  # get skickar anropet, parms bygger ihop URL, timeout gör anrop ge upp efter 10sek utan något svar.
        weather_data.raise_for_status()  # 400 och 500 skapas här
        return weather_data.json()
    except requests.exceptions.RequestException as error:
        print("FEL:", error)
        return None
