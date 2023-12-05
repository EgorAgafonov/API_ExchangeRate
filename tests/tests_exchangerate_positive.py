import pytest
from exchange_app import ExchangeRateAPI

ER = ExchangeRateAPI()


class TestExchangeRatePositive:
    """"""

    def test_get_exchange_rate_USD(self):
        """"""

        status, result = ER.get_exchange_rate("USD")

        assert status == 200
        assert result["base_code"] == "USD"
        print(f"\n{result['conversion_rates']['RUB']}")



