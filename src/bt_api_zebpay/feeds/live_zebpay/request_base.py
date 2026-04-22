from __future__ import annotations

import hashlib
import hmac
import json
import time
from typing import Any
from urllib.parse import urlencode

from bt_api_base.containers.requestdatas.request_data import RequestData
from bt_api_base.feeds.capability import Capability
from bt_api_base.feeds.feed import Feed

from bt_api_zebpay.exchange_data import ZebpayExchangeDataSpot


class ZebpayRequestData(Feed):
    @classmethod
    def _capabilities(cls) -> set[Capability]:
        return {
            Capability.GET_TICK,
            Capability.GET_DEPTH,
            Capability.GET_KLINE,
            Capability.GET_EXCHANGE_INFO,
            Capability.GET_SERVER_TIME,
            Capability.GET_BALANCE,
            Capability.GET_ACCOUNT,
            Capability.MAKE_ORDER,
            Capability.CANCEL_ORDER,
            Capability.QUERY_ORDER,
        }

    def __init__(self, data_queue: Any = None, **kwargs: Any) -> None:
        super().__init__(data_queue, **kwargs)
        self.data_queue = data_queue
        self.exchange_name = kwargs.get('exchange_name', 'ZEBPAY___SPOT')
        self.asset_type = kwargs.get('asset_type', 'SPOT')
        self.api_key = kwargs.get('public_key') or kwargs.get('api_key')
        self.api_secret = kwargs.get('secret_key') or kwargs.get('api_secret')
        self._params = ZebpayExchangeDataSpot()

    def _generate_signature(self, payload: str) -> str:
        if not self.api_secret:
            return ''
        return hmac.new(
            self.api_secret.encode('utf-8'), payload.encode('utf-8'), hashlib.sha256
        ).hexdigest()

    def _get_headers(
        self, method: str = 'GET', params: Any = None, body: Any = None
    ) -> dict[str, str]:
        headers = {'Content-Type': 'application/json'}
        if self.api_key:
            headers['X-AUTH-APIKEY'] = self.api_key
        if self.api_secret:
            timestamp = str(int(time.time() * 1000))
            if method in ('GET', 'DELETE'):
                qp = params.copy() if params else {}
                qp['timestamp'] = timestamp
                headers['X-AUTH-SIGNATURE'] = self._generate_signature(urlencode(qp))
            else:
                bp = body.copy() if body else {}
                bp['timestamp'] = timestamp
                headers['X-AUTH-SIGNATURE'] = self._generate_signature(
                    json.dumps(bp, separators=(',', ':'))
                )
        return headers

    def request(
        self,
        path: str,
        params: Any = None,
        body: Any = None,
        extra_data: Any = None,
        timeout: int = 10,
    ) -> RequestData:
        method = path.split()[0] if ' ' in path else 'GET'
        endpoint = path.split()[1] if ' ' in path else path
        url = self._params.rest_url + endpoint
        if params:
            url = url + '?' + urlencode(params)
        response = self.http_request(
            method=method,
            url=url,
            headers=self._get_headers(method, params, body),
            body=body,
            timeout=timeout,
        )
        return RequestData(response, extra_data)

    async def async_request(
        self,
        path: str,
        params: Any = None,
        body: Any = None,
        extra_data: Any = None,
        timeout: int = 10,
    ) -> RequestData:
        method = path.split()[0] if ' ' in path else 'GET'
        endpoint = path.split()[1] if ' ' in path else path
        url = self._params.rest_url + endpoint
        if params:
            url = url + '?' + urlencode(params)
        response = await self.async_http_request(
            method=method,
            url=url,
            headers=self._get_headers(method, params, body),
            body=body,
            timeout=timeout,
        )
        return RequestData(response, extra_data)

    def push_data_to_queue(self, data: Any) -> None:
        if self.data_queue is not None:
            self.data_queue.put(data)

    def async_callback(self, future: Any) -> None:
        try:
            result = future.result()
            self.push_data_to_queue(result)
        except Exception as exc:
            self.logger.warning('async_callback::%s', exc)

    def connect(self) -> None:
        pass

    def disconnect(self) -> None:
        super().disconnect()

    def is_connected(self) -> bool:
        return True

    @staticmethod
    def _is_error(data: Any) -> bool:
        if data is None:
            return True
        return bool(isinstance(data, dict) and ('error' in data or data.get('code', 0) != 0))

    def _get_server_time(self, extra_data: Any = None, **kwargs: Any):
        path = self._params.get_rest_path('get_server_time')
        extra_data = extra_data or {}
        extra_data.update(
            {
                'request_type': 'get_server_time',
                'asset_type': self.asset_type,
                'exchange_name': self.exchange_name,
                'normalize_function': self._get_server_time_normalize_function,
            }
        )
        return path, None, extra_data

    def _get_tick(self, symbol: str, extra_data: Any = None, **kwargs: Any):
        path = self._params.get_rest_path('get_tick')
        params = {'symbol': self._params.get_symbol(symbol)}
        extra_data = extra_data or {}
        extra_data.update(
            {
                'request_type': 'get_tick',
                'symbol_name': symbol,
                'asset_type': self.asset_type,
                'exchange_name': self.exchange_name,
                'normalize_function': self._get_tick_normalize_function,
            }
        )
        return path, params, extra_data

    def _get_depth(self, symbol: str, count: int = 20, extra_data: Any = None, **kwargs: Any):
        path = self._params.get_rest_path('get_depth')
        params = {'symbol': self._params.get_symbol(symbol)}
        extra_data = extra_data or {}
        extra_data.update(
            {
                'request_type': 'get_depth',
                'symbol_name': symbol,
                'asset_type': self.asset_type,
                'exchange_name': self.exchange_name,
                'normalize_function': self._get_depth_normalize_function,
            }
        )
        return path, params, extra_data

    def _get_kline(
        self, symbol: str, period: str, count: int = 20, extra_data: Any = None, **kwargs: Any
    ):
        path = self._params.get_rest_path('get_kline')
        params = {
            'symbol': self._params.get_symbol(symbol),
            'interval': self._params.get_period(period),
            'limit': count,
        }
        extra_data = extra_data or {}
        extra_data.update(
            {
                'request_type': 'get_kline',
                'symbol_name': symbol,
                'asset_type': self.asset_type,
                'exchange_name': self.exchange_name,
                'normalize_function': self._get_kline_normalize_function,
            }
        )
        return path, params, extra_data

    def _get_exchange_info(self, extra_data: Any = None, **kwargs: Any):
        path = self._params.get_rest_path('get_exchange_info')
        extra_data = extra_data or {}
        extra_data.update(
            {
                'request_type': 'get_exchange_info',
                'asset_type': self.asset_type,
                'exchange_name': self.exchange_name,
                'normalize_function': self._get_exchange_info_normalize_function,
            }
        )
        return path, None, extra_data

    def _get_balance(self, extra_data: Any = None, **kwargs: Any):
        path = self._params.get_rest_path('get_balance')
        extra_data = extra_data or {}
        extra_data.update(
            {
                'request_type': 'get_balance',
                'symbol_name': None,
                'asset_type': self.asset_type,
                'exchange_name': self.exchange_name,
                'normalize_function': self._get_balance_normalize_function,
            }
        )
        return path, None, extra_data

    def _get_account(self, extra_data: Any = None, **kwargs: Any):
        path = self._params.get_rest_path('get_account')
        extra_data = extra_data or {}
        extra_data.update(
            {
                'request_type': 'get_account',
                'symbol_name': None,
                'asset_type': self.asset_type,
                'exchange_name': self.exchange_name,
                'normalize_function': self._get_account_normalize_function,
            }
        )
        return path, None, extra_data

    def _make_order(
        self,
        symbol: str,
        vol: Any,
        price: Any = None,
        order_type: str = 'buy-limit',
        offset: str = 'open',
        post_only: bool = False,
        client_order_id: Any = None,
        extra_data: Any = None,
        **kwargs: Any,
    ):
        path = self._params.get_rest_path('make_order')
        side, otype = order_type.split('-') if '-' in order_type else (order_type, 'limit')
        body = {
            'symbol': self._params.get_symbol(symbol),
            'side': side.upper(),
            'type': otype.upper(),
            'quantity': str(vol),
        }
        if price is not None:
            body['price'] = str(price)
        extra_data = extra_data or {}
        extra_data.update(
            {
                'request_type': 'make_order',
                'symbol_name': symbol,
                'asset_type': self.asset_type,
                'exchange_name': self.exchange_name,
                'normalize_function': self._make_order_normalize_function,
            }
        )
        return path, body, extra_data

    def _cancel_order(
        self, symbol: str, order_id: Any = None, extra_data: Any = None, **kwargs: Any
    ):
        path = self._params.get_rest_path('cancel_order')
        params = {'symbol': self._params.get_symbol(symbol), 'orderId': order_id}
        extra_data = extra_data or {}
        extra_data.update(
            {
                'request_type': 'cancel_order',
                'symbol_name': symbol,
                'asset_type': self.asset_type,
                'exchange_name': self.exchange_name,
                'normalize_function': self._cancel_order_normalize_function,
            }
        )
        return path, params, extra_data

    def _query_order(
        self, symbol: str, order_id: Any = None, extra_data: Any = None, **kwargs: Any
    ):
        path = self._params.get_rest_path('query_order')
        params = {'symbol': self._params.get_symbol(symbol)}
        if order_id is not None:
            params['orderId'] = order_id
        extra_data = extra_data or {}
        extra_data.update(
            {
                'request_type': 'query_order',
                'symbol_name': symbol,
                'asset_type': self.asset_type,
                'exchange_name': self.exchange_name,
                'normalize_function': self._query_order_normalize_function,
            }
        )
        return path, params, extra_data

    @staticmethod
    def _get_server_time_normalize_function(data: Any, extra_data: Any):
        if data is None:
            return [], False
        return [data] if isinstance(data, dict) else [{'serverTime': data}], True

    @staticmethod
    def _get_tick_normalize_function(data: Any, extra_data: Any):
        if ZebpayRequestData._is_error(data):
            return [], False
        if isinstance(data, dict):
            inner = data.get('data')
            return [inner] if inner is not None else [data], True
        return [], False

    @staticmethod
    def _get_depth_normalize_function(data: Any, extra_data: Any):
        if ZebpayRequestData._is_error(data):
            return [], False
        if isinstance(data, dict):
            inner = data.get('data')
            return [inner] if inner is not None else [data], True
        return [], False

    @staticmethod
    def _get_kline_normalize_function(data: Any, extra_data: Any):
        if ZebpayRequestData._is_error(data):
            return [], False
        if isinstance(data, dict):
            inner = data.get('data', [])
            return [inner], inner is not None
        if isinstance(data, list):
            return data, bool(data)
        return [], False

    @staticmethod
    def _get_exchange_info_normalize_function(data: Any, extra_data: Any):
        if ZebpayRequestData._is_error(data):
            return [], False
        if isinstance(data, dict):
            return [data], True
        if isinstance(data, list):
            return data, bool(data)
        return [], False

    @staticmethod
    def _get_balance_normalize_function(data: Any, extra_data: Any):
        if ZebpayRequestData._is_error(data):
            return [], False
        if isinstance(data, dict):
            return [data], True
        if isinstance(data, list):
            return data, bool(data)
        return [], False

    @staticmethod
    def _get_account_normalize_function(data: Any, extra_data: Any):
        if ZebpayRequestData._is_error(data):
            return [], False
        if isinstance(data, dict):
            return [data], True
        if isinstance(data, list):
            return data, bool(data)
        return [], False

    @staticmethod
    def _make_order_normalize_function(data: Any, extra_data: Any):
        if ZebpayRequestData._is_error(data):
            return [], False
        if isinstance(data, dict):
            return [data], True
        return [], False

    @staticmethod
    def _cancel_order_normalize_function(data: Any, extra_data: Any):
        if ZebpayRequestData._is_error(data):
            return [], False
        if isinstance(data, dict):
            return [data], True
        return [], False

    @staticmethod
    def _query_order_normalize_function(data: Any, extra_data: Any):
        if ZebpayRequestData._is_error(data):
            return [], False
        if isinstance(data, dict):
            return [data], True
        return [], False
