from exchange_app import ExchangeRateAPI
from conftest import *

ER = ExchangeRateAPI()


class TestExchangeRatePositive:
    """Класс с коллекцией позитивных тестов для REST API сервиса https://www.exchangerate-api.com"""

    def test_exchange_rates_USD_positive(self):
        """Тест проверки отправки GET-запроса для предоставления сведений о текущем курсе доллара США (USD) по отношению
         к другим валютам. Валидация теста успешна в случае, если ответ сервера содержит положительный кода состояния
        (200), ответ содержит JSON-объект с данными об актуальных обменных курсах валют по отношению к 1$(USD)."""

        status, result = ER.get_exchange_rate("USD")

        assert status == 200, f"\nЗапрос отклонен, код состояния ответа{status}. Проверьте параметры запроса."
        assert result["result"] == "success", (f"\nЗапрос отклонен, код состояния ответа{status}. Проверьте параметры "
                                               f"запроса.")
        assert result["base_code"] == "USD"
        assert result['conversion_rates']["USD"] < result['conversion_rates']['RUB'], "Ущипните себя и всё проверьте ;)"





