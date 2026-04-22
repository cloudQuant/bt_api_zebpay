from __future__ import annotations

from typing import Any

from bt_api_zebpay.feeds.live_zebpay.request_base import ZebpayRequestData


class ZebpayRequestDataSpot(ZebpayRequestData):
    def get_server_time(self, extra_data: Any = None, **kwargs: Any):
        path, params, extra = self._get_server_time(extra_data, **kwargs)
        return self.request(path, params, extra_data=extra)

    def async_get_server_time(self, extra_data: Any = None, **kwargs: Any):
        path, params, extra = self._get_server_time(extra_data, **kwargs)
        self.submit(
            self.async_request(path, params, extra_data=extra), callback=self.async_callback
        )

    def get_tick(self, symbol: Any, extra_data: Any = None, **kwargs: Any):
        path, params, extra = self._get_tick(symbol, extra_data, **kwargs)
        return self.request(path, params, extra_data=extra)

    def async_get_tick(self, symbol: Any, extra_data: Any = None, **kwargs: Any):
        path, params, extra = self._get_tick(symbol, extra_data, **kwargs)
        self.submit(
            self.async_request(path, params, extra_data=extra), callback=self.async_callback
        )

    get_ticker = get_tick

    def async_get_ticker(self, symbol: Any, extra_data: Any = None, **kwargs: Any):
        self.async_get_tick(symbol, extra_data, **kwargs)

    def get_depth(self, symbol: Any, count: int = 20, extra_data: Any = None, **kwargs: Any):
        path, params, extra = self._get_depth(symbol, count, extra_data, **kwargs)
        return self.request(path, params, extra_data=extra)

    def async_get_depth(self, symbol: Any, count: int = 20, extra_data: Any = None, **kwargs: Any):
        path, params, extra = self._get_depth(symbol, count, extra_data, **kwargs)
        self.submit(
            self.async_request(path, params, extra_data=extra), callback=self.async_callback
        )

    def get_kline(
        self, symbol: Any, period: Any, count: int = 20, extra_data: Any = None, **kwargs: Any
    ):
        path, params, extra = self._get_kline(symbol, period, count, extra_data, **kwargs)
        return self.request(path, params, extra_data=extra)

    def async_get_kline(
        self, symbol: Any, period: Any, count: int = 20, extra_data: Any = None, **kwargs: Any
    ):
        path, params, extra = self._get_kline(symbol, period, count, extra_data, **kwargs)
        self.submit(
            self.async_request(path, params, extra_data=extra), callback=self.async_callback
        )

    def get_exchange_info(self, extra_data: Any = None, **kwargs: Any):
        path, params, extra = self._get_exchange_info(extra_data, **kwargs)
        return self.request(path, params, extra_data=extra)

    def async_get_exchange_info(self, extra_data: Any = None, **kwargs: Any):
        path, params, extra = self._get_exchange_info(extra_data, **kwargs)
        self.submit(
            self.async_request(path, params, extra_data=extra), callback=self.async_callback
        )

    def get_balance(self, symbol: Any = None, extra_data: Any = None, **kwargs: Any):
        path, params, extra = self._get_balance(extra_data, **kwargs)
        return self.request(path, params, extra_data=extra)

    def async_get_balance(self, symbol: Any = None, extra_data: Any = None, **kwargs: Any):
        path, params, extra = self._get_balance(extra_data, **kwargs)
        self.submit(
            self.async_request(path, params, extra_data=extra), callback=self.async_callback
        )

    def get_account(self, symbol: Any = None, extra_data: Any = None, **kwargs: Any):
        path, params, extra = self._get_account(extra_data, **kwargs)
        return self.request(path, params, extra_data=extra)

    def async_get_account(self, symbol: Any = None, extra_data: Any = None, **kwargs: Any):
        path, params, extra = self._get_account(extra_data, **kwargs)
        self.submit(
            self.async_request(path, params, extra_data=extra), callback=self.async_callback
        )

    def make_order(
        self,
        symbol: Any,
        volume: Any,
        price: Any = None,
        order_type: str = 'buy-limit',
        offset: str = 'open',
        post_only: bool = False,
        client_order_id: Any = None,
        extra_data: Any = None,
        **kwargs: Any,
    ):
        path, params, extra = self._make_order(
            symbol,
            volume,
            price,
            order_type,
            offset,
            post_only,
            client_order_id,
            extra_data,
            **kwargs,
        )
        return self.request(path, body=params, extra_data=extra)

    def async_make_order(
        self,
        symbol: Any,
        volume: Any,
        price: Any = None,
        order_type: str = 'buy-limit',
        offset: str = 'open',
        post_only: bool = False,
        client_order_id: Any = None,
        extra_data: Any = None,
        **kwargs: Any,
    ):
        path, params, extra = self._make_order(
            symbol,
            volume,
            price,
            order_type,
            offset,
            post_only,
            client_order_id,
            extra_data,
            **kwargs,
        )
        self.submit(
            self.async_request(path, body=params, extra_data=extra), callback=self.async_callback
        )

    def cancel_order(
        self, symbol: Any, order_id: Any = None, extra_data: Any = None, **kwargs: Any
    ):
        path, params, extra = self._cancel_order(symbol, order_id, extra_data, **kwargs)
        return self.request(path, params, extra_data=extra)

    def async_cancel_order(
        self, symbol: Any, order_id: Any = None, extra_data: Any = None, **kwargs: Any
    ):
        path, params, extra = self._cancel_order(symbol, order_id, extra_data, **kwargs)
        self.submit(
            self.async_request(path, params, extra_data=extra), callback=self.async_callback
        )

    def query_order(self, symbol: Any, order_id: Any = None, extra_data: Any = None, **kwargs: Any):
        path, params, extra = self._query_order(symbol, order_id, extra_data, **kwargs)
        return self.request(path, params, extra_data=extra)

    def async_query_order(
        self, symbol: Any, order_id: Any = None, extra_data: Any = None, **kwargs: Any
    ):
        path, params, extra = self._query_order(symbol, order_id, extra_data, **kwargs)
        self.submit(
            self.async_request(path, params, extra_data=extra), callback=self.async_callback
        )
