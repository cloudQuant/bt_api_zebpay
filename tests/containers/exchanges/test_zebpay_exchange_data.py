"""Tests for ZebpayExchangeData container."""

from __future__ import annotations

from bt_api_zebpay.exchange_data import ZebpayExchangeData


class TestZebpayExchangeData:
    """Tests for ZebpayExchangeData."""

    def test_init(self):
        """Test initialization."""
        exchange = ZebpayExchangeData()

        assert exchange.exchange_name == "ZEBPAY___SPOT"

    def test_get_symbol_normalizes(self):
        """normalize 交易对：分隔符统一为 '-'，并转大写。"""
        exchange = ZebpayExchangeData()

        assert exchange.get_symbol("btc/inr") == "BTC-INR"
        assert exchange.get_symbol("btc_inr") == "BTC-INR"
        assert exchange.get_symbol(" btc-inr ") == "BTC-INR"

    def test_get_period_maps_and_roundtrips(self):
        """周期映射 + 反向映射往返一致。"""
        exchange = ZebpayExchangeData()

        assert exchange.get_period("1m") == "1m"
        assert exchange.get_period("unknown") == "unknown"  # 未映射时透传
        assert exchange.get_reverse_period("1d") == "1d"

    def test_get_rest_path_returns_endpoint(self):
        """REST 路径按 key 返回真实端点，未知 key 抛 ValueError。"""
        exchange = ZebpayExchangeData()

        assert exchange.get_rest_path("get_tick") == "GET /api/v2/market/ticker"

        import pytest

        with pytest.raises(ValueError, match="REST path not found"):
            exchange.get_rest_path("nonexistent")
