from __future__ import annotations

from bt_api_base.containers.exchanges.exchange_data import ExchangeData

_FALLBACK_REST_PATHS = {
    'get_tick': 'GET /api/v2/market/ticker',
    'get_ticker': 'GET /api/v2/market/ticker',
    'get_depth': 'GET /api/v2/market/orderbook',
    'get_kline': 'GET /api/v2/market/klines',
    'get_trades': 'GET /api/v2/market/trades',
    'get_exchange_info': 'GET /api/v2/ex/exchangeInfo',
    'get_server_time': 'GET /api/v2/system/time',
    'get_account': 'GET /api/v2/account',
    'get_balance': 'GET /api/v2/account/balance',
    'make_order': 'POST /api/v2/order',
    'cancel_order': 'DELETE /api/v2/order',
    'query_order': 'GET /api/v2/order',
}


class ZebpayExchangeData(ExchangeData):
    def __init__(self) -> None:
        super().__init__()
        self.exchange_name = 'ZEBPAY___SPOT'
        self.rest_url = 'https://sapi.zebpay.com'
        self.wss_url = 'wss://stream.zebpay.com'
        self.rest_paths = dict(_FALLBACK_REST_PATHS)
        self.wss_paths = {}
        self.kline_periods = {
            '1m': '1m',
            '5m': '5m',
            '15m': '15m',
            '30m': '30m',
            '1h': '1h',
            '2h': '2h',
            '4h': '4h',
            '12h': '12h',
            '1d': '1d',
            '1w': '1w',
        }
        self.legal_currency = ['INR', 'USDT']

    @staticmethod
    def get_symbol(symbol):
        s = symbol.strip().replace('/', '-').replace('_', '-').upper()
        return s

    @staticmethod
    def get_reverse_symbol(symbol):
        return symbol.strip().replace('/', '-').replace('_', '-').upper()

    def get_period(self, period: str) -> str:
        return self.kline_periods.get(period, period)

    def get_reverse_period(self, period: str) -> str:
        for k, v in self.kline_periods.items():
            if v == period:
                return k
        return period

    def get_rest_path(self, key: str, **kwargs) -> str:
        path = self.rest_paths.get(key, '')
        if not path:
            raise ValueError(f'[{self.exchange_name}] REST path not found: {key}')
        if kwargs:
            path = path.format(**kwargs)
        return path


class ZebpayExchangeDataSpot(ZebpayExchangeData):
    def __init__(self) -> None:
        super().__init__()
        self.asset_type = 'SPOT'
