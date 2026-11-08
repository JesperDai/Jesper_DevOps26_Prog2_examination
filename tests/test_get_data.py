from unittest.mock import patch

from application.func import get_weather_data


@patch(
    "application.func.requests.get"
)  # @patch för att ersätta vanliga request.get med en mock
def test_get_weather_data(mock_get):
    mock_get.return_value.json.return_value = {  # fejk data som tas emot
        "latitude": 59.33,
        "longitude": 18.07,
        "daily": {
            "time": ["2000-01-01"],
            "temperature_2m_mean": [5.0],
            "precipitation_sum": [1.2],
        },
    }

    mock_get.return_value.raise_for_status.return_value = None  # raise_for_status under lyckad anrop ska ge ut värde NONE, annars raise ett felstatus som 404 eller 500.

    data = get_weather_data(
        lat=59.33, lon=18.07
    )  # anropar funktion men request.get är fortfarande mockad så inget riktigt anrop ut mot externa API

    mock_get.assert_called_once()  # hört att det kan vara bra att kolla att API request bara blev kallad en gång och inte flera.

    # kollar att datan vi får in stämmer överens med vad vi förväntar att få

    assert data is not None
    assert data["latitude"] == 59.33
    assert data["longitude"] == 18.07

    assert "latitude" in data  # kollar att viktiga "keys" finns med i json filen.
    assert "longitude" in data
    assert "daily" in data

    assert isinstance(
        data, dict
    )  # isinstance kollar om ett värde är just den här typen av data som specifieras i koden. I detta fall data == dict
    assert isinstance(data["latitude"], (int, float))
    assert isinstance(data["daily"]["temperature_2m_mean"], list)


def test_get_weather_data_with_invalid_coordinates():
    data = get_weather_data(
        lat=999, lon=999
    )  # anropar funktion med ogiltiga koordinater

    assert data is None  # kollar att datan är NONE eftersom koordinaterna är ogiltiga.
