import pytest
from settings import *
from conftest import *
from exchange_app import ExchangeRateAPI

ER = ExchangeRateAPI()


class TestExchangeRateNegative:
    """Класс с коллекцией негативных тестов для REST API сервиса https://www.exchangerate-api.com."""

    # 1
    @pytest.mark.one
    @pytest.mark.parametrize("base_currency", [strings_generator(255), strings_generator(1000),
                                               special_chars(),
                                               russian_chars(),
                                               russian_chars().upper(),
                                               chinese_chars(),
                                               digits(),
                                               '3.14'], ids=['string=255', 'string=1000', 'special chars',
                                                             'cyrillic chars', 'CYRILLIC CHARS', 'chinese chars',
                                                             'digits', '3.14(float)'])
    @pytest.mark.parametrize("api_key", [api_key_invalid,
                                         api_key_expired,
                                         special_chars(),
                                         russian_chars(),
                                         russian_chars().upper(),
                                         chinese_chars(),
                                         strings_generator(255),
                                         digits()], ids=['api key invalid', 'api key expired', 'special chars',
                                                         'cyrillic chars', 'CYRILLIC CHARS', 'chinese chars',
                                                         'string=255', 'digits'])
    def test_exchange_rates_negative(self, api_key, base_currency):
        """Негативный тест проверки GET-запроса для предоставления сведений о текущих курсах мировых валют по отношению
        к единице выбранной базовой валюты (base_currency). С помощью фикстуры parametrize в параметры запроса
        передаются заведомо не верифицированные значения api_key и base_currency. Валидация негативного теста успешна в
        случае, если статус ответа сервера на запрос(status) содержит отрицательный код (403 или 404), ответ с кодом 403
        содержит JSON-объект с данными о причине(exception) отказа сервера.

        Примечание:
        Ошибка 403 - сервер понял запрос, но не выполнит его;
        Ошибка 404 - сервер не может найти данные согласно запросу."""

        status, result = ER.get_exchange_rate(api_key, base_currency)

        if status == 403:
            print(f"\n{status}")
            print(f"{result['error-type']}")
            assert status == 403
            assert result['error-type'] == "invalid-key" or 'inactive-account'
        else:
            print(f"\n{result}")
            assert status == 404

    # 2
    @pytest.mark.two
    @pytest.mark.parametrize("target_code", ['', 'a', 'ab', 'abc', 'a'.upper(), 'ab'.upper(), 'abc'.upper(),
                                             strings_generator(255), strings_generator(1000), special_chars(),
                                             russian_chars(), russian_chars().upper(), chinese_chars(), digits(),
                                             '3.14'], ids=['empty string', 'one str letter lower',
                                                           'two str letters lower', 'three str letters lower',
                                                           'one str letter upper', 'two str letters upper',
                                                           'three str letters upper', 'string=255', 'string=1000',
                                                           'special chars', 'cyrillic chars', 'CYRILLIC CHARS',
                                                           'chinese chars', 'digits', '3.14(float)'])
    @pytest.mark.parametrize("base_code", ['', 'a', 'ab', 'abc', 'a'.upper(), 'ab'.upper(), 'abc'.upper(),
                                           strings_generator(255), strings_generator(1000), special_chars(),
                                           russian_chars(), russian_chars().upper(), chinese_chars(), digits(),
                                           '3.14'], ids=['empty string', 'one str letter lower',
                                                         'two str letters lower', 'three str letters lower',
                                                         'one str letter upper', 'two str letters upper',
                                                         'three str letters upper', 'string=255', 'string=1000',
                                                         'special chars', 'cyrillic chars', 'CYRILLIC CHARS',
                                                         'chinese chars', 'digits', '3.14(float)'])
    def test_pair_conversion_no_amount_negative(self, base_code, target_code):
        """Негативный тест отправки GET-запроса для предоставления сведений об отношении обменного курса целевой валюты
        (target_code) по отношению к одной единице базовой валюте(base_code) без использования в запросе параметра
        amount:str (path). С помощью фикстуры parametrize в параметры запроса передаются заведомо не верифицированные
        значения переменных base_code и target_code. Валидация негативного теста успешна в случае, если статус ответа
        (status) содержит отрицательный код состояния равный 400, 403 или 404, ответ с кодом
        400 или 403 содержит JSON-объект с данными о причине(exception) отказа сервера."""

        status, result = ER.conversion_of_currency_pair(api_key_valid, base_code, target_code)

        if status == 400:
            assert result['error-type'] == "malformed-request" or 'inactive-account'
            print(f"\n{status}")
            print(f"{result['error-type']}")
        elif status == 403:
            assert result['error-type'] == "malformed-request" or 'inactive-account'
            print(f"\n{status}")
            print(f"{result['error-type']}")
        else:
            assert status == 404
            print(f"\n{status}")
            print(f"\nОшибка 404 - сервер не может найти данные согласно запросу."
                  f"\nJSON объект с ключом ['error-type'] сервером не сформирован.")

    # 3
    # ВАЖНО:
    @pytest.mark.skip(reason='Тест генерирует 2025 тест-кейсов, использовать по необходимости!')
    @pytest.mark.three
    @pytest.mark.parametrize("amount", ['', digits(), 1234567890, strings_generator(255), strings_generator(1000),
                                        special_chars(), russian_chars(), russian_chars().upper(), chinese_chars()],
                             ids=['empty string', '1234567890 string format', '1234567890 int format', 'string=255',
                                  'string=1000', 'special chars', 'cyrillic chars', 'CYRILLIC CHARS', 'chinese chars'])
    @pytest.mark.parametrize("target_code", ['', 'a', 'ab', 'abc', 'a'.upper(), 'ab'.upper(), 'abc'.upper(),
                                             strings_generator(255), strings_generator(1000), special_chars(),
                                             russian_chars(), russian_chars().upper(), chinese_chars(), digits(),
                                             '3.14'], ids=['empty string', 'one str letter lower',
                                                           'two str letters lower', 'three str letters lower',
                                                           'one str letter upper', 'two str letters upper',
                                                           'three str letters upper', 'string=255', 'string=1000',
                                                           'special chars', 'cyrillic chars', 'CYRILLIC CHARS',
                                                           'chinese chars', 'digits', '3.14(float)'])
    @pytest.mark.parametrize("base_code", ['', 'a', 'ab', 'abc', 'a'.upper(), 'ab'.upper(), 'abc'.upper(),
                                           strings_generator(255), strings_generator(1000), special_chars(),
                                           russian_chars(), russian_chars().upper(), chinese_chars(), digits(),
                                           '3.14'], ids=['empty string', 'one str letter lower',
                                                         'two str letters lower', 'three str letters lower',
                                                         'one str letter upper', 'two str letters upper',
                                                         'three str letters upper', 'string=255', 'string=1000',
                                                         'special chars', 'cyrillic chars', 'CYRILLIC CHARS',
                                                         'chinese chars', 'digits', '3.14(float)'])
    def test_pair_conversion_wth_amount_negative(self, base_code, target_code, amount):
        """Негативный тест отправки GET-запроса для предоставления сведений о стоимости покупки целевой валюты за
        указанное количество (amount) базовой валюты. С помощью фикстуры parametrize в параметры запроса передаются
        заведомо не верифицированные значения переменных base_code, target_code, amount. Валидация негативного теста
        успешна в случае, если статус ответа (status) содержит отрицательный код состояния равный 400, 403 или 404,
        ответ с кодом 400 или 403 содержит JSON-объект с данными о причине(exception) отказа сервера."""

        status, result = ER.conversion_of_currency_pair(api_key_valid, base_code, target_code, amount)

        if status == 400:
            assert result['error-type'] == "malformed-request" or 'inactive-account'
            print(f"\n{status}")
            print(f"{result['error-type']}")
        elif status == 403:
            assert result['error-type'] == "malformed-request" or 'inactive-account'
            print(f"\n{status}")
            print(f"{result['error-type']}")
        else:
            assert status == 404
            print(f"\n{status}")
            print(f"\nОшибка 404 - сервер не может найти данные согласно запросу."
                  f"\nJSON объект с ключом ['error-type'] сервером не сформирован.")
