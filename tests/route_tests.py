""" Test suite for image upload """

import logging
from pathlib import Path

resources = Path(__file__).parent / "resources"


def test_client(client):
    """ Test if conf file provides client for mocking API requests """
    assert client


def test_news_route(client):
    """ Test news route by mocking a request """

    response = client.post("portal/news", data={
        "newsImage": (resources / "test.png").open("rb"),
        "newsTitle": "Fermentum leo vel orci porta non pulvinar.",
        "newsContent": "Lorem ipsum dolor sit amet",
        "newsDate": "2017-06-01T08:30"
    })

    assert response.status_code in (200, 304)


def test_individual_route(client):
    """ Test individual route by mocking a request """

    response = client.post("portal/individual", data={
        "indImage": (resources / "test.png").open("rb"),
        'indName': 'Poupette',
        'indSex': 'female',
        'indDesc': 'Very pretty.',
        'situation': 'alone',
        'indSize': 9,
        'indBehavior': 'Being silly.',
        'tagDate': '1993/01/02'
    })

    assert response.status_code in (200, 304)


def test_upload_route(client):
    """ Test upload route by mocking a request """

    response = client.post("portal/upload", data={
        "locFile": (resources / "data_test.csv").open("rb")})

    logging.error(response)
    assert response.status_code in (200, 304)
