import requests

URL="https://api.open-meteo.com/v1/forecast"


def get_weather_data(lat=59.33, lon=18.07):  #Funktion som hämtar data, lat och lon är koordinater till stockholm, start och slut är datum
    
    params = {
        "latitude":lat,
        "longitude":lon,
        "current": ["temperature_2m", "wind_speed_10m"],
        "daily": ["temperature_2m_min", "temperature_2m_max", "precipitation_sum"], #mäter temperatur, medelvärde  och  nederbörd och summan av nederbördet
        "timezone": "auto",
        "forecast_days": 3
    }

    try:
        weather_data = requests.get(URL,params=params, timeout=10) #get skickar anropet, parms bygger ihop URL,anrop ger upp efter 10sek
        weather_data.raise_for_status() #400 och 500 skapas här 
        return weather_data.json()
    except requests.exceptions.RequestException as error:
        print("FEL:", error)
        return None
    
def convert_weather_data_to_list(weather_data):
    # Implementation for converting weather data JSON to a list
    
    daily = weather_data["daily"]

    days = []

    for i in range(len(daily["time"])):
        days.append({
            "date": daily["time"][i],
            "temperature_min": daily["temperature_2m_min"][i],
            "temperature_max": daily["temperature_2m_max"][i],
            "precipitation_sum": daily["precipitation_sum"][i]
        })

    return days