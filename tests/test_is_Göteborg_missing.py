def test_where_is_göteborg():
    from application.func import get_weather_data

    data = get_weather_data(lat=57.71, lon=11.97)

    assert data is not None
    assert data["latitude"] == 57.714157
    assert data["longitude"] == 11.972931
    assert "daily" in data
    assert isinstance(data, dict)
    assert isinstance(data["latitude"], (int, float))
    assert isinstance(data["current"]["temperature_2m"], (int, float))
    assert isinstance(data["daily"]["time"], list)
