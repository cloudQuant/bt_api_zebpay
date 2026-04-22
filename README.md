# ZEBPAY

Exchange plugin for bt_api framework — Indian cryptocurrency exchange.

[![PyPI Version](https://img.shields.io/pypi/v/bt_api_zebpay.svg)](https://pypi.org/project/bt_api_zebpay/)
[![Python Versions](https://img.shields.io/pypi/pyversions/bt_api_zebpay.svg)](https://pypi.org/project/bt_api_zebpay/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/cloudQuant/bt_api_zebpay/actions/workflows/ci.yml/badge.svg)](https://github.com/cloudQuant/bt_api_zebpay/actions)
[![Docs](https://readthedocs.org/projects/bt-api-zebpay/badge/?version=latest)](https://bt-api-zebpay.readthedocs.io/)

---

## English | [中文](#中文)

### Overview

[Zebpay](https://www.zebpay.com/) is an **Indian cryptocurrency exchange** offering crypto trading with INR (Indian Rupee) and USDT pairs. This plugin integrates Zebpay into the [bt_api](https://github.com/cloudQuant/bt_api_py) unified trading framework, supporting **SPOT** markets.

### Features

- **REST API** — market data queries, order management, account queries
- **INR/USDT trading** — supports Indian Rupee and USDT trading pairs
- **Indian market focus** — Zebpay is a major Indian crypto exchange
- **Simple API key auth** — standard API key + secret authentication

### Exchange Code

| Code | Description | Asset Type |
|------|-------------|------------|
| `ZEBPAY___SPOT` | Zebpay spot markets | SPOT |

### Installation

```bash
pip install bt_api_zebpay
```

Or install from source:

```bash
git clone https://github.com/cloudQuant/bt_api_zebpay
cd bt_api_zebpay
pip install -e .
```

### Quick Start

```python
from bt_api import BtApi

api = BtApi(
    exchange_kwargs={
        "ZEBPAY___SPOT": {
            "api_key": "your_api_key",
            "secret": "your_secret",
        }
    }
)

# Get ticker data
ticker = api.get_tick("ZEBPAY___SPOT", "BTC_INR")
print(ticker)

# Get order book
depth = api.get_depth("ZEBPAY___SPOT", "BTC_INR", count=20)
print(depth)

# Get klines
bars = api.get_kline("ZEBPAY___SPOT", "BTC_INR", period="1h", count=100)
print(bars)
```

### Supported Operations

| Operation | Status | Description |
|-----------|--------|-------------|
| Ticker | ✅ | Real-time price and statistics |
| OrderBook/Depth | ✅ | Market depth and order book |
| Klines/Bars | ✅ | Historical OHLCV data |
| Exchange Info | ✅ | Trading rules and symbol info |
| Balance | ✅ | Account balance queries |
| Account | ✅ | Account information |
| Make Order | ✅ | Place limit/market orders |
| Cancel Order | ✅ | Cancel existing orders |
| Query Order | ✅ | Query order status |

### API Reference

#### Feed — ZebpayRequestDataSpot

Inherits from `ZebpayRequestData`. Access via `BtApi`.

```python
api.get_tick("ZEBPAY___SPOT", "BTC_INR")        # Ticker
api.get_depth("ZEBPAY___SPOT", "BTC_INR")       # Order book
api.get_kline("ZEBPAY___SPOT", "BTC_INR")      # Klines
api.get_exchange_info("ZEBPAY___SPOT")          # Exchange info
api.get_balance("ZEBPAY___SPOT")               # Balance
api.get_account("ZEBPAY___SPOT")                # Account info
```

#### Container — ZebpayExchangeDataSpot

Exchange metadata and configuration.

```python
from bt_api_zebpay import ZebpayExchangeDataSpot

info = ZebpayExchangeDataSpot()
print(info.get_rest_url())    # https://sapi.zebpay.com
print(info.get_wss_url())     # wss://stream.zebpay.com
print(info.get_kline_periods())  # { "1m": "1m", "5m": "5m", ... }
```

#### REST Endpoints

| Action | Path | Method |
|--------|------|--------|
| ticker | `/api/v2/market/ticker` | GET |
| orderbook | `/api/v2/market/orderbook` | GET |
| klines | `/api/v2/market/klines` | GET |
| trades | `/api/v2/market/trades` | GET |
| exchangeInfo | `/api/v2/ex/exchangeInfo` | GET |
| balance | `/api/v2/account/balance` | GET |
| order | `/api/v2/order` | POST |
| cancel_order | `/api/v2/order` | DELETE |

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

### Architecture

```
bt_api_zebpay/
├── src/bt_api_zebpay/
│   ├── containers/      # ZebpayExchangeDataSpot
│   ├── feeds/           # ZebpayRequestDataSpot
│   ├── exchange_data/    # Exchange metadata
│   ├── errors/          # Error translation
│   └── plugin.py        # register_plugin()
└── docs/
    └── index.md         # Bilingual API docs
```

### Requirements

- Python 3.9+
- bt_api_base >= 0.15

### Online Documentation

| Resource | Link |
|----------|------|
| Full Docs | https://bt-api-zebpay.readthedocs.io/ |
| Chinese Docs | https://bt-api-zebpay.readthedocs.io/zh/latest/ |
| GitHub Repository | https://github.com/cloudQuant/bt_api_zebpay |
| Issue Tracker | https://github.com/cloudQuant/bt_api_zebpay/issues |

### License

MIT License — see [LICENSE](LICENSE) for details.

---

## 中文

### 概述

[Zebpay](https://www.zebpay.com/) 是一家 **印度加密货币交易所**，提供以印度卢比（INR）和 USDT 计价的加密货币交易。本插件将 Zebpay 接入 [bt_api](https://github.com/cloudQuant/bt_api_py) 统一交易框架，支持 **现货 (SPOT)** 市场。

### 功能特点

- **REST API** — 行情查询、订单管理、账户查询
- **INR/USDT 交易对** — 支持印度卢比和 USDT 交易对
- **印度市场监管** — 主要印度加密货币交易所
- **简单 API Key 认证** — 标准 API Key + Secret 认证方式

### 交易所代码

| 代码 | 描述 | 资产类型 |
|------|--------|----------|
| `ZEBPAY___SPOT` | Zebpay 现货市场 | SPOT |

### 安装

```bash
pip install bt_api_zebpay
```

或从源码安装：

```bash
git clone https://github.com/cloudQuant/bt_api_zebpay
cd bt_api_zebpay
pip install -e .
```

### 快速开始

```python
from bt_api import BtApi

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
print(ticker)

# 获取订单簿
depth = api.get_depth("ZEBPAY___SPOT", "BTC_INR", count=20)
print(depth)

# 获取K线
bars = api.get_kline("ZEBPAY___SPOT", "BTC_INR", period="1h", count=100)
print(bars)
```

### 支持的操作

| 操作 | 状态 | 说明 |
|------|------|------|
| 行情 (Ticker) | ✅ | 实时价格和统计 |
| 订单簿 (OrderBook) | ✅ | 市场深度和挂单 |
| K线 (Klines) | ✅ | 历史OHLCV数据 |
| 交易所信息 | ✅ | 交易规则和交易对信息 |
| 余额 (Balance) | ✅ | 账户余额查询 |
| 账户 (Account) | ✅ | 账户信息 |
| 下单 (Make Order) | ✅ | 限价/市价下单 |
| 撤单 (Cancel Order) | ✅ | 取消现有订单 |
| 查询订单 (Query Order) | ✅ | 查询订单状态 |

### API 参考

#### Feed — ZebpayRequestDataSpot

继承自 `ZebpayRequestData`，通过 `BtApi` 访问。

```python
api.get_tick("ZEBPAY___SPOT", "BTC_INR")        # 行情
api.get_depth("ZEBPAY___SPOT", "BTC_INR")       # 订单簿
api.get_kline("ZEBPAY___SPOT", "BTC_INR")      # K线
api.get_exchange_info("ZEBPAY___SPOT")          # 交易所信息
api.get_balance("ZEBPAY___SPOT")               # 余额
api.get_account("ZEBPAY___SPOT")                # 账户信息
```

#### Container — ZebpayExchangeDataSpot

交易所元数据和配置。

```python
from bt_api_zebpay import ZebpayExchangeDataSpot

info = ZebpayExchangeDataSpot()
print(info.get_rest_url())    # https://sapi.zebpay.com
print(info.get_wss_url())     # wss://stream.zebpay.com
print(info.get_kline_periods())  # { "1m": "1m", "5m": "5m", ... }
```

#### REST 端点

| 动作 | 路径 | 方法 |
|------|------|------|
| ticker | `/api/v2/market/ticker` | GET |
| orderbook | `/api/v2/market/orderbook` | GET |
| klines | `/api/v2/market/klines` | GET |
| trades | `/api/v2/market/trades` | GET |
| exchangeInfo | `/api/v2/ex/exchangeInfo` | GET |
| balance | `/api/v2/account/balance` | GET |
| order | `/api/v2/order` | POST |
| cancel_order | `/api/v2/order` | DELETE |

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

### 项目结构

```
bt_api_zebpay/
├── src/bt_api_zebpay/
│   ├── containers/      # ZebpayExchangeDataSpot
│   ├── feeds/           # ZebpayRequestDataSpot
│   ├── exchange_data/    # 交易所元数据
│   ├── errors/          # 错误翻译
│   └── plugin.py        # register_plugin()
└── docs/
    └── index.md         # 中英文API文档
```

### 系统要求

- Python 3.9+
- bt_api_base >= 0.15

### 在线文档

| 资源 | 链接 |
|------|------|
| 完整文档 | https://bt-api-zebpay.readthedocs.io/ |
| 中文文档 | https://bt-api-zebpay.readthedocs.io/zh/latest/ |
| GitHub 仓库 | https://github.com/cloudQuant/bt_api_zebpay |
| 问题反馈 | https://github.com/cloudQuant/bt_api_zebpay/issues |

### 许可证

MIT 许可证 — 详见 [LICENSE](LICENSE)。
