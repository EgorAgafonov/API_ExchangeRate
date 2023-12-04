import requests
import pytest
from settings import api_key_valid


class ExchangeRateAPI:
    def __init__(self):
        self.base_url = "https://v6.exchangerate-api.com/v6/YOUR-API-KEY/" + api_key_valid

