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
    def test_exchange_rates_api_key_negative(self, api_key, base_code='USD'):
        """Негативный тест проверки GET-запроса для предоставления сведений о текущих курсах мировых валют по отношению
        к единице выбранной базовой валюты (здесь: доллар США (USD)). С помощью фикстуры parametrize в параметры запроса
        передаются заведомо не верифицированные значения. Валидация негативного теста успешна в случае, если статус
        ответа сервера на запрос(status) содержит отрицательный код состояния со стороны клиента (403 или 404), для
        кода 403 ответ содержит JSON-объект с данными о причине(exception) отказа сервера в ответе."""

        status, result = ER.get_exchange_rate(api_key, base_code)

        print(f"\n{status}")
        print(f"\n{result}")
        assert status == 403 or 404




