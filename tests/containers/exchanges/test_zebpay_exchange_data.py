"""Tests for ZebpayExchangeData container."""

from __future__ import annotations

from bt_api_zebpay.exchange_data import ZebpayExchangeData


class TestZebpayExchangeData:
    """Tests for ZebpayExchangeData."""

    def test_init(self):
        """Test initialization."""
        exchange = ZebpayExchangeData()

        assert exchange.exchange_name == "ZEBPAY___SPOT"
