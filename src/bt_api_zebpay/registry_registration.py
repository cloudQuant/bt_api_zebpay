from __future__ import annotations

from bt_api_base.balance_utils import simple_balance_handler as _zebpay_balance_handler
from bt_api_base.registry import ExchangeRegistry

from bt_api_zebpay.exchange_data import ZebpayExchangeDataSpot
from bt_api_zebpay.feeds.live_zebpay.spot import ZebpayRequestDataSpot


def register_zebpay(registry: type[ExchangeRegistry]) -> None:
    registry.register_feed("ZEBPAY___SPOT", ZebpayRequestDataSpot)
    registry.register_exchange_data("ZEBPAY___SPOT", ZebpayExchangeDataSpot)
    registry.register_balance_handler("ZEBPAY___SPOT", _zebpay_balance_handler)
