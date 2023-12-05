import json
import requests
from settings import api_key_valid

a = "https://v6.exchangerate-api.com/v6/b4225086daa983f4e12ee736/latest/"

class ExchangeRateAPI:
    def __init__(self):
        self.base_url = "https://v6.exchangerate-api.com/v6/"

    def get_exchange_rate(self, currency):
        """Отправка стандартного GET-запроса для предоставления сведений о текущем курсе выбранной валюты по отношению к
        валютам других стран."""

        response = requests.get(self.base_url + api_key_valid + "latest/" + currency)

        status = response.status_code
        result = ""
        try:
            result = response.json()
        except json.JSONDecodeError:
            result = response.text

        return status, result
