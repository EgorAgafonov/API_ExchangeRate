import pytest
from exchange_app import ExchangeRateAPI

ER = ExchangeRateAPI()


class TestExchangeRatePositive:
    """"""

    def test_get_exchange_rate_USD(self):
        """"""
        status, result = ER.get_exchange_rate("USD")
        print(f"\n{status}")
        list_of_items = dict(result).items()
        print(result, sep="\n")

        # assert status == "200"


