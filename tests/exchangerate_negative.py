import pytest
from settings import *
from conftest import *
from exchange_app import ExchangeRateAPI

ER = ExchangeRateAPI()


class TestExchangeRateNegative:
    """Класс с коллекцией негативных тестов для REST API сервиса https://www.exchangerate-api.com."""

    @pytest.mark.parametrize("api_key", [api_key_invalid,
                                         api_key_expired,
                                         special_chars(),
                                         russian_chars(),
                                         russian_chars().upper(),
                                         chinese_chars(),
                                         strings_generator(255),
                                         digits()], ids=['api key_invalid', 'api key_expired', 'special chars',
                                                         'cyrillic chars', 'CYRILLIC CHARS',
                                                         'chinese chars', 'string=255', 'digits'])
    @pytest.mark.parametrize("base_currency", [api_key_invalid,
    def test_exchange_rates_negative(self, api_key, base_currency):
        """Негативный тест проверки GET-запроса для предоставления сведений о текущих курсах мировых валют по отношению
        к единице выбранной базовой валюты (base_currency). С помощью фикстуры parametrize в параметры запроса
        передаются заведомо не верифицированные значения api_key и base_currency. Валидация негативного теста успешна в
        случае, если статус ответа сервера на запрос(status) содержит отрицательный код (403 или 404), ответ с кодом 403
        содержит JSON-объект с данными о причине(exception) отказа сервера."""

        status, result = ER.get_exchange_rate(api_key, base_currency)

        if status == 403:
            print(f"\n{status}")
            print(f"{result['error-type']}")
            assert status == 403
            assert result['error-type'] == "invalid-key" or 'inactive-account'
        else:
            print(f"\n{result}")
            assert status == 404





