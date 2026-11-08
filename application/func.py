import requests

URL = "https://api.open-meteo.com/v1/forecast"


def get_weather_data(
    lat=59.33, lon=18.07
):  # Funktion som hämtar data, lat och lon är koordinater till stockholm som default. Om man vill hämta data för en annan stad så skickar man med lat och lon som argument.

    # Check that coordinates are valid
    if not (-90 <= lat <= 90) or not (-180 <= lon <= 180):
        return None

    params = {
        "latitude": lat,
        "longitude": lon,
        "current": ["temperature_2m", "wind_speed_10m"],
        "daily": [
            "temperature_2m_min",
            "temperature_2m_max",
            "precipitation_sum",
        ],
        "timezone": "auto",
        "forecast_days": 3,
    }

    try:
        # get skickar anropet, parms bygger ihop URL, timeout gör anrop ge upp efter 10sek utan något svar.
        weather_data = requests.get(URL, params=params, timeout=10)
        weather_data.raise_for_status()  # 400 och 500 skapas här
        return weather_data.json()
    except requests.exceptions.RequestException as error:
        print("API request didn't work:", error)
        return None


# ==========================================
# Testar att func logik fungerar som den ska.
# ==========================================


def berakna_medel(lista):
    return sum(lista) / len(lista)


def dela(a, b):
    if b == 0:
        raise ValueError("Division med noll")
    return a / b
