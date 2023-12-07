import json
import requests
from settings import api_key_invalid
from exchange_app import ExchangeRateAPI


ER = ExchangeRateAPI()

class TestExchangeRateNegative:
    """Класс с коллекцией негативных тестов для REST API сервиса https://www.exchangerate-api.com."""

    def test_exchange_rates_negative(self):
        """."""

        status, result = ER.get_exchange_rate("USD")
        print(f"\n{result}")

        assert status == 200, f"\nЗапрос отклонен, код состояния ответа{status}. Проверьте параметры запроса."
        assert result["result"] == "success", (f"\nЗапрос отклонен, код состояния ответа{status}. Проверьте параметры "
                                               f"запроса.")
        assert result["base_code"] == "USD"
        assert result['conversion_rates']["USD"] < result['conversion_rates']['RUB'], "Ущипните себя и всё проверьте;)"