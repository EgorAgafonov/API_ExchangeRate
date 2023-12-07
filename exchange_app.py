import json
import requests
from settings import api_key_valid


class ExchangeRateAPI:
    def __init__(self):
        self.base_url = "https://v6.exchangerate-api.com/v6/"

    def get_exchange_rate(self, currency_code: str):
        """Метод стандартного GET-запроса для предоставления сведений о курсах мировых валют по отношению к выбранной
        единице базовой валюты. В качестве значения аргумента currency_code необходимо указать строковый код валюты
        согласно стандарта ISO 4217."""

        response = requests.get(self.base_url + api_key_valid + "latest/" + currency_code)

        status = response.status_code
        result = ""
        try:
            result = response.json()
        except json.JSONDecodeError:
            result = response.text

        return status, result

    def conversion_of_currency_pair(self, base_code: str, target_code: str, amount_of_exchange=None) -> object:
        """Метод отправки GET-запроса для предоставления сведений об отношении обменного курса целевой валюты
        (target_code) по отношению к одной единице базовой валюте(base_code). """

        if not amount_of_exchange:
            response = requests.get(self.base_url + api_key_valid + "pair/" + f"{base_code}/" + f"{target_code}")
        else:
            response = requests.get(self.base_url + api_key_valid + "pair/" + f"{base_code}/" + f"{target_code}/"
                                    + str(amount_of_exchange))

        status = response.status_code
        result = ""
        try:
            result = response.json()
        except json.JSONDecodeError:
            result = response.text

        return status, result
