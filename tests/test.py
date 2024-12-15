import alpaca_trade_api as tradeapi

# 配置API密钥
ALPACA_API_KEY = 'PKX2X38HUKZAYC4CRQ5N'
ALPACA_SECRET_KEY = 'sjF60LaIahDqfgFoo03CdwgpXxDgK4E7SQr72sOr'
ALPACA_BASE_URL = 'https://paper-api.alpaca.markets'  # 使用模拟交易的URL

# 交易配置
ETF_SYMBOL = 'VOO'
USD_AMOUNT = 100  # 交易金额为100美元

def place_order(symbol, usd_amount, api):
    """在Alpaca上创建订单"""
    # 获取当前价格
    asset = api.get_asset(symbol)
    if not asset.tradable:
        raise ValueError(f"{symbol} is not tradable on Alpaca.")

    latest_price = api.get_latest_trade(symbol).price
    # 根据最新价格计算购买数量
    quantity = round(usd_amount / latest_price, 2)

    # 创建买入订单
    api.submit_order(
        symbol=symbol,
        qty=quantity,
        side='buy',
        type='market',
        time_in_force='day'
    )
    print(f"Successfully placed order: Buy {quantity} shares of {symbol} at ${latest_price:.2f} each")

def main():
    # 初始化Alpaca API客户端
    api = tradeapi.REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_BASE_URL)

    # 下单买入VOO
    place_order(ETF_SYMBOL, USD_AMOUNT, api)

if __name__ == '__main__':
    main()
