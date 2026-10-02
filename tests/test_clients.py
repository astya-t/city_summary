from unittest.mock import patch, Mock
import pytest
import requests

from clients.weather import get_weather, CityNotFoundError
from clients.rates import get_rate, RateError, CurrencyNotFoundError


@patch("clients.weather.get_json")            
def test_city_not_found(mock_get_json):       
    mock_get_json.return_value = {"generationtime_ms": 0.5} 

    with pytest.raises(CityNotFoundError):  
        get_weather("Qwertyuiopzz")