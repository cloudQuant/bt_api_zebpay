# ZEBPAY API Reference

## English | [中文](#中文)

### Exchange Code

`ZEBPAY___SPOT`

### Exchange Info

| Item | Value |
|------|-------|
| REST URL | `https://sapi.zebpay.com` |
| WebSocket URL | `wss://stream.zebpay.com` |
| Asset Type | SPOT |
| Legal Currency | INR, USDT |
| Plugin Entry | `bt_api_zebpay.plugin:register_plugin` |

### Supported Capabilities

| Capability | Supported |
|------------|-----------|
| GET_TICK | ✅ |
| GET_DEPTH | ✅ |
| GET_KLINE | ✅ |
| GET_EXCHANGE_INFO | ✅ |
| GET_BALANCE | ✅ |
| GET_ACCOUNT | ✅ |
| MAKE_ORDER | ✅ |
| CANCEL_ORDER | ✅ |
| QUERY_ORDER | ✅ |
| GET_SERVER_TIME | ✅ |

### REST Endpoints

| Action | Path | Method |
|--------|------|--------|
| ticker | `/api/v2/market/ticker` | GET |
| orderbook | `/api/v2/market/orderbook` | GET |
| klines | `/api/v2/market/klines` | GET |
| trades | `/api/v2/market/trades` | GET |
| exchangeInfo | `/api/v2/ex/exchangeInfo` | GET |
| system/time | `/api/v2/system/time` | GET |
| balance | `/api/v2/account/balance` | GET |
| order (place) | `/api/v2/order` | POST |
| order (cancel) | `/api/v2/order` | DELETE |
| order (query) | `/api/v2/order` | GET |

### Kline Periods

| Period | Zebpay Value |
|--------|-------------|
| 1m | 1m |
| 5m | 5m |
| 15m | 15m |
| 30m | 30m |
| 1h | 1h |
| 2h | 2h |
| 4h | 4h |
| 12h | 12h |
| 1d | 1d |
| 1w | 1w |

### API Usage

```python
from bt_api import BtApi

# Initialize
api = BtApi(
    exchange_kwargs={
        "ZEBPAY___SPOT": {
            "api_key": "your_api_key",
            "secret": "your_secret",
        }
    }
)

# Get ticker
ticker = api.get_tick("ZEBPAY___SPOT", "BTC_INR")

# Get depth
depth = api.get_depth("ZEBPAY___SPOT", "BTC_INR", count=20)

# Get klines
bars = api.get_kline("ZEBPAY___SPOT", "BTC_INR", period="1h", count=100)

# Get balance
balance = api.get_balance("ZEBPAY___SPOT")

# Place order
order = api.make_order("ZEBPAY___SPOT", "BTC_INR", volume=0.001, price=5000000, order_type="buy-limit")

# Query order
query = api.query_order("ZEBPAY___SPOT", "BTC_INR", order_id="your_order_id")

# Cancel order
api.cancel_order("ZEBPAY___SPOT", "BTC_INR", order_id="your_order_id")
```

### Container — ZebpayExchangeDataSpot

```python
from bt_api_zebpay import ZebpayExchangeDataSpot

info = ZebpayExchangeDataSpot()
print(info.get_rest_url())          # https://sapi.zebpay.com
print(info.get_wss_url())           # wss://stream.zebpay.com
print(info.get_kline_periods())     # { "1m": "1m", "5m": "5m", ... }
print(info.legal_currency)          # ["INR", "USDT"]
print(info.get_symbol("BTC_INR"))   # BTC-INR
```

---

## 中文

### 交易所代码

`ZEBPAY___SPOT`

### 交易所信息

| 项目 | 值 |
|------|-----|
| REST URL | `https://sapi.zebpay.com` |
| WebSocket URL | `wss://stream.zebpay.com` |
| 资产类型 | SPOT |
| 法定货币 | INR, USDT |
| 插件入口 | `bt_api_zebpay.plugin:register_plugin` |

### 支持的能力

| 能力 | 支持状态 |
|------|---------|
| GET_TICK | ✅ |
| GET_DEPTH | ✅ |
| GET_KLINE | ✅ |
| GET_EXCHANGE_INFO | ✅ |
| GET_BALANCE | ✅ |
| GET_ACCOUNT | ✅ |
| MAKE_ORDER | ✅ |
| CANCEL_ORDER | ✅ |
| QUERY_ORDER | ✅ |
| GET_SERVER_TIME | ✅ |

### REST 端点

| 动作 | 路径 | 方法 |
|------|------|------|
| ticker | `/api/v2/market/ticker` | GET |
| orderbook | `/api/v2/market/orderbook` | GET |
| klines | `/api/v2/market/klines` | GET |
| trades | `/api/v2/market/trades` | GET |
| exchangeInfo | `/api/v2/ex/exchangeInfo` | GET |
| system/time | `/api/v2/system/time` | GET |
| balance | `/api/v2/account/balance` | GET |
| order (下单) | `/api/v2/order` | POST |
| order (撤单) | `/api/v2/order` | DELETE |
| order (查询) | `/api/v2/order` | GET |

### K线周期

| 周期 | Zebpay 值 |
|------|---------|
| 1m | 1m |
| 5m | 5m |
| 15m | 15m |
| 30m | 30m |
| 1h | 1h |
| 2h | 2h |
| 4h | 4h |
| 12h | 12h |
| 1d | 1d |
| 1w | 1w |

### API 用法

```python
from bt_api import BtApi

# 初始化
api = BtApi(
    exchange_kwargs={
        "ZEBPAY___SPOT": {
            "api_key": "your_api_key",
            "secret": "your_secret",
        }
    }
)

# 获取行情
ticker = api.get_tick("ZEBPAY___SPOT", "BTC_INR")

# 获取深度
depth = api.get_depth("ZEBPAY___SPOT", "BTC_INR", count=20)

# 获取K线
bars = api.get_kline("ZEBPAY___SPOT", "BTC_INR", period="1h", count=100)

# 获取余额
balance = api.get_balance("ZEBPAY___SPOT")

# 下单
order = api.make_order("ZEBPAY___SPOT", "BTC_INR", volume=0.001, price=5000000, order_type="buy-limit")

# 查询订单
query = api.query_order("ZEBPAY___SPOT", "BTC_INR", order_id="your_order_id")

# 撤单
api.cancel_order("ZEBPAY___SPOT", "BTC_INR", order_id="your_order_id")
```

### 容器类 — ZebpayExchangeDataSpot

```python
from bt_api_zebpay import ZebpayExchangeDataSpot

info = ZebpayExchangeDataSpot()
print(info.get_rest_url())          # https://sapi.zebpay.com
print(info.get_wss_url())          # wss://stream.zebpay.com
print(info.get_kline_periods())     # { "1m": "1m", "5m": "5m", ... }
print(info.legal_currency)          # ["INR", "USDT"]
print(info.get_symbol("BTC_INR"))   # BTC-INR
```
