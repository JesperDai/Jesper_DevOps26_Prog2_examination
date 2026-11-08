from unittest.mock import patch

import pytest
import requests

from app import app

# skapar en fixture eller så kallad miljö där testerna körs med en separat test klient.
@pytest.fixture
def klient():
    app.config["TESTING"] = True  
    return (
        app.test_client()
    )  # skickar requests utan att starta en web server. Den kollar om responsen


def test_startsida_finns(klient):
    answer = klient.get("/")  # kollar om klienten får startsidan
    assert (
        answer.status_code == 200
    )  # assert kollar om något är sant. I detta fall, kollar den om klienten får status koden lika med 200.


def test_saknas_endpoint(
    klient,
):  # @app.errorhandler(404) finns i app.py som gör att vår 404.html sida visas under 404 fel
    answer = klient.get("/finns-inte")
    assert (
        answer.status_code == 404
    )  # kollar om endpoint /finns-inte ger http status kod 404.
    assert (
        b"Page not Found 404" in answer.data
    )  # kollar att "Page not Found 404" finns i html data i vår 404.html. b sträng används när svaret är av typen byte.


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
