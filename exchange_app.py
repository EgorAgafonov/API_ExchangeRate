import json

import requests
import pytest
from settings import api_key_valid


class ExchangeRateAPI:
    def __init__(self):
        self.base_url = "https://v6.exchangerate-api.com/v6/YOUR-API-KEY/" + api_key_valid

    def get_exchange_rate(self, currency):
        """Отправка стандартного GET-запроса для предоставления сведений о текущем курсе выбранной валюты по отношению к
        валютам других стран."""

        response = requests.get(self.base_url + "/latest" + currency)

        status = response.status_code
        result = ""
        try:
            result = response.json()
        except json.JSONDecodeError:
            result = response.text

        return status, result
