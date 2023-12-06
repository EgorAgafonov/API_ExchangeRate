from exchange_app import ExchangeRateAPI
from conftest import *

ER = ExchangeRateAPI()


class TestExchangeRatePositive:
    """Класс с коллекцией позитивных тестов для REST API сервиса https://www.exchangerate-api.com"""

    def test_exchange_rates_USD_positive(self):
        """Тест проверки отправки GET-запроса для предоставления сведений о текущем курсе доллара США (USD) по отношению
         к другим валютам. Валидация теста успешна в случае, если ответ сервера содержит положительный HTTP-код
         состояния (200), ответ содержит JSON-объект с данными об актуальных обменных курсах валют по отношению
         к 1$(USD)."""

        status, result = ER.get_exchange_rate("USD")

        assert status == 200, f"\nЗапрос отклонен, код состояния ответа{status}. Проверьте параметры запроса."
        assert result["result"] == "success", (f"\nЗапрос отклонен, код состояния ответа{status}. Проверьте параметры "
                                               f"запроса.")
        assert result["base_code"] == "USD"
        assert result['conversion_rates']["USD"] < result['conversion_rates']['RUB'], "Ущипните себя и всё проверьте;)"

    def test_pair_conversion_no_amount(self):
        """Тест проверки отправки GET-запроса для предоставления сведений об отношении обменного курса целевой валюты
        (target_code) по отношению к одной единице базовой валюте(base_code). Валидация теста успешна в случае, если ответ сервера
        содержит положительный HTTP-код состояния (200), ответ содержит JSON-объект со значением ключа [conversion_rate],
        равным текущему курсу целевой валюты по отношению к базовой единице валюты."""

        status, result = ER.conversion_of_currency_pair(None, "USD", "RUB")

        assert status == 200, f"\nЗапрос отклонен, код состояния ответа{status}. Проверьте параметры запроса."
        assert result["result"] == "success", (f"\nЗапрос отклонен, код состояния ответа{status}. Проверьте параметры "
                                               f"запроса.")
        assert result["base_code"] == "USD"
        assert result["target_code"] == "RUB"
        assert result["conversion_rate"] is int or float
        print(Fore.GREEN + Style.DIM + f"\n{result['base_code']}, {result['target_code']}, {result['conversion_rate']}")

    def test_pair_conversion_amount(self):
        """Тест проверки отправки GET-запроса аналогичный тесту test_pair_conversion_no_amount с разницей в проверке
        пересчета стоимости целевой валюты(target_code) за указанное количество(amount) базовой валюты(base_code).
        Валидация теста успешна в случае, если ответ сервера содержит положительный HTTP-код состояния
        (200), ответ содержит JSON-объект со значением ключа [conversion_result], содержащим результат пересчета в
        соответствии с заданным значением amount."""

        amount = 1125
        base_code = 'USD'
        target_code = 'RUB'

        status, result = ER.conversion_of_currency_pair(amount, base_code, target_code)

        assert status == 200, f"\nЗапрос отклонен, код состояния ответа{status}. Проверьте параметры запроса."
        assert result["result"] == "success", (f"\nЗапрос отклонен, код состояния ответа{status}. Проверьте параметры "
                                               f"запроса.")
        assert result["base_code"] == "USD"
        assert result["target_code"] == "RUB"
        assert result["conversion_result"] is int or float
        print(Fore.GREEN + Style.DIM + f"\n{amount} {result['base_code']} = {round(result['conversion_result'],2)} {result['target_code']}")








