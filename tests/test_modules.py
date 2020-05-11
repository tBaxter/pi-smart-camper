import sys
from os import environ
from webapp import settings


def test_api_vars_set():
    assert "IPINFO_API_KEY" in environ
    assert "OPENWEATHER_API_KEY" in environ
    assert settings.IPINFO_API_KEY == environ.get('IPINFO_API_KEY')
    assert settings.OPENWEATHER_API_KEY == environ.get('OPENWEATHER_API_KEY')



