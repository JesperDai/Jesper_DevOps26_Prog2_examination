from unittest.mock import patch

import pytest
import requests

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
    assert data["daily"]["time"] == ["2000-01-01"]


@patch("application.func.requests.get")
def test_get_weather_data_with_invalid_coordinates(mock_get):
    data = get_weather_data(
        lat=999, lon=999
    )  # anropar funktion med ogiltiga koordinater

    assert data is None  # kollar att datan är NONE eftersom koordinaterna är ogiltiga.
    mock_get.assert_not_called()  # kollar att mock_get inte blev kallad eftersom koordinaterna är ogiltiga.


@patch("application.func.requests.get")
def test_API_timeout(mock_get):

    mock_get.side_effect = requests.Timeout

    result = get_weather_data(lat=59.33, lon=18.07)

    assert result is None


@patch(
    "application.func.requests.get"
)  # @patch för att ersätta vanliga request.get med en mock
def test_no_server_access(mock_get):
    mock_response = mock_get.return_value  # mock_get mockar en requests.get anrop. mock_response är mocken som returneras av mock_get.
    mock_response.status_code = 503
    mock_response.raise_for_status.side_effect = requests.HTTPError(
        "503 Service Unavailable"
    )

    with pytest.raises(requests.exceptions.HTTPError):
        mock_response.raise_for_status()
    assert mock_response is not None
    assert mock_response.status_code == 503
