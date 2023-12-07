import json
import requests
from settings import api_key_invalid
from exchange_app import ExchangeRateAPI


ER = ExchangeRateAPI()

class TestExchangeRateNegative:
    """����� � ���������� ���������� ������ ��� REST API ������� https://www.exchangerate-api.com."""

    def test_exchange_rates_negative(self):
        """."""

        status, result = ER.get_exchange_rate("USD")
        print(f"\n{result}")

        assert status == 200, f"\n������ ��������, ��� ��������� ������{status}. ��������� ��������� �������."
        assert result["result"] == "success", (f"\n������ ��������, ��� ��������� ������{status}. ��������� ��������� "
                                               f"�������.")
        assert result["base_code"] == "USD"
        assert result['conversion_rates']["USD"] < result['conversion_rates']['RUB'], "�������� ���� � �� ���������;)"