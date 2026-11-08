import pytest

from app import app


# skapar en fixture eller så kallad miljö där testerna körs med en separat test klient.
@pytest.fixture
def klient():
    app.config["TESTING"] = True
    return app.test_client()  # skickar requests utan att starta en web server.


def test_startsida_works(klient):
    answer = klient.get("/")  # kollar om klienten får startsidan
    assert (
        answer.status_code == 200
    )  # assert kollar om något är sant. I detta fall, kollar den om klienten får status koden lika med 200.


def test_missing_endpoint(
    klient,
):  # @app.errorhandler(404) finns i app.py som gör att vår 404.html sida visas under 404 fel
    answer = klient.get("/does-not-exist")
    assert (
        answer.status_code == 404
    )  # kollar om endpoint /does-not-exist ger http status kod 404.
    assert (
        b"Page not Found 404" in answer.data
    )  # kollar att "Page not Found 404" finns i html data i vår 404.html. b sträng används när svaret är av typen byte.


def test_invalid_city(klient):

    response = klient.post("/weather", data={"city": "London"})

    assert response.status_code == 400
    assert b"Not a city" in response.data


def test_valid_city(klient):

    response = klient.post("/weather", data={"city": "Stockholm"})

    assert response.status_code == 200
    assert b"Stockholm" in response.data
