import pytest
from settings import *
from conftest import *
from exchange_app import ExchangeRateAPI

ER = ExchangeRateAPI()


class TestExchangeRateNegative:
    """ ласс с коллекцией негативных тестов дл€ REST API сервиса https://www.exchangerate-api.com."""

    @pytest.mark.parametrize("api_key", [api_key_invalid,
                                         api_key_expired,
                                         special_chars(),
                                         russian_chars(),
                                         russian_chars().upper(),
                                         chinese_chars(),
                                         strings_generator(255),
                                         digits()], ids=['api key_invalid', 'api key_expired', 'special chars',
                                                         'cyrillic chars', 'CYRILLIC CHARS', '255 symbols name',
                                                         'chinese chars' 'string=255', 'digits'])
    # @pytest.mark.parametrize("age", ["1", 23.45, -1], ids=['string_age', 'float_age', 'negative_age'])
    def test_exchange_rates_positive(self, api_key, base_code='USD'):
        """Ќегативный тест проверки GET-запроса дл€ предоставлени€ сведений о текущих курсах мировых валют по отношению
        к единице выбранной базовой валюты (здесь: доллар —Ўј (USD)). — помощью фикстуры parametrize в параметры запроса
        передаютс€ заведомо не верифицированные значени€. ¬алидаци€ негативного теста успешна в случае, если ответ
        сервера на запрос содержит отрицательный HTTP-код состо€ни€ (400), ответ содержит JSON-объект с данными о
       причине(exception) отказа сервера в ответе."""

        status, result = ER.get_exchange_rate(api_key, base_code)

        assert status == 404
        assert result["error-type"] == 'invalid-key'
