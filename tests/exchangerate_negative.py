import pytest
from settings import *
from conftest import *
from exchange_app import ExchangeRateAPI

ER = ExchangeRateAPI()


class TestExchangeRateNegative:
    """����� � ���������� ���������� ������ ��� REST API ������� https://www.exchangerate-api.com."""

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
        """���������� ���� �������� GET-������� ��� �������������� �������� � ������� ������ ������� ����� �� ���������
        � ������� ��������� ������� ������ (�����: ������ ��� (USD)). � ������� �������� parametrize � ��������� �������
        ���������� �������� �� ���������������� ��������. ��������� ����������� ����� ������� � ������, ���� �����
        ������� �� ������ �������� ������������� HTTP-��� ��������� (400), ����� �������� JSON-������ � ������� �
       �������(exception) ������ ������� � ������."""

        status, result = ER.get_exchange_rate(api_key, base_code)

        assert status == 404
        assert result["error-type"] == 'invalid-key'
