import pytest
from unittest.mock import patch
from app import app
from app.externals import get_weather_data

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_weather(client, mock_redis):
    get_weather_data.calls = list()
    for _ in range(150):
        response = client.get("/weather?city=Astana")
        assert response.status_code == 200
    assert len(get_weather_data.calls) == 1
    
def test_weather_case_insensitive_city(client, mock_redis):
    get_weather_data.calls = list()
    response1 = client.get("/weather?city=Astana")
    assert response1.status_code == 200
    assert len(get_weather_data.calls) == 1
    response2 = client.get("/weather?city=astana")
    assert response2.status_code == 200
    assert len(get_weather_data.calls) == 1