from exchange_app import ExchangeRateAPI
from conftest import *

ER = ExchangeRateAPI()


class TestExchangeRatePositive:
    """Класс с коллекцией позитивных тестов для REST API сервиса https://www.exchangerate-api.com."""

    def test_exchange_rates_USD_positive(self):
        """Тест проверки отправки GET-запроса для предоставления сведений о текущих курсах мировых валют по отношению к
        единице выбранной базовой валюты (здесь: доллар США (USD)). Валидация теста успешна в случае, если ответ сервера
        содержит положительный HTTP-код состояния (200), ответ содержит JSON-объект с данными об актуальных обменных
        курсах валют по отношению к 1$(USD)."""

        status, result = ER.get_exchange_rate("USD")
        print(f"\n{result}")

        assert status == 200, f"\nЗапрос отклонен, код состояния ответа{status}. Проверьте параметры запроса."
        assert result["result"] == "success", (f"\nЗапрос отклонен, код состояния ответа{status}. Проверьте параметры "
                                               f"запроса.")
        assert result["base_code"] == "USD"
        assert result['conversion_rates']["USD"] < result['conversion_rates']['RUB'], "Ущипните себя и всё проверьте;)"

    def test_pair_conversion_no_exchange(self):
        """Тест проверки отправки GET-запроса для предоставления сведений об отношении обменного курса целевой валюты
        (target_code) по отношению к одной единице базовой валюте(base_code). Валидация теста успешна в случае, если
        ответ сервера содержит положительный HTTP-код состояния (200), ответ содержит JSON-объект со значением ключа
        [conversion_rate] равным текущему курсу целевой валюты по отношению к единице базовой валюты."""

        status, result = ER.conversion_of_currency_pair("USD", "RUB", None)

        assert status == 200, f"\nЗапрос отклонен, код состояния ответа{status}. Проверьте параметры запроса."
        assert result["result"] == "success"
        assert result["base_code"] == "USD"
        assert result["target_code"] == "RUB"
        assert result["conversion_rate"] is int or float
        print(Fore.GREEN + Style.DIM + f"\n1 {result['base_code']} = {round(result['conversion_rate'],2)} "
                                       f"{result['target_code']}")

    def test_pair_conversion_exchange(self):
        """Тест аналогичный тесту test_pair_conversion_no_amount с разницей в проверке функции расчета суммы продажи
        целевой валюты за указанное количество(amount_of_exchange) базовой валюты. Валидация теста успешна в случае,
        если ответ сервера содержит положительный HTTP-код состояния (200), ответ содержит JSON-объект с
        ключом [conversion_result], значением которого является сумма продажи целевой валюты."""

        amount_of_exchange = 1100
        status, result = ER.conversion_of_currency_pair('USD', 'RUB', amount_of_exchange)

        assert status == 200, f"\nЗапрос отклонен, код состояния ответа{status}. Проверьте параметры запроса."
        assert result["result"] == "success"
        assert result["base_code"] == "USD"
        assert result["target_code"] == "RUB"
        assert result["conversion_result"] is int or float
        print(Fore.GREEN + Style.DIM + f"\n{amount_of_exchange} {result['base_code']} = "
                                       f"{round(result['conversion_result'],2)} {result['target_code']}")








