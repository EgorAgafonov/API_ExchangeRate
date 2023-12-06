import json
import requests
from settings import api_key_valid

a = "https://v6.exchangerate-api.com/v6/b4225086daa983f4e12ee736/latest/"

class ExchangeRateAPI:
    def __init__(self):
        self.base_url = "https://v6.exchangerate-api.com/v6/"

    def get_exchange_rate(self, currency_code: str):
        """Отправка стандартного GET-запроса для предоставления сведений о текущем курсе выбранной валюты по отношению к
        валютам других стран. В качестве позиционного аргумента необходимо указать код валюты согласно
        стандарта ISO 4217."""

        response = requests.get(self.base_url + api_key_valid + "latest/" + currency_code)

        status = response.status_code
        result = ""
        try:
            result = response.json()
        except json.JSONDecodeError:
            result = response.text

        return status, result

    def conversion_of_currency_pair(self, base_code: str, target_code: str, amount=None):
        """"""
        if amount is None:
            response = requests.get(self.base_url + api_key_valid + "pair/" + f"{base_code}/" + f"{target_code}")
        elif amount == float or int:
            response = requests.get(self.base_url + api_key_valid + "pair/" + f"{base_code}/" + f"{target_code}/" + str(amount))
        else:
            pass

        status = response.status_code
        result = ""
        try:
            result = response.json()
        except json.JSONDecodeError:
            result = response.text

        return status, result
